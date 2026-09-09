import json, os

with open("/tmp/pdf_251_full_ocr.json") as f:
    pages = json.load(f)

print(f"Loaded {len(pages)} line-by-line transcribed pages!")

notes_dir = "/home/skc/dev/SAGE/content/cds/geography/notes"
os.makedirs(notes_dir, exist_ok=True)

chapters = [
    {"slug": "universe", "title": "Universe and Solar System", "pages": range(1, 17), "difficulty": "Hard"},
    {"slug": "latitudes-longitudes", "title": "Latitudes, Longitudes and Time Systems", "pages": range(17, 56), "difficulty": "Medium"},
    {"slug": "geomorphology", "title": "Geomorphology and Earth Interior", "pages": range(56, 78), "difficulty": "Hard"},
    {"slug": "plate-tectonics", "title": "Plate Tectonics, Mountains and Volcanism", "pages": range(78, 95), "difficulty": "Hard"},
    {"slug": "rocks-minerals", "title": "Rocks, Minerals and Rock Cycle", "pages": range(95, 104), "difficulty": "Medium"},
    {"slug": "landforms", "title": "Geomorphic Processes and Landforms", "pages": range(104, 147), "difficulty": "Hard"},
    {"slug": "atmosphere-ozone", "title": "Atmosphere, Ozone Layer and Greenhouse Effect", "pages": range(147, 163), "difficulty": "Medium"},
    {"slug": "winds-cyclones", "title": "Pressure Belts, Local Winds and Cyclones", "pages": range(163, 185), "difficulty": "Hard"},
    {"slug": "clouds-rainfall", "title": "Condensation, Clouds and World Rainfall", "pages": range(185, 205), "difficulty": "Medium"},
    {"slug": "koeppen-climate", "title": "Koeppen Climate Classification and Indian Climate", "pages": range(205, 229), "difficulty": "Hard"},
    {"slug": "oceanography", "title": "Oceanography, Ocean Currents and Coral Reefs", "pages": range(229, 252), "difficulty": "Hard"}
]

page_map = {p["page"]: p for p in pages}

for ch in chapters:
    ch_slug = ch["slug"]
    ch_title = ch["title"]
    ch_pages = ch["pages"]
    
    sections = []
    for p in ch_pages:
        item = page_map.get(p, {})
        emb = item.get("embedded", "").strip()
        ocr = item.get("ocr", "").strip()
        
        content_parts = []
        if emb:
            content_parts.append(f"**Embedded Text / PYQs:**\n{emb}")
        if ocr:
            content_parts.append(f"**Handwritten Slide Notes & Diagram Annotations:**\n{ocr}")
            
        full_p_text = "\n\n".join(content_parts) if content_parts else "_No text content on this page._"
        sections.append(f"### Page {p}\n\n{full_p_text}")
        
    chapter_content = "\n\n---\n\n".join(sections)
    
    note_md = f"""---
exam: "CDS"
subject: "Physical Geography"
topic: "{ch_title}"
difficulty: "{ch['difficulty']}"
tags: [cds, geography, physical-geography, {ch_slug}, topic]
---

# {ch_title}

Exhaustive, page-by-page, line-by-line master notes covering all handwritten slides, diagram annotations, formulas, definitions, and PYQs for **{ch_title}** from the 251-page Physical Geography Master Class.

---

## Page-by-Page Line-by-Line Complete Transcripts & Notes

{chapter_content}

---

## Navigation

- [[cds/geography/geography_overview|Physical Geography Subject Overview]]
- [[cds/geography/question_db|Question Database]]
- [[cds/cds_overview|CDS Exam Master Dashboard]]
"""
    note_path = f"{notes_dir}/{ch_slug}.md"
    with open(note_path, "w") as f:
        f.write(note_md)
    print(f"Updated Master Note: {note_path}")

print("ALL 11 CHAPTER NOTES SUCCESSFULLY REBUILT PAGE-BY-PAGE!")
