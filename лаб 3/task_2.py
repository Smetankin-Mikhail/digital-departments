# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, splitter=","):
    # узнаем запятая ли используется в качестве разделителя
    for i in range(len(first_group)):
        if first_group[i] != ",": # Если разделитель не запятая,
            first_group_up = first_group.upper() # то возведим строку в верхний регист
            for k in range(1,len(first_group)): # и найдим позицию первого пересечения, отличного от первой буквы списка
                if first_group_up[k]==first_group[k]:
                    splitter = first_group[k-1] # поскольку обращение к элементу с 0 то k-1
    split_first_group = first_group.split(splitter) # разделение первого списока
    split_second_group = second_group.split(splitter) # разделение первого списока

    common_participants = list(set(split_first_group).intersection(split_second_group)) # поиск пересечения

    alphabet_list = sorted(common_participants) # алфавитный порядок
    #result_list = splitter.join(alphabet_list)
    return (alphabet_list)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group)) # Вызов функции


# TODO Провеьте работу функции с разделителем отличным от запятой
