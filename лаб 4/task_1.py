# TODO решите задачу
import json

FILENAME = "input.json"

def task() -> float:
    #открываем файл в режиме чтения
    with open(FILENAME, 'r') as file:
        #Десериализация данных из файла
        data = json.load(file)
        #создание списка из произведений двух значений в каждом словаре с помощью лист компрехейшен
        total_ = [dict_['score'] * dict_['weight'] for dict_ in data]
        #возвращение суммы значений спискаокругленного до 3 знаков после запятой
        return f"{sum(total_):.3f}"

print(task())
