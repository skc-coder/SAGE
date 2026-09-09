#!/usr/bin/env python3
import os, sys, json, tomllib, base64, io, time
from concurrent.futures import ThreadPoolExecutor, as_completed
import pypdf
import requests
from PIL import Image

CREDENTIALS_PATH = os.path.expanduser("~/Documents/Security_and_Credentials/api_keys.toml")
with open(CREDENTIALS_PATH, "rb") as f:
    config = tomllib.load(f)

API_KEYS = config.get("gemini_api_keys", [])
if not API_KEYS:
    print("Error: No Gemini API keys found.")
    sys.exit(1)

print(f"Loaded {len(API_KEYS)} Gemini API Key(s).")
sys.stdout.flush()

PDF_PATH = "/home/skc/dev/SAGE/pdfs/Physical Geography Oneshot_.-compressed.pdf"
OUT_JSON = "/tmp/physical_geography_gemini_full.json"

PROMPT = """Transcribe all handwritten geography notes, formulas, diagrams, definitions, and PYQs on this slide. Be exhaustive."""

def process_page(args):
    page_num, img_bytes, embedded_txt, worker_id = args
    key = API_KEYS[worker_id % len(API_KEYS)]
    
    if len(embedded_txt) > 400:
        return {"page": page_num, "content": embedded_txt, "type": "text"}
        
    if not img_bytes:
        return {"page": page_num, "content": embedded_txt, "type": "empty"}

    try:
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        buf = io.BytesIO()
        img.save(buf, format='JPEG', quality=80)
        b64_img = base64.b64encode(buf.getvalue()).decode('utf-8')
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={key}"
        payload = {
            "contents": [{
                "parts": [
                    {"inline_data": {"mime_type": "image/jpeg", "data": b64_img}},
                    {"text": PROMPT}
                ]
            }]
        }
        
        resp = requests.post(url, json=payload, timeout=30)
        if resp.status_code == 200:
            res_json = resp.json()
            text = res_json['candidates'][0]['content']['parts'][0]['text']
            return {"page": page_num, "content": text, "type": "gemini_ocr"}
        else:
            return {"page": page_num, "content": f"[HTTP {resp.status_code} Error: {resp.text[:100]}]", "type": "error"}
    except Exception as e:
        return {"page": page_num, "content": f"[Exception: {e}]", "type": "error"}

def main():
    reader = pypdf.PdfReader(PDF_PATH)
    total_pages = len(reader.pages)
    print(f"Extracting page images for {total_pages} pages...", flush=True)
    
    tasks = []
    for idx in range(total_pages):
        page_num = idx + 1
        page = reader.pages[idx]
        embedded = page.extract_text() or ""
        clean_lines = [l.strip() for l in embedded.split('\n') if l.strip() and 'Journey' not in l and '7597637099' not in l]
        clean_embedded = "\n".join(clean_lines)
        
        img_bytes = None
        if len(page.images) > 0:
            img_bytes = list(page.images)[0].data
            
        tasks.append((page_num, img_bytes, clean_embedded, idx))

    print(f"Dispatching {total_pages} pages to Gemini 2.5 Flash API...", flush=True)
    results = {}
    
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(process_page, t): t[0] for t in tasks}
        completed = 0
        for future in as_completed(futures):
            p_num = futures[future]
            res = future.result()
            results[p_num] = res
            completed += 1
            if completed % 25 == 0 or completed == total_pages:
                elapsed = time.time() - start_time
                print(f"Gemini API Progress: {completed}/{total_pages} pages transcribed ({elapsed:.1f}s)...", flush=True)

    sorted_results = [results[p] for p in sorted(results.keys())]
    with open(OUT_JSON, "w") as f:
        json.dump(sorted_results, f, indent=2)
        
    print(f"FINISHED! All {total_pages} pages processed in {time.time() - start_time:.1f}s. Saved to {OUT_JSON}", flush=True)

if __name__ == "__main__":
    main()
