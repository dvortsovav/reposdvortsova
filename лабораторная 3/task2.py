def find_common_participants(group1, group2, delimiter=','):

    # разделяем строки на списки участников
    group1_participants = group1.split(delimiter)
    group2_participants = group2.split(delimiter)

    # находим пересечение множеств участников
    common_participants = list(set(group1_participants).intersection(group2_participants))

    # сортируем список общих участников в алфавитном порядке
    common_participants.sort()

    # возвращаем список общих участников
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
participants_intersection = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(participants_intersection)
