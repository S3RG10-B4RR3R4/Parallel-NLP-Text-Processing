import os
import json
import multiprocessing as mp
from tqdm import tqdm
from utils import preprocess_text

def process_book(book_path):
    try:
        with open(book_path, 'r', encoding='utf-8') as f:
            text = f.read()
            tokens = preprocess_text(text)
            word_freq = {}
            for token in tokens:
                word_freq[token] = word_freq.get(token, 0) + 1
        return word_freq
    except Exception as e:
        print(f"Error processing {book_path}: {e}")
        return {}

def parallel_word_frequency(book_paths, num_processes=None):
    with mp.Pool(processes=num_processes) as pool:
        book_frequencies = list(tqdm(pool.imap(process_book, book_paths), total=len(book_paths), desc="Processing (parallel)"))

    word_freq = {}
    for book_freq in book_frequencies:
        for word, count in book_freq.items():
            word_freq[word] = word_freq.get(word, 0) + count

    # Guardar resultados en JSON
    with open("results/parallel_results.json", "w", encoding="utf-8") as f:
        json.dump(word_freq, f, indent=4)

    return word_freq
