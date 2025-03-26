# Book Analysis Project

## Overview

This project allows you to download public domain books from [Project Gutenberg](https://www.gutenberg.org/), preprocess their text, perform text analysis, and generate benchmarking plots. It organizes all the downloaded books, processed data, and analysis results into separate directories.

The project uses Python and several libraries, including `requests` for downloading the books, `nltk` for text processing, and `tqdm` for progress bars during the download and processing phases.

### Project Structure

The project is organized as follows:

```
/book-analysis/
│
├── src/
│   ├── serial_version.py      # Serial version of text processing
│   ├── parallel_version.py    # Parallel version of text processing
│   └── utils.py               # Utility functions (downloading, preprocessing, etc.)
│
├── data/                      # Datasets (books downloaded from Gutenberg)
├── plots/                     # Benchmarking plots generated during the analysis
├── results/                   # Processed results (text analysis results)
├── requirements.txt           # Required dependencies for the project
└── README.md                  # This file
```

## Requirements

This project requires several Python libraries. To install all the required dependencies, use the following command:

```bash
pip install -r requirements.txt
```

### Required Libraries:
- `requests`: For downloading books from Project Gutenberg.
- `nltk`: For text processing tasks (tokenization, stopwords removal).
- `tqdm`: For displaying download and processing progress bars.

## Installation Instructions

### Clone the Repository:

Clone the repository to your local machine with the following command:

```bash
git clone https://github.com/your-username/book-analysis.git
cd book-analysis
```

### Install Dependencies:
Use the requirements.txt file to install the necessary Python libraries:

```bash
pip install -r requirements.txt
```

### Run the Program:
Execute the main.py script to begin the process. This will:
- Download books from Gutenberg
- Preprocess the downloaded text
- Analyze the text
- Generate plots and save them

```bash
python src/main.py
```

## Usage

### How to Download Books

The program allows you to download a configurable number of books from Project Gutenberg. By default, it downloads 5 books (for testing purposes). You can change this number in the main.py file by modifying the `num_books` parameter:

```python
book_paths = download_gutenberg_texts(num_books=5)  # Change this number to download more books
```

Examples:
- To download 10 books:
  ```python
  book_paths = download_gutenberg_texts(num_books=10)
  ```
- To download 50 books:
  ```python
  book_paths = download_gutenberg_texts(num_books=50)
  ```

## Expected Output

Once the books are downloaded, you will see a progress bar indicating the download status. The books will be saved in the `data/` directory with filenames based on their Gutenberg IDs.

The program will also preprocess the books by:
- Converting the text to lowercase.
- Removing punctuation.
- Tokenizing the text into words.
- Removing common stopwords (e.g., "the", "and", "is").

The processed results, such as word frequencies or text analysis data, will be saved in the `results/` directory in JSON format.

Benchmarking plots for the analysis will be generated and stored in the `plots/` directory.

## Running the Code

After modifying the number of books in `main.py` (if desired), you can run the script with:

```bash
python src/main.py
```

### Expected Directory Structure After Running the Script

```
/book-analysis/
│
├── data/      # Contains the downloaded books
│   └── 100.txt
│   └── 101.txt
│   └── ...
│
├── results/   # Contains the processed analysis results (JSON files)
│   └── analysis_results.json
│
├── plots/     # Contains the benchmarking plots (images)
│   └── plot1.png
│   └── plot2.png
│
└── src/       # Contains Python source code
│   └── main.py
│   └── utils.py
│   └── serial_version.py
│   └── parallel_version.py
```

## Explanation of Code

### 1. utils.py

This file contains utility functions for downloading books, preprocessing text, and managing directories.

#### `download_gutenberg_texts()`
This function downloads books from Project Gutenberg. It takes a `num_books` argument, which specifies how many books to download. The books are saved in the `data/` directory.

Breakdown of the function:
- It starts by iterating over book IDs, beginning with 100.
- It attempts to download each book in .txt format from the Gutenberg website.
- If the book is successfully downloaded (with a valid response and sufficient content), it is saved to the `data/` directory.
- The progress of the download is displayed using a progress bar (tqdm).

Example of how to change the number of books:
```python
book_paths = download_gutenberg_texts(num_books=5)  # Change this to download more books
```

#### `preprocess_text()`
This function preprocesses the text of the downloaded books:
- Converts the text to lowercase.
- Removes punctuation.
- Tokenizes the text into individual words.
- Removes stopwords (commonly used words like "the", "and", "is" which don't add meaningful content to the analysis).

### 2. serial_version.py and parallel_version.py

These files implement two different versions of text processing:
- `serial_version.py`: Processes the text one book at a time in a sequential manner.
- `parallel_version.py`: Uses parallel processing to handle multiple books simultaneously, improving performance when dealing with a large number of books.

Both files are designed to analyze the content of the books and generate results such as word frequency counts.

### 3. main.py

This is the entry point of the project. It:
- Calls `download_gutenberg_texts()` to download the specified number of books.
- Uses the `serial_version.py` or `parallel_version.py` (depending on which one you choose to run) to process the downloaded books.
- Saves the results in the `results/` directory and generates benchmarking plots in the `plots/` directory.

#### Key Code Section for Modifying the Number of Books to Download

In the `main.py` file, the number of books to download is controlled by the `num_books` argument:

```python
book_paths = download_gutenberg_texts(num_books=5)  # Change this number to download more books
```

You can change the 5 to any number to download more or fewer books from Gutenberg. For example, setting it to 50 will download 50 books:

```python
book_paths = download_gutenberg_texts(num_books=50)
```

### 4. requirements.txt

This file lists the Python dependencies required to run the project. To install these dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Contributions

Contributions are welcome! If you have any improvements, fixes, or new features you'd like to add, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your changes:
   ```bash
   git checkout -b new-feature
   ```
4. Make your changes and commit them:
   ```bash
   git commit -am 'Add new feature'
   ```
5. Push your changes to your forked repository:
   ```bash
   git push origin new-feature
   ```
6. Open a pull request from your fork to the original repository.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

Thank you for using this project! If you have any questions, suggestions, or issues, feel free to open an issue or contact the author.
