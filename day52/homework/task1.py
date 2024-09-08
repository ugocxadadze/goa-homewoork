def print_board(board):
    """გამოიტანს თამაშის დაფას."""
    print("\n")
    print("  |  |  ")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("  |  |  ")
    print("---------")
    print("  |  |  ")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("  |  |  ")
    print("---------")
    print("  |  |  ")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("  |  |  ")
    print("\n")

def check_winner(board):
    """ამოწმებს, არსებობს თუ არა გამარჯვებული დაფაზე."""
    win_conditions = [
        (0, 1, 2),  # პირველი რიგი
        (3, 4, 5),  # მეორე რიგი
        (6, 7, 8),  # მესამე რიგი
        (0, 3, 6),  # პირველი სვეტური
        (1, 4, 7),  # მეორე სვეტური
        (2, 5, 8),  # მესამე სვეტური
        (0, 4, 8),  # დიაგონალი მარჯვნიდან მარცხნივ
        (2, 4, 6)   # დიაგონალი მარცხნიდან მარჯვნივ
    ]


def is_board_full(board):
    """ამოწმებს, არის თუ არა დაფა სავსე."""
    return " " not in board

def play_game():
    """ტემპერირებული თამაში."""
    board = [" "  in range(9)]  # შექმნის ცარიელ დაფას
    currentplayer = "X"  # დაწყების მოთამაშე
    winner = None

    while winner is None and not (board):
        (board)
        print(f"{current_player}'s turn")

        try:
            move = int(input("შეიყვანეთ თქვენი ნაბიჯი (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("არასწორი ნაბიჯი, სცადეთ კიდევ.")
                continue
        except ValueError:
            print("გთხოვთ, შეიყვანოთ ვალიდური რიცხვი.")
            continue

        board[move] = current_player
        winner = check_winner(board)

        if winner is None:
            current_player = "O" if current_player == "X" else "X"

    print_board(board)

    if winner:
        print(f"{winner} მოიგო!")
    else:
        print("ტაი!")
    play_game()