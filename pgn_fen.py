###Fer
# pgn
def quitar(pgn, caracter1, caracter2):
    '''para quitatr parentesis'''
    paren = ''
    aux = False
    for i in pgn:
        if i == caracter1:
            aux = True
        if aux:
            paren += i
        if i == caracter2:
            aux = False
            pgn = pgn.replace(paren, '')
            paren = ''
    return pgn

def traduce_replace(f):
    '''Traduce de sp a uk'''
    # '♟♜♞♝♛♚' #
    f = f.replace('R', 'K')
    f = f.replace('T', 'R')
    f = f.replace('C', 'N')
    f = f.replace('A', 'B')
    f = f.replace('D', 'Q')
    f = f.replace('OOO', 'O-O-O')
    f = f.replace('OO', 'O-O')

    return f

############################
def movi_a_lista(idioma,movimientos_fen) -> list | None:
    '''mete los movimientos en una lista'''
    if idioma == 'uk':
        planilla1=[]
        busca = r'[RNBQK]?[a-h]?[1-8]?x?[a-h][1-8]=?[RNBQ]?|O-O-O|O-O'
        planilla1 = re.findall(busca, movimientos_fen)
        return planilla1
    ############################


    if idioma == 'sp':
    # mete los movimientos en una lista
        busca = r'[TCADR]?[a-h]?[1-8]?x?[a-h][1-8]=?[TCAQ]?|O-O-O|O-O|OOO|OO'
        planilla1 = re.findall(busca, movimientos_fen)
        
    
        planilla2=[]
        
        
        for movimiento in planilla1:
            planilla2.append(traduce_replace(movimiento))
            
        print('planilla2',planilla2)
        
        
        return planilla2
    ############################
############################
# diccionario obtenido
# partida = {'inicio': 'rnbqkbnr/pppppppp/8/8/8/PPPPPPPP/RNBQKBNR'
###########################

###########################
# crea un diccionario
# clave el movimiento
# valor la  FEN de movimiento


def diccionario_de_movimientos(movimientos_pgn):
    '''Crea un diccionario con la clave jugada y el valor fen'''
    jugada_fen = {}
    ##########################
    tablero = chess.Board()

    # Lista de movimientos como str
    jugadas = movi_a_lista('sp', movimientos_pgn)
    index_jugadas= list(enumerate(jugadas,1))
    print(f'{index_jugadas=}')
    #dict
    jugada_fen = {(0,'inicial'): tablero.fen()}
    
    planilla = ['inicial']
    for media_jugada in index_jugadas:
    # Introduce las jugadas
    # en el modulo
        tablero.push_san(media_jugada[1]) # Para pasarle solo el movimiento
    
# Hay que hacer una copia
# Para hacer una lista de tableros
# aux = posi.copy()
# tablero.append(aux)

# Rellena el diccionario
# Con la jugada y el fen
        jugada_fen[media_jugada] = tablero.fen()

        
        planilla.append(media_jugada[1])
    print(f'{planilla=}')
    return jugada_fen, planilla


def tabla_de_tableros(jugada_fen, planilla) -> dict:
    '''Crea un diccionario con la clave jugada y valor una tabla con las posiciones'''
    jugada_fotograma = {}
    for media_jugada in enumerate(planilla): # un movimiento
        posicion = []
        # ['rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1']
        fen = jugada_fen[media_jugada].split(' ')
        # ['r1b1kbnr', 'ppppqppp', '2n5', '4P3', '8', '5N2', 'PPP1PPPP', 'RNBQKB1R']
        fen = fen[0].split('/') # una lista de filas
        for fila_fen in fen:
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
            posicion.append(fila_tablero)          
        # inicial : [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        #            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        #            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        #            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        jugada_fotograma[media_jugada]= posicion

    return jugada_fotograma

###################################################################


if __name__ == '__main__':
    import re
    import chess
    from partidas import PGN
#########################
    '''
    print(dir(str))
    PGN = quitar(PGN, '(', ')')
    PGN = quitar(PGN, '{', '}')

    print(PGN)
    '''
    posicion_fen, movimientos = diccionario_de_movimientos(PGN)
    print(posicion_fen)
    posicion_fotograma = tabla_de_tableros(posicion_fen, movimientos)
    for  jugada in enumerate(movimientos):
        print(jugada)
        for fotograma in posicion_fotograma[jugada]:
            print(fotograma)
######################################################################
