import os
import time
import sys

def create_game_board():
    return [" " for x in range(9)]

# VARIABLES
game_running = True
player1_name = None
player2_name = None
board = create_game_board()


# BEFORE THE GAME STARTS
player1_name = input("Spieler 1, gib deinen Namen ein: ") or "Spieler 1"
player2_name = input("Spieler 2, gib deinen Namen ein: ") or "Spieler 2"


# FUNCTIONS
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def print_board():
#    print(board[0] + " | " + board[1] + " | " + board[2])
#    print(board[3] + " | " + board[4] + " | " + board[5])
#    print(board[6] + " | " + board[7] + " | " + board[8])

    print(" " + "╔═══╦═══╦═══╗")
    print(" " + "║ " + board[0] + " ║ " + board[1] + " ║ " + board[2] + " ║")
    print(" " + "╠═══╬═══╬═══╣")
    print(" " + "║ " + board[3] + " ║ " + board[4] + " ║ " + board[5] + " ║")
    print(" " + "╠═══╬═══╬═══╣")
    print(" " + "║ " + board[6] + " ║ " + board[7] + " ║ " + board[8] + " ║")
    print(" " + "╚═══╩═══╩═══╝")
    print()

def check_move(cell):
    # Die Prüfung in dieser Funktion könnte man folgendermaßen abkürzen:
    #   return board[cell] == " "
    # Deine Variante ist aber natürlich auch richtig.

    if board[cell] == " ":
        return True
    else:
        return False

def do_move(player, cell):
    board[cell] = player

def check_win(player):
    # Diese Herangehensweise finde ich sehr gut! In meinem Programm ist die Berechnung weitaus komplexer,
    # aber das muss sie gar nicht sein! Das schöne an dieser Variante hier ist,
    # dass man die Logik sehr gut lesen und verstehen kann.
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True

    # Vereinfachen könntest du diese Prüfungen folgendermaßen:
    # -> siehe Funktion "check_combination"
    # return (check_combination(0, 1, 2, player) or
    #     check_combination(3, 4, 5, player) or
    #     check_combination(6, 7, 8, player) or
    #     check_combination(0, 3, 6, player) or
    #     check_combination(1, 4, 7, player) or
    #     check_combination(2, 5, 8, player) or
    #     check_combination(0, 4, 8, player) or
    #     check_combination(2, 4, 6, player))

def check_combination(value1, value2, value3, player):
    return board[value1] == player and board[value2] == player and board[value3] == player

# GAME LOOP
while game_running:
    player1_move_valid = False
    player2_move_valid = False

    while not player1_move_valid:
        clear()
        print_board()
        player1_move = int(input(player1_name + ", du bist am Zug. Gib ein Feld ein [1-9]: "))
        if player1_move > 0 and player1_move < 10:
            check1 = check_move((player1_move - 1))
            if check1:
                do_move("X", (player1_move - 1))
                player1_move_valid = True
            else:
              print("Keine gültige Eingabe!")
              time.sleep(1)
        else:
            print("Keine gültige Eingabe!")
            time.sleep(1)
    player1_check = check_win("X")
    if player1_check:
        clear()
        print_board()
        print(player1_name + " hat gewonnen!")
        player1_move_valid = True
        player2_move_valid = True
        game_running = False

    while not player2_move_valid:
        clear()
        print_board()
        player2_move = int(input(player2_name + ", du bist am Zug. Gib ein Feld ein [1-9]: "))
        if player2_move > 0 and player2_move < 10:
            check2 = check_move((player2_move - 1))
            if check2:
                do_move("O", (player2_move - 1))
                player2_move_valid = True
            else:
                 print("Keine gültige Eingabe!")
                 time.sleep(1)
        else:
            print("Keine gültige Eingabe!")
            time.sleep(1)
    player2_check = check_win("O")
    if player2_check:
        clear()
        print_board()
        print(player2_name + " hat gewonnen!")
        player1_move_valid = True
        player2_move_valid = True
        game_running = False

    # Wenn einer der beiden Spieler gewonnen hat, wird gefragt, ob die Runde neu gestartet werden soll.
    # Im Grunde wird hier deine Logik aus der zweiten Schleife ("while not game_running") verwendet.
    # Die Prüfung hättest du also einfach nur in der Haupt-Schleife ("while game_running") machen müssen.
    # Wie ich sagte: Es war nur eine Kleinigkeit ;-)
    if player1_check or player2_check:
        # Speichern der Eingabe auf die Variable "answer":
        #   • Sofern nichts eingegeben wurde, wird automatisch "y" gespeichert (Ausdruck: or "y")
        #   • Die Eingabe wird automatisch in Kleinbuchstaben umgewandelt (dadurch kann man anschließend leichter prüfen)
        answer = (input("Nochmal spielen? [Y/n]: ") or "y").lower()
        if answer == "y":
            board = create_game_board()
            game_running = True


# while not game_running:
#     answer = input("Nochmal spielen? [Y/n]: ")
#     if answer == "" or answer == "y" or answer == "Y":
#         board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
#         game_running = True
#     else:
#         sys.exit(0)
