list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

quantity_plaers_in_team = len(list_players) // 2  # Кол-во игроков в команде

team_1 = list_players[:quantity_plaers_in_team]  # Игроки в команде 1
team_2 = list_players[quantity_plaers_in_team:]  # Игроки в команде 2

print(team_1)
print(team_2)
