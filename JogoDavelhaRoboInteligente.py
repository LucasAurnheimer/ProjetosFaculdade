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

def player_move(board):
    # Esta função permite que o jogador humano faça sua jogada.
    while True:
        row = int(input("Escolha a linha (0, 1 ou 2): "))
        col = int(input("Escolha a coluna (0, 1 ou 2): "))

        if board[row][col] == " ":
            board[row][col] = 'X'
            break
        else:
            print("Essa posição já foi escolhida. Tente novamente.")

def ai_move(board):
    # Esta função faz a jogada do computador utilizando o algoritmo Minimax.
    best_score = float('-inf')  # Melhor pontuação inicial como negativo infinito.
    best_move = None  # Melhor jogada inicial como nula.

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'O'  # Faz a jogada.
                score = minimax(board, False)  # Chama o algoritmo Minimax.
                board[i][j] = " "  # Desfaz a jogada.

                # Atualiza a melhor jogada e a melhor pontuação.
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    # Realiza a melhor jogada no tabuleiro.
    board[best_move[0]][best_move[1]] = 'O'
    print("O computador escolheu a posição: ({}, {})".format(best_move[0], best_move[1]))

def minimax(board, is_maximizing):
    # Esta função implementa o algoritmo Minimax para avaliar as jogadas.

    winner = check_winner(board)  # Verifica se há um vencedor.
    if winner == 'X':  # Se o jogador humano vence, retorna -1.
        return -1
    elif winner == 'O':  # Se o computador vence, retorna 1.
        return 1
    elif is_board_full(board):  # Se o tabuleiro estiver cheio (empate), retorna 0.
        return 0

    if is_maximizing:
        # Se estiver maximizando (vez do computador), explora todas as possíveis jogadas do computador.
        best_score = float('-inf')  # Melhor pontuação inicial como negativo infinito.
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'O'  # Faz a jogada.
                    score = minimax(board, False)  # Chama o Minimax recursivamente.
                    board[i][j] = " "  # Desfaz a jogada.

                    # Atualiza a melhor pontuação.
                    best_score = max(score, best_score)
        return best_score
    else:
        # Se estiver minimizando (vez do jogador humano), explora todas as possíveis jogadas do jogador humano.
        best_score = float('inf')  # Melhor pontuação inicial como positivo infinito.
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'X'  # Faz a jogada.
                    score = minimax(board, True)  # Chama o Minimax recursivamente.
                    board[i][j] = " "  # Desfaz a jogada.

                    # Atualiza a melhor pontuação.
                    best_score = min(score, best_score)
        return best_score

def choose_starting_player():
    # Esta função sorteia aleatoriamente qual jogador começa o jogo.
    return random.choice(['player', 'AI'])

def play_game():
    # Esta função inicia o jogo da velha.

    board = [[" " for _ in range(3)] for _ in range(3)]  # Inicializa o tabuleiro.
    starting_player = choose_starting_player()  # Escolhe aleatoriamente quem começa.

    print("Bem-vindo ao Jogo da Velha!")
    print("O jogador {} começa.".format(starting_player))

    print_board(board)  # Imprime o tabuleiro inicial.

    for _ in range(9):
        if starting_player == 'player':
            player_move(board)  # Jogada do jogador humano.
        else:
            ai_move(board)  # Jogada do computador.

        print_board(board)  # Imprime o tabuleiro após a jogada.

        winner = check_winner(board)  # Verifica se há um vencedor.
        if winner:
            print("Parabéns! Jogador {} venceu!".format(winner))
            play_again()  # Pergunta se deseja jogar novamente.
            return

        if is_board_full(board):  # Verifica se o tabuleiro está cheio (empate).
            print("Empate!")
            play_again()  # Pergunta se deseja jogar novamente.
            return

        starting_player = 'AI' if starting_player == 'player' else 'player'  # Alterna os jogadores.

def play_again():
    # Esta função pergunta se deseja jogar novamente e reinicia o jogo se sim.
    restart = input("Deseja jogar novamente? (s/n): ")
    if restart.lower() == 's':
        play_game()
    else:
        print("Obrigado por jogar!")  # Mensagem de encerramento.

if __name__ == "__main__":
    play_game()  # Inicia o jogo.
