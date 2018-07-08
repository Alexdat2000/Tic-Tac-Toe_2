import commands


def start():
    print("Welcome to Tic-Tac-Toe")
    print("Made by _Alexdat2000_")
    while True:
        a = input("If you need help type /help, else type /start\n")
        if a == "/help":
            commands.game_help()
            break
        elif a == "/start":
            break
        else:
            print("Unknown command")


def printer(field):
    print("·············")
    print(f"· {field[0]} · {field[1]} · {field[2]} ·")
    print("·············")
    print(f"· {field[3]} · {field[4]} · {field[5]} ·")
    print("·············")
    print(f"· {field[6]} · {field[7]} · {field[8]} ·")
    print("·············")


def fighter_choose():
    while True:
        player_char = input("Choose your fighter (X/O) (X are first)\n")
        if player_char == "X" or player_char == "x":
            player_char = "x"
            break
        elif player_char == "O" or player_char == "o" or player_char == "0":
            player_char == "o"
            break
        else:
            print("Unknown command")
    if player_char == 'x':
        robot_char = 'o'
    else:
        robot_char = 'x'

    return [player_char, robot_char]

