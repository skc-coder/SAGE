#!/usr/bin/env python3
import os, sys, json, tomllib, base64, glob, time, requests
from concurrent.futures import ThreadPoolExecutor, as_completed

CREDENTIALS_PATH = os.path.expanduser("~/Documents/Security_and_Credentials/api_keys.toml")
with open(CREDENTIALS_PATH, "rb") as f:
    config = tomllib.load(f)

API_KEYS = config.get("gemini_api_keys", [])
print(f"Loaded {len(API_KEYS)} Gemini API Key(s).")

PNG_DIR = "/tmp/pdf_all_png"
OUT_JSON = "/tmp/physical_geography_gemini_full.json"

PROMPT = """You are an expert exam transcript generator for Physical Geography UPSC CDS/NDA/CAPF.
Transcribe all handwritten and printed notes on this slide in complete detail with ZERO omission.
Include headers, key concepts, definitions, formulas, scientist names, dates, diagrams, and PYQ questions with options & answers."""

def process_img(args):
    page_num, img_path, worker_id = args
    key = API_KEYS[worker_id % len(API_KEYS)]

    try:
        with open(img_path, "rb") as f:
            b64_img = base64.b64encode(f.read()).decode('utf-8')
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={key}"
        payload = {
            "contents": [{
                "parts": [
                    {"inline_data": {"mime_type": "image/png", "data": b64_img}},
                    {"text": PROMPT}
                ]
            }]
        }
        
        resp = requests.post(url, json=payload, timeout=40)
        if resp.status_code == 200:
            res_json = resp.json()
            text = res_json['candidates'][0]['content']['parts'][0]['text']
            return {"page": page_num, "content": text, "type": "gemini_ocr"}
        else:
            return {"page": page_num, "content": f"[HTTP Error {resp.status_code}]", "type": "error"}
    except Exception as e:
        return {"page": page_num, "content": f"[Exception: {e}]", "type": "error"}

def main():
    processed_pages = set()
    results = {}
    total_expected = 251
    start_time = time.time()

    print("Starting Streaming Gemini Flash API Processing...", flush=True)

    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = {}
        
        while len(results) < total_expected:
            images = sorted(glob.glob(f"{PNG_DIR}/page-*.png"))
            new_tasks = []
            
            for img_path in images:
                filename = os.path.basename(img_path)
                try:
                    # page-001.png -> 1
                    page_num = int(filename.split('-')[1].split('.')[0])
                    if page_num not in processed_pages and page_num not in futures:
                        processed_pages.add(page_num)
                        new_tasks.append((page_num, img_path, page_num - 1))
                except Exception:
                    pass
            
            for task in new_tasks:
                fut = executor.submit(process_img, task)
                futures[task[0]] = fut
                
            # Check completed futures
            done_pages = []
            for page_num, fut in futures.items():
                if page_num not in results and fut.done():
                    results[page_num] = fut.result()
                    done_pages.append(page_num)
                    
            if done_pages and (len(results) % 15 == 0 or len(results) == total_expected):
                elapsed = time.time() - start_time
                print(f"Gemini API Streaming Progress: {len(results)}/{total_expected} pages transcribed ({elapsed:.1f}s)...", flush=True)
                # Incremental save
                sorted_res = [results[k] for k in sorted(results.keys())]
                with open(OUT_JSON, "w") as f:
                    json.dump(sorted_res, f, indent=2)

            time.sleep(1)

    sorted_res = [results[k] for k in sorted(results.keys())]
    with open(OUT_JSON, "w") as f:
        json.dump(sorted_res, f, indent=2)
        
    print(f"ALL 251 PAGES COMPLETED in {time.time() - start_time:.1f}s!")

if __name__ == "__main__":
    main()
