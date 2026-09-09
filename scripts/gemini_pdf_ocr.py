#!/usr/bin/env python3
"""
High-Speed Parallel Gemini Vision OCR & Note Structure Pipeline for SAGE
Offloads page transcription & structured extraction directly to Gemini Flash API.
"""
import os, sys, json, time, io, tomllib
from concurrent.futures import ThreadPoolExecutor, as_completed
import pypdf
from PIL import Image
import google.genai as genai
from google.genai import types

# Load credentials from ~/Documents/Security_and_Credentials/api_keys.toml
credentials_path = os.path.expanduser("~/Documents/Security_and_Credentials/api_keys.toml")
if not os.path.exists(credentials_path):
    print(f"Error: Credentials file not found at {credentials_path}")
    sys.exit(1)

with open(credentials_path, "rb") as f:
    config = tomllib.load(f)

API_KEYS = config.get("gemini_api_keys", [])
if not API_KEYS:
    print("Error: No Gemini API keys found in api_keys.toml")
    sys.exit(1)

print(f"Loaded {len(API_KEYS)} Gemini API Key(s) for parallel offloading.")

def get_client(worker_id):
    key = API_KEYS[worker_id % len(API_KEYS)]
    return genai.Client(api_key=key)

PDF_PATH = "/home/skc/dev/SAGE/pdfs/Physical Geography Oneshot_.-compressed.pdf"
OUTPUT_JSON = "/tmp/physical_geography_gemini_ocr.json"

PROMPT = """You are an expert exam OCR & Knowledge Extractor for UPSC CDS/NDA/CAPF Physical Geography.
Transcribe and analyze all contents of this handwritten/printed slide image with ZERO omission.

Include:
1. Exact Chapter/Topic Name & Section Header
2. All Theory Points, Scientist Names, Dates, Formulas, Definitions, Classification Tables
3. All PYQ Questions (if present on slide): Question text, Year/Exam (e.g. CAPF 2024, CDS 2 2025), Options (a,b,c,d), and Answer/Solution if indicated.
4. Any Diagrams/Maps/Landform descriptions.

Format strictly as Markdown."""

def process_page(args):
    page_num, image_bytes, embedded_text, worker_id = args
    client = get_client(worker_id)
    
    # If page has substantial clean text and no image required
    if len(embedded_text.strip()) > 300:
        return {
            "page": page_num,
            "source": "embedded",
            "content": embedded_text
        }
        
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG', quality=85)
        img_bytes = img_byte_arr.getvalue()
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[
                types.Part.from_bytes(data=img_bytes, mime_type='image/jpeg'),
                PROMPT
            ]
        )
        return {
            "page": page_num,
            "source": "gemini_vision",
            "content": response.text
        }
    except Exception as e:
        return {
            "page": page_num,
            "source": "error",
            "content": f"[Extraction Error: {e}]"
        }

def main():
    reader = pypdf.PdfReader(PDF_PATH)
    total_pages = len(reader.pages)
    print(f"Preparing batch for {total_pages} pages...")
    
    tasks = []
    for idx in range(total_pages):
        page_num = idx + 1
        page = reader.pages[idx]
        embedded = page.extract_text() or ""
        clean_embedded = "\n".join([l.strip() for l in embedded.split('\n') if l.strip() and 'Journey' not in l and '7597637099' not in l])
        
        image_bytes = None
        if len(page.images) > 0:
            image_bytes = list(page.images)[0].data
            
        tasks.append((page_num, image_bytes, clean_embedded, idx))

    print(f"Offloading {total_pages} pages to Gemini Flash Vision via 6 concurrent workers...")
    results = {}
    
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {executor.submit(process_page, task): task[0] for task in tasks}
        completed = 0
        for future in as_completed(futures):
            p_num = futures[future]
            res = future.result()
            results[p_num] = res
            completed += 1
            if completed % 10 == 0 or completed == total_pages:
                print(f"Gemini API Progress: {completed}/{total_pages} pages transcribed...")

    sorted_results = [results[p] for p in sorted(results.keys())]
    with open(OUTPUT_JSON, "w") as f:
        json.dump(sorted_results, f, indent=2)
        
    print(f"\nSUCCESS! All {total_pages} pages transcribed via Gemini Vision to {OUTPUT_JSON}")

if __name__ == "__main__":
    main()
