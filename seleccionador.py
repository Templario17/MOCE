#!/usr/bin/env python
#*-* coding: utf-8 -*-


INFANTERIA = {
    '10A':"INFANTERIA LIVINA", '10A1A':"UNIDADES CONVENCIONALES", '10A1B':"OPERACION EN SELVA",
    '10A1C':"OPERACIONES EN MONTAÑA", '10A1D':"OPERACIONES URBANAS", '10A1E':"OPERACIONES AEROTRASPORTADA",
    '10A1F':"VEHICULOS LIVIANOS INFANTERIA", '10A1G':"ARMAMENTO MEDIANO Y PEASADO",
    '10A1H':"SISTEMAS ANTITANQUE",'10B1I':"VEHICULOS LIVIANOS INF",
    '10B1J':"SISTEMA DE ARMAS LIVIANOS",'10B1K':"MANTENIMIENTO DE ARMAS",
    '10B1L':"OPERACIONES CON ARMAS COMBINADAS", '10C1M':"VEHICULOS PESADOS INFATERIA",
    '10C1N':"SISTEMAS DE ARMAS PESADAS", '10C1Ñ':"MANTENIMIENTO ARMAS PESADAS",
    '10C1O':"SISTEMAS DE COMUNCACIONES VEHICULOS PESADOS"
}

ARMA = {
    '12':"ARTILLERIA", '10':"INFANTERIA", '11':"CABALERIA"
}


moce = "O310A1BF0000"

msj = "Su Perfil aplica segun codigo MOCE :"

def seleccionador(moce):
        MOCE = moce[2:4]
        A = moce[2:5]
        B = moce[2:7]
        AR = str(ARMA[MOCE])
        arma = AR

        print "ARMA : {}".format(AR)
        print AR[B]


#        print "SUB ESPECIALIDAD {}".format(str(AR[B]))

        if moce[7] != "F":
            print "{} REGULARES".format(msj)
            print moce[7]
        else:
            print "{} PROCEDIMIENTO COMANDO".format(msj)


seleccionador(moce)
