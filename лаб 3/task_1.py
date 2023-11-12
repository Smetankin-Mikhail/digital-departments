# TODO Напишите функцию для поиска индекса товара
def search_pos(items, find): # Функция для поиска индекса товара
    for i in range(len(items)): # Ищем сходство в каждом товаре
        if find == items[i]:
            pos = i
            break # Остановка поиска позиции после первого сходства
        else: pos = None # Если позиция не найдена, то None
    return pos

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан'] # Исходный список товаров

for find_item in ['банан', 'груша', 'персик']: # Товары, которые необходимо найти
    index_item = search_pos(items_list, find_item) # Позиция товаров, которые необходимо найти
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
