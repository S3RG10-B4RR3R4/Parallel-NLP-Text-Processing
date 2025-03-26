import os
import json
from tqdm import tqdm
from utils import preprocess_text

def serial_word_frequency(book_paths):
    all_frequencies = {}

    for book_path in tqdm(book_paths, desc="Processing (serial)"):
        try:
            with open(book_path, 'r', encoding='utf-8') as f:
                text = f.read()
                tokens = preprocess_text(text)
                freq = {}
                for token in tokens:
                    freq[token] = freq.get(token, 0) + 1
                book_name = os.path.basename(book_path)
                all_frequencies[book_name] = freq
        except Exception as e:
            print(f"Error processing {book_path}: {e}")

    # Guardar resultados en JSON
    with open("results/serial_results.json", "w", encoding="utf-8") as f:
        json.dump(all_frequencies, f, indent=4)

    return all_frequencies
