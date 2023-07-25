def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner(board, row, col):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for dr, dc in directions:
        count = 1
        for i in range(1, 5):
            r, c = row + i * dr, col + i * dc
            if 0 <= r < 15 and 0 <= c < 15 and board[r][c] == board[row][col]:
                count += 1
            else:
                break

        for i in range(1, 5):
            r, c = row - i * dr, col - 5 * dc
            if 0 <= r < 15 and 0 <= c < 15 and board[r][c] == board[row][col]:
                count += 1
            else:
                break

        if count >= 5:
            return True

    return False

def play_game():
    board = [["." for _ in range(15)] for _ in range(15)]
    player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        print(f"Player {player}, it's your turn.")
        row = int(input("Enter row (0-14): "))
        col = int(input("Enter column (0-14): "))

        if board[row][col] == ".":
            board[row][col] = player
            if check_winner(board, row, col):
                print_board(board)
                print(f"Player {player} wins!")
                game_over = True
            else:
                player = "X" if player == "O" else "O"
        else:
            print("That position is already taken. Try again.")

play_game()
