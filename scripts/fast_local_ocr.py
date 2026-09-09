import pytesseract, json, glob, time, sys, os
from PIL import Image

PNG_DIR = "/tmp/pdf_all_png"
OUT_JSON = "/tmp/physical_geography_local_ocr.json"

images = sorted(glob.glob(f"{PNG_DIR}/page-*.png"))
print(f"Starting local Tesseract OCR for {len(images)} pages...")

start_time = time.time()
results = []

for idx, img_path in enumerate(images):
    page_num = idx + 1
    try:
        image = Image.open(img_path)
        txt = pytesseract.image_to_string(image)
        results.append({
            "page": page_num,
            "content": txt,
            "type": "local_ocr"
        })
    except Exception as e:
        results.append({
            "page": page_num,
            "content": f"[OCR Error: {e}]",
            "type": "error"
        })
        
    if page_num % 50 == 0 or page_num == len(images):
        print(f"Local OCR Progress: {page_num}/{len(images)} pages ({time.time()-start_time:.1f}s)...", flush=True)

with open(OUT_JSON, "w") as f:
    json.dump(results, f, indent=2)

print(f"LOCAL OCR COMPLETE! Processed all {len(images)} pages in {time.time()-start_time:.1f}s.")
