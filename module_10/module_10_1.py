import time
def write_words(word_count, file_name):
    with open(file_name,'w',encoding='utf8') as file:
        for num in range(word_count):
            file.write(f'Какое-то слово № {num}\n')
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

start = time.time()
for word_count, file_num in [(10, 1), (30, 2), (200, 3), (100, 4)]:
    write_words(word_count,f'example{file_num}.txt')
end = time.time()
print(end-start)

from threading import Thread

start = time.time()
ts=[]
for word_count, file_num in [(10, 1), (30, 2), (200, 3), (100, 4)]:
    ts += [Thread(target=write_words, args = (word_count,f'example{file_num}.txt'))]

for t in ts:
    t.start()

for t in ts:
    t.join()
end = time.time()
print(end-start)
