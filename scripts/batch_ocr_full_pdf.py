import pypdf, pytesseract, json, sys, os, time
from PIL import Image
import io

pdf_path = "/home/skc/dev/SAGE/pdfs/Physical Geography Oneshot_.-compressed.pdf"
out_json = "/tmp/pdf_251_full_ocr.json"

reader = pypdf.PdfReader(pdf_path)
total = len(reader.pages)

print(f"Starting line-by-line OCR for all {total} pages of Physical Geography PDF...")

results = []
start_time = time.time()

for idx in range(total):
    page_num = idx + 1
    page = reader.pages[idx]
    
    embedded = page.extract_text() or ""
    clean_lines = [l.strip() for l in embedded.split('\n') if l.strip() and 'Journey' not in l and '7597637099' not in l]
    clean_embedded = "\n".join(clean_lines)
    
    ocr_lines = []
    if len(page.images) > 0:
        for img_idx, img in enumerate(page.images):
            try:
                image = Image.open(io.BytesIO(img.data)).convert('RGB')
                txt = pytesseract.image_to_string(image)
                if txt.strip():
                    ocr_lines.append(txt.strip())
            except Exception:
                pass
                
    ocr_text = "\n".join(ocr_lines)
    
    results.append({
        "page": page_num,
        "embedded": clean_embedded,
        "ocr": ocr_text,
        "combined": clean_embedded if len(clean_embedded) > 150 else (clean_embedded + "\n" + ocr_text)
    })
    
    if page_num % 25 == 0 or page_num == total:
        print(f"Progress: {page_num}/{total} pages extracted ({time.time()-start_time:.1f}s)...", flush=True)

with open(out_json, "w") as f:
    json.dump(results, f, indent=2)

print(f"Extracted all {total} pages to {out_json} in {time.time()-start_time:.1f}s!")
