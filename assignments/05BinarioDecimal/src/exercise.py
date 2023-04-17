# Nombre:
# Matricula:
# Carrera:
# Fecha:

"""
Diseña y códifica un programa en Python que haga lo siguiente: 

Datos de Entrada:
El programa ya tiene 2 matrices con la información de las Series de una plataforma y otra con contiene información de alumnos.
- cada renglón de cada  matriz se organiza de la siguiente forma
       Nombre ,            clase,    código,      País,  duracion_min,        fecha,     calificación
['I Am Not an Animal', 'Animation',   '11.164',     'GB',      '349',         '10/05/04',          '9.5']
['Benito',                'LAE',       'A0000',     'MX',     '349',         '10/05/04',          '100']

la matriz podría tener cualquier otra información - no siempre tendra la misma,
solo por cuestiones de tiempo se tienen 2 opciones - debes programar tu solución para que
funcione para cualquier otro contenido de la matriz no únicamente para los actuales,
de lo contrario TU SOLUCIÓN NO TENDRÁ SE TOMARA EN CUENTA (0 PTOS.).

Salidas:
El programa debe desplegar un listado como se muestra a continuación, con una numeración de 1 hasta n(la cantidad de renglones de la matriz)
el programa debe tener la programación para calcular lo siguiente usando los datos de la matriz 
       - NOTA IMPORTANTE - debes diseñar tu solución para que funcione para cualquier otro contenido de la matriz 
         no únicamente para el actual, de lo contrario TU SOLUCIÓN NO SE TOMARÁ EN CUENTA(0 PTOS).
    - Contar y desplegar la cantidad de series o alumnos que existen para cada clase (TIP - contar la cantidad total de la misma clase, usa listas)
    - Contar y desplegar la cantidad total de elementos de la matriz.  
    - Calcular y desplegar el promedio de todas calificaciones
       (TIP - usa un acumulador - inicializar antes del ciclo e incrementar al ir recorriendo la matriz)
    - Calcular y desplegar el promedio de todas las duraciones.

La salida debería ser para el caso 1 :
1 I Am Not an Animal
2 Chernobyl
3 Rick and Morty
4 Breaking Bad
5 Hunter x Hunter
6 Sherlock
7 Planet Earth II
8 Peaky Blinders
9 Stranger Things
10 DEATH NOTE
11 Avatar: The Last Airbender
12 The Twilight Zone
13 The Wire
14 Gravity Falls
15 The Sopranos
16 Neon Genesis Evangelion
17 The Marvelous Mrs. Maisel
18 Young Justice
19 Band of Brothers
20 Futurama
Animation 9
Drama 6
Crime 3
Documentary 1
Comedy 1
Total: 20
Calificacion Promedio: 8.38
Tiempo Promedio: 893.2

Si No Funciona en GitHub -10 ptos.
"""
def main():

       
    series = [['I Am Not an Animal', 'Animation', '11.164', 'GB', '349', '10/05/04', '9.5'],
    ['Chernobyl', 'Drama', '46.429', 'US', '595', '06/05/19', '8.6'],
    ['Rick and Morty', 'Animation', '132.429', 'US', '1395', '02/12/13', '8.5'],
    ['Breaking Bad', 'Drama', '161.35', 'US', '3560', '20/01/08', '8.4'],
    ['Hunter x Hunter', 'Animation', '136.761', 'JP', '152', '02/10/11', '8.3'],
    ['Sherlock', 'Crime', '35.74', 'GB', '1885', '25/07/10', '8.3'],
    ['Planet Earth II', 'Documentary', '17.744', 'GB', '348', '06/11/16', '8.3'],
    ['Peaky Blinders', 'Crime', '59.824', 'GB', '572', '12/09/13', '8.3'],
    ['Stranger Things', 'Drama', '81.441', 'US', '2671', '15/07/16', '8.3'],
    ['DEATH NOTE', 'Animation', '56.677', 'JP', '599', '04/10/06', '8.3'],
    ['Avatar: The Last Airbender', 'Animation', '15.668', 'US', '552', '21/02/05', '8.3'],
    ['The Twilight Zone', 'Drama', '12.384', 'US', '295', '02/10/59', '8.3'],
    ['The Wire', 'Crime', '30.153', 'US', '869', '02/06/02', '8.3'],
    ['Gravity Falls', 'Animation', '40.365', 'US', '298', '15/06/12', '8.3'],
    ['The Sopranos', 'Drama', '25.922', 'US', '846', '10/01/99', '8.3'],
    ['Neon Genesis Evangelion', 'Animation', '29.844', 'JP', '233', '04/10/95', '8.3'],
    ['The Marvelous Mrs. Maisel', 'Comedy', '23.354', 'US', '105', '16/03/17', '8.3'],
    ['Young Justice', 'Animation', '30.096', 'US', '121', '26/11/10', '8.3'],
    ['Band of Brothers', 'Drama', '19.555', 'GB', '1500', '09/09/01', '8.2'],
    ['Futurama', 'Animation', '40.574', 'US', '919', '28/03/99', '8.2']]
    
    alumnos =  [['Josu', 'ITC', 'AL345', 'MX', '300', '10/05/04', '99'],
    ['Cristian', 'INE', 'AL456', 'US', '500', '06/05/19', '88'],
    ['Ricky', 'IFI', 'AL456', 'MX', '1200', '02/12/13', '45'],
    ['Beatriz', 'IRS', 'AL100', 'US', '5600', '20/01/08', '100'],
    ['Hugo', 'IFI', 'AL890', 'MX', '5000', '02/10/11', '100'],
    ['Silvia', 'ITC', 'AL888', 'MX', '4000', '25/07/10', '90'],
    ['Pedro', 'ITC', 'AL999', 'MX', '1000', '06/11/16', '99']
                ]
      
    # leer la opcion
    opcion = int(input())

    if opcion == 1 :
        matriz = series.copy()
    else:
        matriz = alumnos.copy( )
    
    # Añade aquí tu programación con comentarios y estandar de codificación


    print("Total de series:", total)
    print("Calificacion Promedio:", round(promedio, 2))
    print("Tiempo Promedio:", round(promedio, 2))

if __name__=='__main__':
    main()
