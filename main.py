import fitz
import json

def extract_structure_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    toc = doc.get_toc()
    structure = {}

    def add_to_structure(struct, level, title):
        if level == 1:
            struct[title] = {}
            return struct[title]
        elif level > 1:
            keys = list(struct.keys())
            if keys:
                return add_to_structure(struct[keys[-1]], level - 1, title)
        return struct

    for entry in toc:
        level, title, _ = entry
        add_to_structure(structure, level, title)

    return structure

pdf_file = "test.pdf"
structure = extract_structure_from_pdf(pdf_file)

with open('structure.json', 'w', encoding='utf-8') as f:
    json.dump(structure, f, ensure_ascii=False, indent=4)

print("Структура успешно сохранена в файл structure.json.")
