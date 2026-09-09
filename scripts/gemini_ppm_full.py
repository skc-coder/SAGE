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
    while True:
        images = sorted(glob.glob(f"{PNG_DIR}/page-*.png"))
        print(f"Current PNGs rendered: {len(images)}/251...", flush=True)
        if len(images) >= 251:
            break
        time.sleep(2)
        
    print(f"All 251 pages rendered! Dispatching to Gemini 2.5 Flash Vision API...")
    tasks = [(idx + 1, img_path, idx) for idx, img_path in enumerate(images)]
    
    results = {}
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = {executor.submit(process_img, t): t[0] for t in tasks}
        completed = 0
        for future in as_completed(futures):
            p_num = futures[future]
            res = future.result()
            results[p_num] = res
            completed += 1
            if completed % 25 == 0 or completed == len(tasks):
                print(f"Gemini API Progress: {completed}/{len(tasks)} pages transcribed ({time.time()-start_time:.1f}s)...", flush=True)

    sorted_results = [results[p] for p in sorted(results.keys())]
    with open(OUT_JSON, "w") as f:
        json.dump(sorted_results, f, indent=2)
        
    print(f"FINISHED! All {len(tasks)} pages processed in {time.time() - start_time:.1f}s. Output: {OUT_JSON}")

if __name__ == "__main__":
    main()
