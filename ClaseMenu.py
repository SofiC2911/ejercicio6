# -*- coding: utf-8 -*-
from ClaseFechaHora import FechaHora

class Menu:
    __switcher = None
    
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.salir
                           }
        
    def getSwitcher(self):
        return self.__switcher
    
    def salir(self,r1,r2):
        print('Salir del menu')
        
    def opcion(self,op,r1,r2):
        if type(op) == int:
            func = self.__switcher.get(op, lambda: print("Opción no válida"))
            func(r1,r2)
        else:
            print('parametro incorrecto')
    
    def opcion1(self,r1,r2):     #sumar
        sumar = r1 + r2
        FechaHora.Mostrar(sumar)
        
        
    def opcion2(self,r1,r2):   #restar
        restar = r1 - r2
        FechaHora.Mostrar(restar)
    
    def opcion3(self,r1,r2):  #comparar mayor
        may = r1 > r2
        if may:
            print('La primer fecha es mayor')
        else:
            print('La primer fecha no es mayor')