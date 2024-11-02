import threading
from time import sleep, time

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Измерение времени выполнения
start = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end = time()
print(f"Время выполнения для последовательных вызовов: {end - start} сек.")

# Создание потоков
threads = []
files = [('example5.txt', 10), ('example6.txt', 30),
         ('example7.txt', 200), ('example8.txt', 100)]

start_threads = time()
for file_name, count in files:
    thread = threading.Thread(target=write_words, args=(count, file_name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_threads = time()
print(f"Время выполнения для потоков: {end_threads - start_threads} сек.")
