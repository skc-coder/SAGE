#!/usr/bin/env python3
import sys
import re
import os
import pypdf

def study_chapter(pdf_path, chapter_num):
    print(f"📖 Loading PDF: {pdf_path} for Chapter {chapter_num}...")
    if not os.path.exists(pdf_path):
        print(f"❌ Error: PDF file '{pdf_path}' not found!")
        sys.exit(1)
        
    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Total Pages in PDF: {total_pages}")
    
    chapter_str = f"{chapter_num}."
    chapter_title_str = f"Chapter {chapter_num}"
    
    start_page = None
    end_page = None
    chapter_name = "Unknown Chapter"
    
    # 1. Parse PDF Outline / Bookmarks
    def find_bookmark(outlines):
        nonlocal start_page, chapter_name
        for item in outlines:
            if isinstance(item, list):
                find_bookmark(item)
            else:
                title = getattr(item, "title", str(item))
                if chapter_str in title or chapter_title_str in title or f"{chapter_num} " in title:
                    page = reader.get_destination_page_number(item) if hasattr(item, "page") else None
                    if page is not None:
                        start_page = page
                        chapter_name = title
                        print(f"🎯 Found Bookmark: '{title}' at page {page + 1}")
                        
    find_bookmark(reader.outline)
    
    if start_page is None:
        print(f"⚠️ Bookmark not found in PDF outline for Chapter {chapter_num}. Searching page text...")
        for p_num in range(total_pages):
            text = reader.pages[p_num].extract_text()
            if f"CHAPTER {chapter_num}" in text.upper() or f"{chapter_num}." in text:
                start_page = p_num
                print(f"🎯 Text Match found at page {p_num + 1}")
                break

    if start_page is None:
        print(f"❌ Could not find start page for Chapter {chapter_num}.")
        sys.exit(1)

    # Determine end page (up to next chapter or 35 pages max)
    end_page = min(start_page + 40, total_pages)
    
    extracted_text = ""
    for p in range(start_page, end_page):
        t = reader.pages[p].extract_text()
        if p > start_page + 2 and ("CHAPTER " in t.upper() or re.search(r"\n\d{1,2}\.\s+[A-Z]", t)):
            # Check if next chapter started
            match = re.search(r"CHAPTER\s+(\d+)", t, re.IGNORECASE)
            if match and int(match.group(1)) != int(chapter_num):
                print(f"🛑 Next Chapter {match.group(1)} detected at page {p+1}. Stopping extraction.")
                end_page = p
                break
        extracted_text += f"\n--- PDF PAGE {p+1} ---\n" + t
        
    out_file = f"chapter_{chapter_num}_extracted.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(extracted_text)
        
    print(f"✅ Extracted pages {start_page+1} to {end_page} ({len(extracted_text)} chars) into '{out_file}'")
    
    # 2. Extract Questions Summary
    pe_start = extracted_text.find("PRACTICE EXERCISE")
    if pe_start != -1:
        pe_text = extracted_text[pe_start:]
        q_matches = re.findall(r"\n(\d+)\.\s+(.*?)(?=\n\d+\.\s+|$)", pe_text, re.DOTALL)
        print(f"📊 Practice Exercise detected: ~{len(q_matches)} questions found.")
    else:
        print("ℹ️ Note: Practice Exercise section header not found directly in text excerpt.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 chapter_study_helper.py <pdf_path> <chapter_num>")
        sys.exit(1)
    study_chapter(sys.argv[1], sys.argv[2])
