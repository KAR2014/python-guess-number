# -*- coding: utf-8 -*-
"""#Numero Aleatorio"""
import random
import time

ALEATORIO = random.randint(1, 20)
SALIDA = 0
print u"                              ***** Cognits *****"
print U"\n                       **** Adivinado Full Pro 2.0 © ****"
JUGADOR = raw_input("Ingresa tu Nombre: ")
print u"""\n¡BIENVENIDO! """+ JUGADOR +u"""
INSTRUCCIONES: El reto del juego es adivinar 
un número comprendido entre un rango de (1-20).
\n¡OJO!: Recuerda que solo tienes 5 oportunidades.\n¡Suerte! 
"""
INTENTOS = 0
TURNO2 = 5
#print aleatorio
while INTENTOS < 5:
    INGRESO = raw_input("Ingresa un número: ")
    try:
        INGRESO = int(INGRESO)
        SALIDA = 1
    except(RuntimeError, TypeError, NameError, ValueError):
        print u"Incorrecto. Tiene que indicar un valor numérico entero \n" # Comparador numerico
    if SALIDA == 1:
        INTENTOS += 1
        TURNO2 -= 1
        if INGRESO < ALEATORIO and INGRESO > 0: #verifica si el # es muy alto
            SALIDA = 0
            print u"Incorrecto. El número es Mayor. Inténtalo de nuevo."
            TURNO2 = str(TURNO2)
            print u"Te quedan "+ TURNO2 +" intentos\n"
            TURNO2 = int(TURNO2)
        if INGRESO > ALEATORIO and INGRESO < 20: #verifica si el # es muy bajo
            print u"Incorrecto. El numero es Menor. Inténtalo de nuevo."
            SALIDA = 0
            TURNO2 = str(TURNO2)
            print u"Te quedan "+ TURNO2 +" intentos\n"
            TURNO2 = int(TURNO2)
        if INGRESO > 20:
            print u"Incorrecto. Inténtalo de nuevo."
            TURNO2 = str(TURNO2)
            print u"Te quedan "+ TURNO2 +" intentos\n"
            TURNO2 = int(TURNO2)
            SALIDA = 0
        if INGRESO <= 0:
            print u"Incorrecto. Inténtalo de nuevo."
            TURNO2 = str(TURNO2)
            print u"Te quedan "+ TURNO2 +" intentos\n"
            TURNO2 = int(TURNO2)
            SALIDA = 0
        if INGRESO == ALEATORIO:
            break
if INGRESO == ALEATORIO:
    INTENTOS = str(INTENTOS)
    print u"¡Correcto!, " + JUGADOR + u" Usted gano adivino el número"
    print u" en tan solo: " + INTENTOS +u" intentos\n"
    print u"                     **** Adivinador Full Pro 2.0 © **** "
    print u"                            ***** Cognits *****"
    print u"                         Third Generation Grupo # 2 :\n"
    print u"                               Annabel Girón"
    print u"                               Fernando López"
    print u"                                Kevin Herrera\n"
    print u"                          KAR_KO,INDUSTRIS Copyright ®"
    time.sleep(5)
if INTENTOS == 5:
    ALEATORIO = str(ALEATORIO)
    print u"¡Terminó el Juego! ¡Inténtalo otra Vez!.\nEl número correcto era: " + ALEATORIO +"\n"
    print u"                     **** Adivinador Full Pro 2.0 © **** "
    print u"                            ***** Cognits *****"
    print u"                         Third Generation Grupo # 2 :\n "
    print u"                               Annabel Girón"
    print u"                               Fernando López"
    print u"                                Kevin Herrera\n"
    print u"                          KAR_KO,INDUSTRIS Copyright ®"
    time.sleep(5)
