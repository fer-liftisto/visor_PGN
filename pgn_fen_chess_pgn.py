import chess.pgn


def tabla_de_tableros(posicion):

    # un movimiento
    fotograma = []

    # ['rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1']
    FEN = posicion.split(' ')

    # ['r1b1kbnr', 'ppppqppp', '2n5', '4P3', '8', '5N2', 'PPP1PPPP', 'RNBQKB1R']
    FEN = FEN[0].split('/')  # una lista de filas

    for fila_fen in FEN:

        fila_tablero = []
        for casilla in fila_fen:

            if casilla.isnumeric():
                con = int(casilla)
                while con > 0:
                    fila_tablero.append(' ')
                    con -= 1
            elif casilla.isalpha():
                fila_tablero.append(casilla)

            # [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            #  ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            #  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            #  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            #  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            #  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            #  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            #  ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        fotograma.append(fila_tablero)
        
    return fotograma



with open('lichess_pgn_2024.10.30_LIFTISTO_vs_israel_ima.6sfvWFd7 (1).pgn','r') as pgn:

    first_game = chess.pgn.read_game(pgn)


# Iterate through all moves and play them on a board.
board = first_game.board()
for move in first_game.mainline_moves():
    board.push(move)
    posicion=board.fen()
    print(board)
    print(posicion)
    tablero=tabla_de_tableros(posicion)
    for jugada in tablero:
        print(jugada)
        
    input()
