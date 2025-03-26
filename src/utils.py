import os
import string
import requests
import json
from tqdm import tqdm
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Descargar recursos de NLTK si no están disponibles
import nltk
nltk_dependencies = ['punkt', 'stopwords']
for resource in nltk_dependencies:
    try:
        nltk.data.find(f'tokenizers/{resource}' if 'punkt' in resource else f'corpora/{resource}')
    except LookupError:
        nltk.download(resource)

# Asegurarse de que la salida de la consola esté en UTF-8
import sys
sys.stdout.reconfigure(encoding="utf-8")

# Crear directorios si no existen
def create_directories():
    for directory in ["data", "plots", "results"]:
        os.makedirs(directory, exist_ok=True)

# Descargar libros de Gutenberg
def download_gutenberg_texts(num_books=50):
    base_url = "https://www.gutenberg.org/files/{id}/{id}-0.txt"
    books_directory = "data"
    os.makedirs(books_directory, exist_ok=True)

    downloaded_books = []
    book_id = 100
    attempts = 0
    max_attempts = num_books * 6

    print(f"\nDownloading {num_books} books...\n")
    with tqdm(total=num_books, desc="Downloading books") as pbar:
        while len(downloaded_books) < num_books and attempts < max_attempts:
            url = base_url.format(id=book_id)
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200 and len(response.text) > 10000:
                    filename = os.path.join(books_directory, f"{book_id}.txt")
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(response.text)
                    downloaded_books.append(filename)
                    pbar.update(1)
            except:
                pass
            book_id += 1
            attempts += 1

    print(f"\n[✔] Books downloaded: {len(downloaded_books)}\n")  # Cambié el símbolo para que sea seguro en todas las consolas
    return downloaded_books

# Preprocesar texto
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    return [word for word in tokens if word.isalpha() and word not in stop_words]
