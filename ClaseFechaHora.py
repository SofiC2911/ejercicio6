class FechaHora:
    __dia = 0
    __mes = 0
    __año = 0
    __hora = 0
    __minuto = 0
    __segundo = 0
    
    def __init__(self,d,m,a,h,minu,seg):
        self.__dia = d
        self.__mes = m
        self.__año = a
        self.__hora = h
        self.__minuto = minu
        self.__segundo = seg
    
    def Mostrar(self):
        print('%.2d/%.2d/%.2d\t -\t %.2d:%.2d:%.2d' % (self.__dia, self.__mes, self.__año, self.__hora, self.__minuto, self.__segundo))
        self.Validar(self.__dia, self.__mes, self.__año, self.__hora, self.__minuto, self.__segundo)

    def Validar(self, dia, mm, aa, hs, mi, seg):
        bandera = False
        if hs in range (0, 24) and type(hs) == int:
            if mi in range (0, 60) and type(mi) == int:
                if seg in range (0, 60) and type(seg) == int:
                    if mm in [1, 3, 5, 7, 8, 10, 12]:
                        if dia in range (1, 32) and type(dia) == int:
                            bandera = True
                    elif mm in [4, 6, 9, 11]:
                        if dia in range (1, 31) and type(dia) == int:
                            bandera = True
                    elif mm == 2:
                        if (self.Bisiesto(aa)):
                            if dia in range (1, 30) and type(dia) == int:
                                bandera = True
                        else: 
                            if dia in range (1, 29) and type(dia) == int:
                                bandera = True
        if bandera:
            print('\nFecha y Hora ingresada es valida\n')
        else:
            print('\nFecha Y hora incorrectas\n')
                        
    def Bisiesto(self, aa):
        bisiesto = False
        if aa % 4 == 0 and (aa % 100 != 0 or aa % 400 == 0):
            bisiesto = True
        return bisiesto
    
    def getDia(self):
        return self.__dia
    
    def getMes(self):
        return self.__mes
    
    def getAño(self):
        return self.__año
    
    def getHora(self):
        return self.__hora
    
    def getMinu(self):
        return self.__minuto
    
    def getSeg(self):
        return self.__segundo
    
    def __add__(self,r2):
        return FechaHora(self.__dia + r2.getDia(), self.__mes + r2.getMes(), 
                         self.__año + r2.getAño(), self.__hora + r2.getHora(), 
                         self.__minuto + r2.getMinu(), self.__segundo + r2.getSeg())
    
    def __sub__(self,r2):
        return FechaHora(self.__dia - r2.getDia(), self.__mes - r2.getMes(), 
                         self.__año - r2.getAño(), self.__hora - r2.getHora(), 
                         self.__minuto - r2.getMinu(), self.__segundo - r2.getSeg())
    
    def __gt__(self, fechahora):
        bool = False
        if self.__año > fechahora.getAño():
            bool = True
        elif self.__año < fechahora.getAño():
            pass
        elif self.__mes > fechahora.getMes():
            bool = True
        elif self.__mes < fechahora.getMes():
            pass
        elif self.__dia > fechahora.getDia():
            bool = True
        elif self.__dia < fechahora.getDia():
            pass
        elif self.__hora > fechahora.getHora():
            bool = True
        elif self.__hora < fechahora.getHora():
            pass
        elif self.__minuto > fechahora.getMin():
            bool = True
        elif self.__minuto < fechahora.getMin():
            pass
        elif self.__segundo > fechahora.getSeg():
            bool = True
        elif self.__segundo < fechahora.getSeg():
            pass
        return bool
