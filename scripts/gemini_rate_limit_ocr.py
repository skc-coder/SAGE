#!/usr/bin/env python3
import os, sys, json, tomllib, base64, glob, time, requests

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

# Load existing results to skip successful ones
results_map = {}
if os.path.exists(OUT_JSON):
    try:
        with open(OUT_JSON) as f:
            existing = json.load(f)
            for item in existing:
                if item.get("type") == "gemini_ocr" and len(item.get("content", "")) > 100:
                    results_map[item["page"]] = item
    except Exception:
        pass

print(f"Already successfully transcribed: {len(results_map)}/251 pages.")

images = sorted(glob.glob(f"{PNG_DIR}/page-*.png"))

key_idx = 0
for idx, img_path in enumerate(images):
    page_num = idx + 1
    if page_num in results_map:
        continue
        
    success = False
    attempts = 0
    while not success and attempts < 5:
        key = API_KEYS[key_idx % len(API_KEYS)]
        key_idx += 1
        
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
            
            resp = requests.post(url, json=payload, timeout=30)
            if resp.status_code == 200:
                res_json = resp.json()
                text = res_json['candidates'][0]['content']['parts'][0]['text']
                results_map[page_num] = {"page": page_num, "content": text, "type": "gemini_ocr"}
                success = True
                print(f"Page {page_num}/251 transcribed successfully!")
            elif resp.status_code == 429:
                print(f"Rate limited on key #{key_idx%len(API_KEYS)}. Waiting 3 seconds...")
                time.sleep(3)
                attempts += 1
            else:
                print(f"Page {page_num} HTTP Error {resp.status_code}: {resp.text[:80]}")
                time.sleep(2)
                attempts += 1
        except Exception as e:
            print(f"Page {page_num} Exception: {e}")
            time.sleep(2)
            attempts += 1

    # Save progress after every page
    sorted_res = [results_map[p] for p in sorted(results_map.keys())]
    with open(OUT_JSON, "w") as f:
        json.dump(sorted_res, f, indent=2)

print(f"FINISHED! Total successfully transcribed pages: {len(results_map)}/251")
