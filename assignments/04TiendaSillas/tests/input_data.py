# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["iii9", "F", "10"],
        ["Tipo de laptop i5, i7, i9: ",
         "Tipo de cliente F, R, N: ",
          "Cantidad de laptops: ",
        "Error en tipo de laptop"],
        '''Debe salir:
        Error en tipo de laptop
        '''
    ),
    (
        ["i9", "Tec", "10"],
        ["Tipo de laptop i5, i7, i9: ",
         "Tipo de cliente F, R, N: ",
          "Cantidad de laptops: ",
        "Error en tipo de cliente"],
        '''Debe salir:
        Error en tipo de cliente
        '''
    ),
    (
    ["i7", "R", "10"],
    ["Tipo de laptop i5, i7, i9: ",
     "Tipo de cliente F, R, N: ",
      "Cantidad de laptops: ",
    "Total sin dcto: 95,000",
    "Descuento: 23,750",
    "Total a pagar: 71,250"],
    '''Debe salir:
    Total sin dcto: 95,000
    Descuento: 23,750
    Total a pagar: 71,250
    '''
    ),
    (
    ["i7", "f", "10"],
    ["Tipo de laptop i5, i7, i9: ",
    "Tipo de cliente F, R, N: ",
    "Cantidad de laptops: ",
    "Total sin dcto: 95,000",
    "Descuento: 28,500",
    "Total a pagar: 66,500"],
    '''Debe salir:
    Total sin dcto: 95,000
    Descuento: 28,500
    Total a pagar: 66,500
    '''
    ),

    (
    ["i7", "n", "10"],
    ["Tipo de laptop i5, i7, i9: ",
    "Tipo de cliente F, R, N: ",
    "Cantidad de laptops: ",
    "Total sin dcto: 95,000",
    "Descuento: 9,500",
    "Total a pagar: 85,500"
    ],
    '''Debe salir:
    Total sin dcto: 95,000
    Descuento: 9,500
    Total a pagar: 85,500
    '''
    ),

    (
    ["i7", "R", "10"],
    ["Tipo de laptop i5, i7, i9: ",
    "Tipo de cliente F, R, N: ",
    "Cantidad de laptops: ",
    "Total sin dcto: 95,000",
    "Descuento: 23,750",
    "Total a pagar: 71,250"
    ],
    '''Debe salir:
    Total sin dcto: 95,000
    Descuento: 23,750
    Total a pagar: 71,250
    '''
    ),

    (
    ["i5", "f", "10"],
    ["Tipo de laptop i5, i7, i9: ",
    "Tipo de cliente F, R, N: ",
    "Cantidad de laptops: ",
    "Total sin dcto: 75,000",
    "Descuento: 22,500",
    "Total a pagar: 52,500"

    ],
    '''Debe salir:
    Total sin dcto: 75,000
    Descuento: 22,500
    Total a pagar: 52,500
    '''
    ),
    (
    ["i9", "f", "19"],
    ["Tipo de laptop i5, i7, i9: ",
    "Tipo de cliente F, R, N: ",
    "Cantidad de laptops: ",
    "Total sin dcto: 218,500",
    "Descuento: 65,550",
    "Total a pagar: 152,950"
    ],
    '''Debe salir:
    Total sin dcto: 218,500
    Descuento: 65,550
    Total a pagar: 152,950
    '''
    ),
    (
    ["i9", "n", "10"],
    ["Tipo de laptop i5, i7, i9: ",
    "Tipo de cliente F, R, N: ",
    "Cantidad de laptops: ",
    "Total sin dcto: 115,000",
    "Descuento: 11,500",
    "Total a pagar: 103,500"
    ],
    '''Debe salir:
    Total sin dcto: 115,000
    Descuento: 11,500
    Total a pagar: 103,500
    '''
    ),

    (
    ["i9", "r", "10"],
    ["Tipo de laptop i5, i7, i9: ",
    "Tipo de cliente F, R, N: ",
    "Cantidad de laptops: ",
    "Total sin dcto: 115,000",
    "Descuento: 28,750",
    "Total a pagar: 86,250"
    ],
    '''Debe salir:
    Total sin dcto: 115,000
    Descuento: 28,750
    Total a pagar: 86,250

    '''
    )

]
