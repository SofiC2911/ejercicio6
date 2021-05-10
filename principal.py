# -*- coding: utf-8 -*-
from ClaseFechaHora import FechaHora
from ClaseMenu import Menu

if __name__ == '__main__':
    r1 = FechaHora(1,1,2020,00,00,00)
    r2= FechaHora(1,1,2021,00,00,00)

    r1.Mostrar()

    r2.Mostrar()
    
    menu = Menu()
    
    salir = False
    while not salir:
        print("\n-----------------Menu--------------------")
        print(" 1 - Sumar ")
        print(" 2 - Restar ")
        print(" 3 - Comparar ")
        print(" 4 - Salir ")
        op = int(input(' Ingrese una opcion: '))
        menu.opcion(op,r1,r2)
        if op == 4:
            salir = True