# Параметры книги
pages = 100           # количество страниц
lines_per_page = 50   # число строк на странице
chars_per_line = 25   # количество символов в строке
bytes_per_char = 4    # байты для хранения одного символа

# объем одной книги в байтах
book_size_bytes = pages * lines_per_page * chars_per_line * bytes_per_char

disk_size_mb = 1.44
disk_size_bytes = disk_size_mb * 1024 * 1024  # в байты

# количество книг, которые можно поместить на дискету
number_of_books = int(disk_size_bytes // book_size_bytes)

print("Количество книг, помещающихся на дискету:", number_of_books)

