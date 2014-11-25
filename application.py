# -*- coding: utf-8 -*-
import random
import time

aleatorio = random.randint(1, 20)
exit = 0
print u"                              ***** Cognits *****"
print U"\n                       **** Adivinado Full Pro 2.0 © ****"
nombre = raw_input("Ingresa tu Nombre: ") 
print (u"""\n¡BIENVENIDO! """+ nombre +u"""\nINSTRUCCIONES: El reto del juego es adivinar un número comprendido entre 
un rango de (1-20). \n¡OJO!: Recuerda que solo tienes 5 oportunidades.\n¡Suerte! 
""") 
intentos = 0
turno2 = 5
#print aleatorio
while intentos < 5:

	numero = raw_input("Ingresa un número:  ")
	
	try: 
			numero = int(numero)
			exit = 1
	except: 
		print u"Tiene que indicar un valor numérico entero" # si no introduce un valor numerico, volvemos al inicio del bucle continue
		print 

	
	if exit == 1:

		intentos += 1
		turno2 -= 1


		if numero < aleatorio and numero >0: 
			print u"El número es Mayor"  # verifica si el numero es muy alto
			exit=0
			turno2=str(turno2)
			print (u"Te quedan "+ turno2 +" intentos")
			turno2=int(turno2)
			print 

		if numero > aleatorio and numero < 20: 
			print u"El numero es Menor" #verifica si el numero es muy bajo
			exit=0
			turno2=str(turno2)
			print (u"Te quedan "+ turno2 +" intentos")
			turno2=int(turno2)

			print

		if numero > 20:
			print (u"El Número debe ser menor o igual a 20")
			turno2=str(turno2)
			print u"Te quedan "+ turno2 +" intentos"
			turno2=int(turno2)
			exit =0
			print 

		if numero <=0:
			print (u"El Número debe ser Mayor a 0")
			turno2=str(turno2)
			print (u"Te quedan "+ turno2 +" intentos")
			turno2=int(turno2)
			exit =0
			print 


		if numero == aleatorio: 
			break

if numero == aleatorio: 
	intentos = str(intentos) 
	print
	print u"Excelente, " + nombre + u"! has adivinado el número en: " + intentos + u" intentos!"
	print 
	print u"                     **** Adivinador Full Pro 2.0 © **** "
	print u"                            ***** Cognits *****"
	print u"                         Third Generation Grupo # 2 :\n"
	print u"                               Annabel Girón"
	print u"                               Fernando López"
	print u"                                Kevin Herrera\n"
	print u"                          KAR_KO,INDUSTRIS Copyright ®"

	time.sleep(5)

if intentos == 5: 
	aleatorio = str(aleatorio) 
	print u"Lo sentimos te quedaste sin intentos y no adivinaste el número.\nEl número correcto era: " + aleatorio
	print 
	print u"                     **** Adivinador Full Pro 2.0 © **** "
	print u"                            ***** Cognits *****"
	print u"                         Third Generation Grupo # 2 :\n "
	print u"                               Annabel Girón"
	print u"                               Fernando López"
	print u"                                Kevin Herrera\n"
	print u"                          KAR_KO,INDUSTRIS Copyright ®"

	time.sleep(5)
