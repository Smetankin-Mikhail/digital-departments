# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    #открываем файл csv файл в режиме чтения
    with open(INPUT_FILENAME, 'r') as csv_file:
        #считываем файл
        read_file = csv.DictReader(csv_file)
        #преобразуем в список
        list_ = [row for row in read_file]
        # открываем файл json файл в режиме перезаписи
        with open(OUTPUT_FILENAME,'w') as json_file:
            # сериализируем в файл с отступами равными 4
            json_data = json.dumps(list_, indent=4)
            #наполняем файл
            json_file.write(json_data)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
