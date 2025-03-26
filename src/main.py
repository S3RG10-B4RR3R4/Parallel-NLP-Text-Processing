import time
import matplotlib.pyplot as plt
from utils import create_directories, download_gutenberg_texts
from serial_version import serial_word_frequency
from parallel_version import parallel_word_frequency

def benchmark_processing(book_paths, max_processes=None):
    if max_processes is None:
        import multiprocessing as mp
        max_processes = mp.cpu_count()

    # Procesamiento en serie
    print("\n🔄 Running Serial Processing...\n")
    start_serial = time.time()
    serial_freq = serial_word_frequency(book_paths)
    serial_time = time.time() - start_serial

    # Procesamiento en paralelo
    print("\n⚡ Running Parallel Processing...\n")
    process_times = []
    num_processes_list = list(range(1, max_processes + 1))

    for num_processes in num_processes_list:
        start_parallel = time.time()
        parallel_freq = parallel_word_frequency(book_paths, num_processes)
        parallel_time = time.time() - start_parallel
        process_times.append(parallel_time)

    # Generar y guardar gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(num_processes_list, process_times, marker='o', label="Parallel Processing")
    plt.axhline(y=serial_time, color='r', linestyle='--', label="Serial Time")
    plt.title('Parallel Processing: Execution Time vs Number of Processes')
    plt.xlabel('Number of Processes')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plots/benchmarking.png")
    print("\n📊 Plot saved to 'plots/benchmarking.png'")

    print(f"\n⏱️ Serial processing time: {serial_time:.4f} seconds")
    print(f"⚡ Fastest parallel processing time: {min(process_times):.4f} seconds")

if __name__ == "__main__":
    create_directories()
    
    # 🔽 Cambiar el número de libros aquí 🔽
    book_paths = download_gutenberg_texts(num_books=5)  # Cambiar este número para descargar más libros
    
    benchmark_processing(book_paths)
