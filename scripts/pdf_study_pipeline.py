#!/usr/bin/env python3
"""
SAGE PDF Processing & Note Generation Pipeline
Supports both embedded-text PDFs and handwritten/scanned PDF notes.
Uses PyMuPDF/pypdf for text/image extraction and Tesseract OCR for handwritten images.
"""
import os
import sys
import json
import argparse
import pypdf
import pytesseract
from PIL import Image
import io

def process_pdf(pdf_path, output_json, max_pages=None):
    if not os.path.exists(pdf_path):
        print(f"Error: PDF path '{pdf_path}' does not exist.")
        sys.exit(1)
        
    print(f"Opening PDF: {pdf_path}")
    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")
    
    pages_to_process = min(total_pages, max_pages) if max_pages else total_pages
    pages_data = []
    
    for idx in range(pages_to_process):
        page_num = idx + 1
        page = reader.pages[idx]
        
        # 1. Embedded text extraction
        raw_text = page.extract_text() or ""
        clean_lines = [l.strip() for l in raw_text.split('\n') if l.strip() and 'Journey' not in l and '7597637099' not in l]
        clean_embedded = "\n".join(clean_lines)
        
        # 2. Image / OCR extraction
        ocr_text = ""
        has_images = len(page.images) > 0
        if len(clean_embedded) < 50 and has_images:
            ocr_lines = []
            for img_idx, img in enumerate(page.images):
                try:
                    img_bytes = img.data
                    image = Image.open(io.BytesIO(img_bytes)).convert("RGB")
                    # Tesseract OCR
                    txt = pytesseract.image_to_string(image)
                    if txt.strip():
                        ocr_lines.append(txt.strip())
                except Exception as e:
                    pass
            ocr_text = "\n".join(ocr_lines)
            
        final_text = clean_embedded if len(clean_embedded) >= 50 else ocr_text
        is_pyq = any(k in final_text.upper() for k in ["QUES", "CDS", "NDA", "CAPF", "AFCAT", "WHICH OF THE FOLLOWING"])
        
        pages_data.append({
            "page": page_num,
            "has_embedded_text": len(clean_embedded) >= 50,
            "embedded_text": clean_embedded,
            "ocr_text": ocr_text,
            "combined_text": final_text,
            "is_pyq": is_pyq
        })
        
        if page_num % 25 == 0 or page_num == pages_to_process:
            print(f"Processed {page_num}/{pages_to_process} pages...")

    with open(output_json, "w") as f:
        json.dump(pages_data, f, indent=2)
    print(f"Successfully saved page index to {output_json}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SAGE PDF Extractor Pipeline")
    parser.add_argument("--pdf", required=True, help="Path to PDF file")
    parser.add_argument("--out", required=True, help="Output JSON path")
    parser.add_argument("--max-pages", type=int, default=None, help="Max pages to process")
    args = parser.parse_args()
    
    process_pdf(args.pdf, args.out, args.max_pages)
