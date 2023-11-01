quantity_symbols_in_line = 25
quantity_lines_on_page = 50
quantity_pages_in_book = 100
volume_disk = 1.44
volume_symbol_in_bytes = 4

volume_disk_in_bytes = volume_disk * 1024 * 1024  # Переводим Мб в байты (1 Мб = 1024 Кб = 1024 * 1024 байт)
quantity_symbols_in_book = quantity_symbols_in_line * quantity_lines_on_page * quantity_pages_in_book  # Кол-во символов
# в книге
volume_book = quantity_symbols_in_book * volume_symbol_in_bytes  # размер книги в байтах

quantity_books_in_disk = volume_disk_in_bytes // volume_book

print("Количество книг, помещающихся на дискету:", int(quantity_books_in_disk))

