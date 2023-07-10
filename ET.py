import os
os.system("cls")



ListaEntrada=[]
UbicacionD = range(1,101)
UbicacionV=[]

escenario="""
Entradas Disponibles

1  2  3  4  5  6  7  8  9  10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
31 32 33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48 49 50                        
51 52 53 54 55 56 57 58 59 60
61 62 63 64 65 66 67 68 69 70 
71 72 73 74 75 76 77 78 79 80
81 82 83 84 85 86 87 88 89 90
91 92 93 94 95 96 97 98 99 100

"""


precioEntrada="""
Los precios de las entradas son las siguientes

* Platinum, $120.000. (Asientos del 1 al 20)
* Gold, $80.000. (Asientos del 21 al 50)
* Silver, $50.000. (Asientos del 51 al 100).



"""

ub1=[]


menu ="""----------------------------------
    1. Comprar Entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir
-----------------------------------------
Seleccione Opcion:

"""
nom= input("Ingrese su nombre: ")
ape= input("Ingrese su Apellido: ")





opc= int(input(menu))
while True:
    try:
        entrada= int(input("Ingrese cantidad de entradas: "))
        for i in range (1,101):
            print(i)
            if i in UbicacionD:
                print(f"Asiento {i}: Disponible")
            elif i in UbicacionD:
                print(f"Asiento {i}: Vendido")    
        if entrada <=3 and entrada >=1:
            for i in range (entrada):
                ub1= int(input("Seleccione una ubicacion disponible: "))
                
            break
        else:
            print("La cantidad ingresada no es valida")   
                 
        
      
    except:
        print("Ocurrio una excepcion, Intente nuevamente")     



while True:
    try:
        opc =int(input(menu))
        if opc ==5:
            print(f"""Adios {nom} {ape}""")
            break
    except:
        print("Ocurrio una excepcion, Intente nuevamente")     
        
        


while True:
    try:
        opc =int(input(menu))
        if opc == 2:

    except:
        print("Ocurrio una excepcion, Intente nuevamente")   