import os
import time

# Директория для обхода
directory = "."

for root, dirs, files in os.walk(directory):  # Использование os.walk для обхода каталога
    for file in files:
        filepath = os.path.join(root, file)  # Примените os.path.join для формирования полного пути к файлам

        filetime = os.path.getmtime(filepath)  # Получение времени последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        filesize = os.path.getsize(filepath)  # Использование os.path.getsize для получения размера файла

        parent_dir = os.path.dirname(filepath)  # Использование os.path.dirname для получения родительской директории файла

        # Вывод информации о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
