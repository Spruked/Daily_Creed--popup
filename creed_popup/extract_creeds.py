from docx import Document
import json
import re

DOCX_NAME = "The_Creed_101_Final_With_Author 2025-06-04 16_20_49.docx"
OUT_JSON = "creeds.json"

def is_creed_start(line):
    return bool(re.match(r"^\d+\.\s", line.strip()))

def get_creed_number(line):
    match = re.match(r"^(\d+)\.\s", line.strip())
    return int(match.group(1)) if match else None

def main():
    doc = Document(DOCX_NAME)

    creeds = {}
    current_number = None
    buffer = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue

        if is_creed_start(text):
            # Save previous creed
            if current_number is not None:
                creeds[str(current_number)] = "\n".join(buffer).strip()
            # Start new creed
            current_number = get_creed_number(text)
            buffer = [text]
        else:
            if current_number is not None:
                buffer.append(text)

    # Save last one
    if current_number is not None:
        creeds[str(current_number)] = "\n".join(buffer).strip()

    print(f"Extracted {len(creeds)} creeds.")

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(creeds, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
