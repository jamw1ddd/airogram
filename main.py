import fitz
import json

def extract_structure_from_pdf(pdf_path):
    # Открываем PDF-файл
    doc = fitz.open(pdf_path)
    
    # Извлекаем оглавление
    toc = doc.get_toc()

    # Создаем пустую структуру
    structure = {}

    # Функция для добавления уровней в структуру
    def add_to_structure(struct, level, title):
        if level == 1:
            struct[title] = {}
            return struct[title]
        elif level > 1:
            keys = list(struct.keys())
            if keys:
                return add_to_structure(struct[keys[-1]], level - 1, title)
        return struct

    # Обрабатываем оглавление
    for entry in toc:
        level, title, _ = entry
        add_to_structure(structure, level, title)

    return structure

# Укажите путь к вашему PDF-файлу
pdf_file = "test.pdf"
structure = extract_structure_from_pdf(pdf_file)

# Сохраняем структуру в JSON-файл
with open('structure.json', 'w', encoding='utf-8') as f:
    json.dump(structure, f, ensure_ascii=False, indent=4)

print("Структура успешно сохранена в файл structure.json.")
