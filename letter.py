import tkinter as tk
from tkinter import filedialog
import string
from docx import Document
import os

def analyze_file_characters(file_path):
    try:
        file_extension = os.path.splitext(file_path)[1].lower()
        text = ""
        if file_extension == '.txt':
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        elif file_extension == '.docx':
            doc = Document(file_path)
            for paragraph in doc.paragraphs:
                text += paragraph.text + '\n'
        else:
            print(f"Error: Unsupported file format:{file_extension}")
            return None
        counts = {
            'cyrillic': 0,
            'latin': 0,
            'digits': 0,
            'whitespace': 0,
            'special_chars': 0,
            'total_chars': len(text)
        }
        cyrillic_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        latin_chars = string.ascii_letters
        digits_chars = string.digits
        whitespace_chars = string.whitespace

        for char in text:
            if char in cyrillic_chars:
                counts['cyrillic'] += 1
            elif char in latin_chars:
                counts['latin'] += 1
            elif char in digits_chars:
                counts['digits'] += 1
            elif char in whitespace_chars:
                counts['whitespace'] += 1
            else:
                counts['special_chars'] += 1
        
        return counts
    except FileNotFoundError:
        print(f"Error: file in '{file_path}' wasn`t found" )
        return None
    except Exception as e:
        print(f"Error like {e}")
        return None
def select_file_and_analyze():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select .txt file or docx",
        filetypes=[
            ("Txt and Word files","*.txt *.docx"),
            ("Txt files","*.txt"),
            ("Documend Word", "*.docx"),
            ("All files","*.*")
            ]
    )
    if file_path:
        print(f"Selected file:{file_path}")
        print("Start analyzing...")
        results = analyze_file_characters(file_path)
        if results:
                print("\n--- Результаты анализа ---")
                print(f"Общее количество символов: {results['total_chars']}")
                print(f"Кириллица: {results['cyrillic']}")
                print(f"Латиница: {results['latin']}")
                print(f"Цифры: {results['digits']}")
                print(f"Пробелы: {results['whitespace']}")
                print(f"Спецсимволы: {results['special_chars']}")
                print("-------------------------")
    else:
        print("Выбор файла отменен.")   

if __name__ =="__main__":
    select_file_and_analyze()

