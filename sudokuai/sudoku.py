import pygame
import random

def create_board():
    # 9x9'lik boş bir tahta oluşturun
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Tahtayı rastgele sayılarla doldurun
    for i in range(9):
        for j in range(9):
            num = random.randint(1, 9)
            # Sayının geçerli olup olmadığını kontrol edin
            if is_valid(board, i, j, num):
                board[i][j] = num

    return board

def is_valid(board, row, col, num):
    # Aynı satırda veya sütunda aynı sayıdan var mı kontrol edin
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # 3x3'lük blokta aynı sayıdan var mı kontrol edin
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def print_board(board):
    for row in board:
        print(row)

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0

    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def draw_board(screen, board):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)
    for i in range(9):
        for j in range(9):
            cell_value = str(board[i][j]) if board[i][j] != 0 else ""
            color = BLACK if board[i][j] != 0 else (255, 0, 0)  # Yeni eklenen renk kontrolü
            text_surface = font.render(cell_value, True, color)
            screen.blit(text_surface, (65 + 45 * j, 65 + 45 * i))

    for i in range(10):
        if i % 3 == 0: