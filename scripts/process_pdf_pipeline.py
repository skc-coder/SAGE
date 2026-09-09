#!/usr/bin/env python3
import sys, os, json, re, time
import pypdf, pytesseract
from PIL import Image
import io

def extract_pdf(pdf_path, output_json):
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file {pdf_path} does not exist.")
        sys.exit(1)
        
    print(f"Starting extraction for {pdf_path}...")
    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    
    pages_data = []
    start_time = time.time()
    
    for i in range(total_pages):
        page_num = i + 1
        page = reader.pages[i]
        
        # Embedded text
        emb_text = (page.extract_text() or '').strip()
        clean_emb = '\n'.join([line.strip() for line in emb_text.split('\n') if line.strip()])
        
        # Tesseract OCR on images
        ocr_lines = []
        for img in page.images:
            try:
                image = Image.open(io.BytesIO(img.data)).convert('RGB')
                txt = pytesseract.image_to_string(image)
                if txt.strip():
                    ocr_lines.append(txt.strip())
            except Exception:
                pass
                
        clean_ocr = '\n'.join(ocr_lines)
        
        pages_data.append({
            "page": page_num,
            "embedded": clean_emb,
            "ocr": clean_ocr
        })
        
        if page_num % 50 == 0 or page_num == total_pages:
            print(f"Processed {page_num}/{total_pages} pages ({time.time()-start_time:.1f}s)...")
            
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(pages_data, f, indent=2)
        
    print(f"Extraction complete! Saved to {output_json}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: process_pdf_pipeline.py <pdf_path> [output_json]")
        sys.exit(1)
    pdf_p = sys.argv[1]
    out_j = sys.argv[2] if len(sys.argv) > 2 else "/tmp/pdf_extract.json"
    extract_pdf(pdf_p, out_j)
