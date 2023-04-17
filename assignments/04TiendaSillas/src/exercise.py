# Nombre - 
# Matricula - 
# Carrera -

"""
En una tienda de laptops se venden de 3 tipos: corei5, corei7, corei9
La tienda además tiene clasificados a sus  clientes en las siguientes categorias: frecuentes, registrados y nuevos

Ya pronto se acerca la venta del Buen Fin, por lo tanto El director de la tienda a decidido dar los siguientes
descuentos dependiendo del cliente:

Clientes frecuentes(F o f):
- se les dará un descuento del 30%  por cualquier monto de compra

Clientes registrados(R o r):
- si su compra es superior a $20,000  e inferior a $30,000 un 15% de descuento
- si su compra es superior $30,000 un 25% de descuento

Clientes nuevos(N o n):
- se les dará un 10% de descuento por cualquier monto de compra

Lleva a cabo el análisis, diseño y codificación en python de un programa
que lea la categoria de la laptop (que puede ser i5, i7, i9 que puede ser ingresada cómo Mayúscula o minúscula),
el tipo de cliente (que es una letra f,r,n que puede ser ingresada cómo Mayúscula o minúscula)
y la cantidad a comprar (que es un número entero).
Para esta versión que vas a diseñar solo se le permite al cliente realizar una comprar de un solo tipo de laptop.

El programa debe tener las siguientes funciones:
Función llamada total_antes_descuento que recibe como parámetros: tipo_laptop y la cantidad: 
        La función retorna el total incial, antes del descuento.
Función llamada calcula_descuento que recibe como parámetros: el total inicial y el tipo_cliente: 
         La función retorna el monto del descuento.

Si No Funciona en GitHub -10 ptos.

Casos de prueba:

Tipo de laptop i5, i7, i9: iii9
Tipo de cliente F, R, N: F
Cantidad de laptops: 10
Error en tipo de laptop

Tipo de laptop i5, i7, i9: i9
Tipo de cliente F, R, N: Tec
Cantidad de laptops: 10
Error en tipo de cliente

Tipo de laptop i5, i7, i9: i7
Tipo de cliente F, R, N: R
Cantidad de laptops: 10
Total sin dcto: 95,000
Descuento: 23,750
Total a pagar: 71,250

Tipo de laptop i5, i7, i9: i7
Tipo de cliente F, R, N: f
Cantidad de laptops: 10
Total sin dcto: 95,000
Descuento: 28,500
Total a pagar: 66,500

"""
# Inicia el programa
def total_antes_descuento(tipo_laptop, cantidad):
    """Los precios de las laptops  son:
corei5 $7_500.00 c/u
corei7 $9_500.00 c/u
corei9 $11_500.00 c/u
 3 tipos: i5, i7, i9 Nota - podría ingresar también como I5, I7, I9
 """
    pass


def calcula_descuento(total_inicial, tipo_cliente):
    """Clientes frecuentes(F o f):
- se les dará un descuento del 30%  por cualquier monto de compra

Clientes registrados(R o r):
- si su compra es superior a $20,000  e inferior a $30,000 un 15% de descuento
- si su compra es superior  o igual a $30,000 un 25% de descuento

Clientes nuevos(N o n):
- se les dará un 10% de descuento por cualquier monto de compra
"""
    pass


def main() :
    # 1º Leer los datos de entrada
    laptops = input("Tipo de laptop i5, i7, i9: ")
    cliente = input("Tipo de cliente F, R, N: ")
    cantidad = int( input("Cantidad de laptops: "))





if __name__=='__main__':
    main()
