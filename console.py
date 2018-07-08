import commands
import console_commands


def main():
    field = [' ']*9

    console_commands.start()
    player_char, robot_char = console_commands.fighter_choose()

    print("\n************************")
    print("** Let the game begin **")
    print("************************")

    if player_char == "x":
        field = commands.player_step(field, 'x')
        console_commands.printer(field)

    while True:
        field = commands.robot_step(field, robot_char)
        pos = commands.check_end(field)
        if pos == "END":
            print('Computer win')
            console_commands.printer(field)
            break
        elif pos == "DRAW":
            print("Draw")
            console_commands.printer(field)
            break

        console_commands.printer(field)

        field = commands.player_step(field, player_char)
        pos = commands.check_end(field)
        if pos == "END":
            print('You win')
            console_commands.printer(field)
            break
        elif pos == "DRAW":
            print("Draw")
            console_commands.printer(field)
            break
        console_commands.printer(field)

    print("Thanks for playing")


if __name__ == '__main__':
    main()
