from docx import Document

doc = Document("The_Creed_101_Final_With_Author 2025-06-04 16_20_49.docx")

for i, p in enumerate(doc.paragraphs):
    if p.text.strip():
        print(f"{i}: {repr(p.text)}")
