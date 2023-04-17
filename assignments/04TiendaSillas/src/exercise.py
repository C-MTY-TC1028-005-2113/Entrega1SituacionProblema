# Nombre -
# Matricula -
# Carrera -
figura = "?"
def leer_cartas_jugador(nombre, tablero):
    pass

def  despliega_tablero(opcion, matriz, r1 = None, c1 = None, r2 = None, c2 = None):
    pass

def son_pares(opcion, tablero, escondidas, r1, c1, r2, c2):
    pass

def main() :
    # 1º Leer los datos de entrada
    caso = int(input())
    if caso == 1:
        pares_jugador1 = 0
        escondidas = [['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q'], ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q']]
        tablero = [['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]
        r1,c1,r2,c2 = leer_cartas_jugador("Jugador1", tablero);
        pares_jugador1 += son_pares(1,tablero, escondidas,r1,c1,r2,c2)
        print("Pares Jugador1:",pares_jugador1)
    elif caso == 2:
        pares_jugador1 = 0
        escondidas = [['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q'], ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q']]
        tablero = [['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]
        r1,c1,r2,c2 = leer_cartas_jugador("Jugador1", tablero);
        pares_jugador1 += son_pares(1,tablero, escondidas,r1,c1,r2,c2)
        print(pares_jugador1)



if __name__=='__main__':
    main()
