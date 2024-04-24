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

def ai_move1(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if board[row][col] == " ":
            board[row][col] = 'X'
            print("O computador1 escolheu a posição: ({}, {})".format(row, col))
            break

def ai_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if board[row][col] == " ":
            board[row][col] = 'O'
            print("O computador2 escolheu a posição: ({}, {})".format(row, col))
            break

def choose_starting_player():
    return random.choice(['player1', 'AI'])

def play_game():
    global player1_wins, player2_wins, draws, total_games
    board = [[" " for _ in range(3)] for _ in range(3)]
    starting_player = choose_starting_player()

    print("Bem-vindo ao Jogo da Velha!")
    print("O jogador {} começa.".format(starting_player))

    print_board(board)

    for _ in range(9):
        if starting_player == 'player':
            ai_move1(board)
        else:
            ai_move(board)

        print_board(board)

        if _ >= 4:
            winner = check_winner(board)
            if winner:
                if winner == 'X':
                    player1_wins += 1
                else:
                    player2_wins += 1
                return

        starting_player = 'AI' if starting_player == 'player' else 'player'

    draws += 1

def main():
    global player1_wins, player2_wins, draws, total_games
    player1_wins = 0
    player2_wins = 0
    draws = 0

    while True:
        try:
            num_games = int(input("Quantos jogos você gostaria de jogar? "))
            break
        except ValueError:
            print("Por favor, insira um número válido.")

    for game in range(1, num_games + 1):
        print("\nJogo", game)
        play_game()

    total_games = player1_wins + player2_wins + draws
    print("\nResultado final:")
    print("Vitórias do Jogador 1:", player1_wins)
    print("Vitórias do Jogador 2:", player2_wins)
    print("Empates:", draws)
    print("Total de partidas jogadas:", total_games)

    print("Obrigado por jogar!")

if __name__ == "__main__":
    main()
