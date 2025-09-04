import matplotlib.pyplot as plt

def draw_board(board):
    _, ax = plt.subplots()
    # Draw grid
    for i in range(4):
        ax.plot([0, 3], [i, i], color='black')
        ax.plot([i, i], [0, 3], color='black')
    # Draw X and O
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                ax.text(j + 0.5, 2.5 - i, "X", fontsize=36, ha='center', va='center', color='red')
            elif board[i][j] == "O":
                ax.text(j + 0.5, 2.5 - i, "O", fontsize=36, ha='center', va='center', color='blue')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    plt.show()

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("Instructions:")
    print("Enter row and column numbers between 1 and 3 to place your mark.")
    print("Rows and columns are numbered from 1 (top/left) to 3 (bottom/right).")
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        draw_board(board)
        print(f"Player {current_player}'s turn.")
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter col (1-3): ")) - 1
            if row not in range(3) or col not in range(3):
                print("Row and column must be between 1 and 3. Try again.")
                continue
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers only. Try again.")
            continue
        board[row][col] = current_player
        if check_winner(board, current_player):
            draw_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_full(board):
            draw_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()