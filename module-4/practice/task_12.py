# крестики-нолики
import random

board = [" " for _ in range(9)]
wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f"-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_wins(s):
    for a,b,c in wins:
        if board[a] == board[b] == board[c] == s:
            return True
    return False
    
def is_draw():
    return " " not in board

def computer_move():
    empty_ceils = [i for i in range(9) if board[i] == " "]
    if not empty_ceils:
        return
    move = random.choice(empty_ceils)
    board[move] = "o" 
    
def tic_tac_toe(): 
    while True:
        print_board()
        move = int(input("Ход(0-9): "))
        if move<0 or move>8 or board[move] != " ":
            print("Неверный ход.")
            continue
        board[move] = "x"
        if check_wins("x"):
            print_board()
            print("Победа")
            break
        if is_draw():
            print_board()
            print("Ничья")
            break
        computer_move()
        if check_wins("o"):
            print_board()
            print("Проигрыш")
            break
        if is_draw():
            print_board()
            print("Ничья")
            break

tic_tac_toe()