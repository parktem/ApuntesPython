# -*- coding: utf-8 -*-

variable = 0


#Estructura de if, elif, y else.
if variable == 0:
    print "soy un cero"
elif variable == 1:
    print "soy un uno"
else :
    print "no se sabe lo que soy"

a = ['Mary', 'tenia', 'un', 'corderito']

#Estructura de for, range(len(a)) es "Hasta rango de longitud de a, es decir, hasta 4"
for i in range(len(a)):
    print i, a[i]

indice = 30
step = 10

#range es obligatorio si quieres que avance hasta un numero. Ejemplo for i in range(10).
#range es capaz también de recibir distintos parametros, indice es desde donde empieza la i, 100 que no puede llegar ni sobrepasar, y step es la incrementación.
for i in range(indice, 100, step):
    print i

a = ['bruja','pikachu', 'xyzzy']

#Así le puedes decir hasta que parametro quieres que lea, y la i asumirá ese valor. Es como un foreach.
for i in a[0:2]:
    print i, #Apunte: Esta coma que hay hace que el proximo output se muestre pegado a este.

#Aquí explica que puedes comprobar si un valor esta dentro de un vector poniendo un in. También que el OR se escribe como 'or'
tuplasSi = ('s', 'S', 'si', 'Si', 'SI')
tuplasNo = ('n', 'no', 'No', 'NO')
tuplasPuede = ('puede', 'posiblemente', 'quizas')
ok = 'no';
if (ok in tuplasSi or ok in tuplasPuede):
    print "Aqui no se encuentra"
if ok in tuplasNo:
    print "Aqui se ha encontrado"

#while True:
#   pass
