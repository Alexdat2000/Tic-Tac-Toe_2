import random


def robot_step(field, comp_char):
    print("Computer's turn")
    while True:
        a = random.randint(0, 8)
        if field[a] == " ":
            field[a] = comp_char
            break
    return field


def player_step(field, fighter):
    while True:
        while True:
            try:
                pos_x, pos_y = map(int, input("Your turn\n").split(":"))
                break
            except ValueError:
                print("Please, input nums in format 1:1\n")
        if pos_x < 1 or pos_x > 3 or pos_y < 1 or pos_y > 3:
            print("Error\n")
        pos = (pos_y-1)*3 + pos_x-1
        if pos < 0 or pos > 8:
            print("Error\n")
        if field[pos] == " ":
            field[pos] = fighter
            break
        else:
            print("Error, this field is not empty, choose another\n")

    return field


def check_end(field):
    pos = "OK"
    a = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 5, 8], [2, 5, 6]]
    for i in a:
        if field[i[0]] == field[i[1]] == field[i[2]] != " ":
            pos = "END"
            break
    if " " not in field:
        pos = "DRAW"
    return pos


def game_help():
    # выводит помощь
    print("тут типа помощь")
