def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Checar linhas e colunas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Checar diagonais
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print("Bem-vindo ao Jogo da Velha!")
    print_board(board)

    for _ in range(9):
        row = int(input("Jogador {}: Escolha a linha (0, 1 ou 2): ".format(players[current_player])))
        col = int(input("Jogador {}: Escolha a coluna (0, 1 ou 2): ".format(players[current_player])))

        # Verificar se a posição está vazia
        if board[row][col] == " ":
            board[row][col] = players[current_player]
            print_board(board)

            # Verificar se alguém ganhou
            if _ >= 4:
                winner = check_winner(board)
                if winner:
                    print("Parabéns! Jogador {} venceu!".format(winner))
                    break

            current_player = (current_player + 1) % 2
        else:
            print("Essa posição já foi escolhida. Tente novamente.")

    else:
        print("Empate!")

    restart = input("Deseja jogar novamente? (s/n): ")
    if restart.lower() == 's':
        play_game()

if __name__ == "__main__":
    play_game()
