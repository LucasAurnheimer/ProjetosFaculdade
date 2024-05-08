import random

def print_board(board):
    # Esta função imprime o tabuleiro na tela.
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Esta função verifica se há um vencedor no tabuleiro.
    # Verifica linhas, colunas e diagonais.
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

def is_board_full(board):
    # Esta função verifica se o tabuleiro está cheio (empate).
    for row in board:
        if " " in row:
            return False
    return True

def choose_starting_player():
    # Esta função sorteia aleatoriamente qual jogador começa o jogo.
    return random.choice(['X', 'O'])

def random_move(board, player):
    # Esta função faz uma jogada aleatória no tabuleiro.
    if player == 'O':
        # Se o jogador aleatório começar, o jogador experiente joga no meio, se estiver vazio
        if board[1][1] == " ":
            board[1][1] = player
            return

    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = player
            return

def ai_move(board, player):
    # Esta função faz a jogada do computador baseada em uma estratégia refinada.

    if player == 'X':
        # Estratégia refinada
        # Verifica se o oponente está prestes a vencer
        opponent = 'O'
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = opponent
                    if check_winner(board) == opponent:
                        board[i][j] = player
                        return
                    else:
                        board[i][j] = " "
        # Se o oponente não está prestes a vencer, aplica a estratégia normal
        # Prioriza vitórias imediatas
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    if check_winner(board) == player:
                        return
                    else:
                        board[i][j] = " "

        # Bloqueia vitórias do oponente
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = opponent
                    if check_winner(board) == opponent:
                        board[i][j] = player
                        return
                    else:
                        board[i][j] = " "

        # Ocupa os cantos e centro
        moves = [(0, 0), (0, 2), (2, 0), (2, 2)]

        for move in moves:
            if board[move[0]][move[1]] == " ":
                board[move[0]][move[1]] = player
                return

        # Se não houver posições centrais, cantos ou vitórias imediatas/bloqueios, escolhe uma posição aleatória
        random_move(board, player)
    else:
        # Jogada aleatória
        random_move(board, player)

def play_game(num_games):
    # Esta função inicia o jogo da velha.

    player_wins = 0
    ai_wins = 0
    ties = 0

    for game in range(1, num_games + 1):
        print("Jogo #{}".format(game))
        board = [[" " for _ in range(3)] for _ in range(3)]  # Inicializa o tabuleiro.
        starting_player = choose_starting_player()  # Escolhe aleatoriamente quem começa.

        print("Jogador inicial: {}".format(starting_player))

        for move in range(1, 10):
            print("Rodada #{}".format(move))
            print_board(board)
            if starting_player == 'X':
                ai_move(board, 'X')
            else:
                ai_move(board, 'O')

            winner = check_winner(board)  # Verifica se há um vencedor.
            if winner:
                print("Jogador {} venceu!".format(winner))
                if winner == 'X':
                    player_wins += 1
                else:
                    ai_wins += 1
                break
            elif is_board_full(board):
                print("Empate!")
                ties += 1
                break

            starting_player = 'O' if starting_player == 'X' else 'X'  # Alterna os jogadores.
        
        print("Final do Jogo #{}:".format(game))
        print_board(board)
        print()

    print("\nResultado final:")
    print("Vitórias do Jogador 1:", player_wins)
    print("Vitórias do Jogador 2:", ai_wins)
    print("Empates:", ties)
    print("Total de partidas jogadas:", num_games)

if __name__ == "__main__":
    num_games = int(input("Quantos jogos você gostaria de jogar entre os dois computadores? "))
    play_game(num_games)  # Inicia o jogo.
