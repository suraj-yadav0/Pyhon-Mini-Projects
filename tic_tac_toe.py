def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def is_valid_move(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    return board[row][col] == " "


def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print("Enter row (0-2) and column (0-2) separated by space")

    while True:
        print("\nCurrent board:")
        print_board(board)

        player = players[current_player]
        print(f"\nPlayer {player}'s turn")

        while True:
            try:
                row, col = map(int, input("Enter row and column: ").split())
                if is_valid_move(board, row, col):
                    break
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Invalid input! Enter two numbers separated by space.")

        board[row][col] = player

        if check_winner(board, player):
            print("\nFinal board:")
            print_board(board)
            print(f"\nPlayer {player} wins!")
            break

        if is_board_full(board):
            print("\nFinal board:")
            print_board(board)
            print("\nIt's a tie!")
            break

        current_player = (current_player + 1) % 2


if __name__ == "__main__":
    play_tic_tac_toe()