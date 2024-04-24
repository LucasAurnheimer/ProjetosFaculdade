import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def player_move(board):
    while True:
        row = int(input("Escolha a linha (0, 1 ou 2): "))
        col = int(input("Escolha a coluna (0, 1 ou 2): "))

        if board[row][col] == " ":
            board[row][col] = 'X'
            break
        else:
            print("Essa posição já foi escolhida. Tente novamente.")

def ai_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if board[row][col] == " ":
            board[row][col] = 'O'
            print("O computador escolheu a posição: ({}, {})".format(row, col))
            break

def choose_starting_player():
    return random.choice(['player', 'AI'])

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    starting_player = choose_starting_player()

    print("Bem-vindo ao Jogo da Velha!")
    print("O jogador {} começa.".format(starting_player))

    print_board(board)

    for _ in range(9):
        if starting_player == 'player':
            player_move(board)
        else:
            ai_move(board)

        print_board(board)

        if _ >= 4:
            winner = check_winner(board)
            if winner:
                print("Parabéns! Jogador {} venceu!".format(winner))
                play_again()
                return

        starting_player = 'AI' if starting_player == 'player' else 'player'

    print("Empate!")
    play_again()

def play_again():
    restart = input("Deseja jogar novamente? (s/n): ")
    if restart.lower() == 's':
        play_game()
    else:
        print("Obrigado por jogar!")

if __name__ == "__main__":
    play_game()