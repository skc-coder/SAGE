import json, os, re

with open("/tmp/physical_geography_gemini_full.json") as f:
    pages = json.load(f)

print(f"Loaded {len(pages)} transcribed pages from Gemini Vision!")

# Define target output directories in Obsidian vault
vault_base = "/home/skc/dev/SAGE/content/cds/geography"
notes_dir = f"{vault_base}/notes"
questions_dir = f"{notes_dir}/questions"
variations_dir = f"{notes_dir}/variations"

os.makedirs(questions_dir, exist_ok=True)
os.makedirs(variations_dir, exist_ok=True)

# Organize transcribed pages into chapters
chapters = [
    {
        "slug": "universe",
        "title": "Universe and Solar System",
        "pages": range(1, 17),
        "difficulty": "Hard"
    },
    {
        "slug": "latitudes-longitudes",
        "title": "Latitudes, Longitudes and Time Systems",
        "pages": range(17, 56),
        "difficulty": "Medium"
    },
    {
        "slug": "geomorphology",
        "title": "Geomorphology and Earth Interior",
        "pages": range(56, 78),
        "difficulty": "Hard"
    },
    {
        "slug": "plate-tectonics",
        "title": "Plate Tectonics, Mountains and Volcanism",
        "pages": range(78, 95),
        "difficulty": "Hard"
    },
    {
        "slug": "rocks-minerals",
        "title": "Rocks, Minerals and Rock Cycle",
        "pages": range(95, 104),
        "difficulty": "Medium"
    },
    {
        "slug": "landforms",
        "title": "Geomorphic Processes and Landforms",
        "pages": range(104, 147),
        "difficulty": "Hard"
    },
    {
        "slug": "atmosphere-ozone",
        "title": "Atmosphere, Ozone Layer and Greenhouse Effect",
        "pages": range(147, 163),
        "difficulty": "Medium"
    },
    {
        "slug": "winds-cyclones",
        "title": "Pressure Belts, Local Winds and Cyclones",
        "pages": range(163, 185),
        "difficulty": "Hard"
    },
    {
        "slug": "clouds-rainfall",
        "title": "Condensation, Clouds and World Rainfall",
        "pages": range(185, 205),
        "difficulty": "Medium"
    },
    {
        "slug": "koeppen-climate",
        "title": "Koeppen Climate Classification and Indian Climate",
        "pages": range(205, 229),
        "difficulty": "Hard"
    },
    {
        "slug": "oceanography",
        "title": "Oceanography, Ocean Currents and Coral Reefs",
        "pages": range(229, 252),
        "difficulty": "Hard"
    }
]

page_dict = {p["page"]: p.get("content", "") for p in pages}

print("Building Obsidian Vault Notes...")

for ch in chapters:
    ch_slug = ch["slug"]
    ch_title = ch["title"]
    ch_pages = ch["pages"]
    
    # Collect text content for this chapter
    content_blocks = []
    for p_num in ch_pages:
        txt = page_dict.get(p_num, "")
        if txt.strip():
            content_blocks.append(f"### Page {p_num} Notes & Transcripts\n\n{txt.strip()}")
            
    full_chapter_text = "\n\n---\n\n".join(content_blocks)
    
    # Write Chapter Topic Note
    note_content = f"""---
exam: "CDS"
subject: "Physical Geography"
topic: "{ch_title}"
difficulty: "{ch['difficulty']}"
tags: [cds, geography, physical-geography, {ch_slug}, topic]
---

# {ch_title}

Comprehensive, exhaustive notes and transcriptions covering **{ch_title}** from the Physical Geography Master Class.

---

## Theory, Intuition & Key Concepts

{full_chapter_text}

---

## Navigation

- [[cds/geography/geography_overview|Physical Geography Subject Dashboard]]
- [[cds/cds_overview|CDS Exam Master Dashboard]]
"""
    note_path = f"{notes_dir}/{ch_slug}.md"
    with open(note_path, "w") as f:
        f.write(note_content)
    print(f"Created Topic Note: {note_path}")

print("Vault Note Generation Finished!")
