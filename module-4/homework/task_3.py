def print_board(board):
    print("\n" + "-" * 35)
    for row in board:
        print("|", end="")
        for cell in row:
            print(f"{cell:2d} |", end="")
        print("\n" + "-" * 35)

def is_valid(x, y, board):
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] == 0

def solve_knight_tour(board, x, y, move_count):
    if move_count == 64:
        return True
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    for dx, dy in moves:
        next_x = x + dx
        next_y = y + dy
        if is_valid(next_x, next_y, board):
            board[next_x][next_y] = move_count + 1
            if solve_knight_tour(board, next_x, next_y, move_count + 1):
                return True
            board[next_x][next_y] = 0
    return False

def main():
    board = [[0 for _ in range(8)] for _ in range(8)]
    try:
        x = int(input("Введите номер строки (0–7): "))
        y = int(input("Введите номер столбца (0–7): "))
        if not (0 <= x < 8 and 0 <= y < 8):
            print("Ошибка: координаты должны быть от 0 до 7.")
            return
    except ValueError:
        print("Ошибка: введите целые числа.")
        return
    board[x][y] = 1
    if solve_knight_tour(board, x, y, 1):
        print("Путь найден!")
        print_board(board)
    else:
        print("Путь не найден.")

main()