# Nombre -
# Matricula -
# Carrera -
figura = "?"
def leer_cartas_jugador(nombre, tablero):
    # desplegar el nombre del jugador recibido en el parámetro nombre
    # leer la carta1 r1, c1  " r1":, "c1:"
    # validar que la carta este en el rango 0..5 y que esa carta no  este visible
    # leer la carta2 r2, c2  " r2":, "c2:"
    # validar que la carta este en el rango 0..5 y que esa carta no  este visible
    # y que sea diferente de la carta1
    pass

def  despliega_tablero(opcion, matriz, r1 = None, c1 = None, r2 = None, c2 = None):
    pass

def son_pares(opcion, tablero, escondidas, r1, c1, r2, c2):
    # destapar las cartas en el tablero
    # desplegar_tablero resaltando las cartas seleccionadas
    # verificar si son pares
    # si si son pares asignar a la variable puntos = 1
    #     desplegar "Par"
    # si no son pares asignar a  puntos = 0
    #     desplegar "Impar"
    #     volver a tapar las cartas en el tablero
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
    elif caso == 3:
        pares_jugador1 = 5
        escondidas = [['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q'], ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q']]
        tablero = [['a', 'b', '?', '?', '?', 'f'], ['g', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', 'b', '?', '?', '?', 'f'], ['g', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]
        r1,c1,r2,c2 = leer_cartas_jugador("Jugador23", tablero);
        pares_jugador1 += son_pares(1,tablero, escondidas,r1,c1,r2,c2)
        print("Pares Jugador23:",pares_jugador1)



if __name__=='__main__':
    main()
