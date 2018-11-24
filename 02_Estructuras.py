# -*- coding: utf-8 -*-

#Esto son listas en python, a las cuales se accede a sus valores como un vector en Java.
#len es lo mismo que length.
#a[0:-1] es "sacame desde la posición 0 contando desde el principio, hasta la posición que yo te indique."
#Si la posición indicada empieza por negativo, se refiere contando desde el final.
#Si solo pone un numero, si lo pone a la izquierda [2:] significa "Saca todo desde la posición 2", en cambio [0:2] significa "Saca todo hasta la posición 2"
a = ['pan', 'huevos', 100, 1234]
print(len(a))
print(a[0:-1])
print(a[:2])
print(a[:2] + ['carne', 2 * 2]) #Concatena el vector a hasta la segunda posición con un nuevo vector inicializado ahí mismo.

#Si haces print a un array bidimensional, lo saca tal cual.
matrix =[ [1,2,3] , [6,5,4], [7,9,8]]
print(matrix)

#print 2 * (a[:2] + ['Boo!'])
# A  diferencia de las cadenas de texto,
# que son inmutables, es posible cambiar
# un elemento individual de una lista:
a = ['pan', 'huevos', 100, 1234]
a[2] = a[2] + 23
print(a[2])
print(a)


# reemplazar algunos
a[0:2] = [1, 12, 14]
print(a)


# borrar algunos
a[0:2] = [] # a[0:2] = list()
print(a)


# insertar algunos
a[1] = ['bruja', 'xyzzy']
print(a)
# Reemplazar algunos elementos:

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
print(a)


thelist = [5, 3, 'p', 9, 'e']
print thelist[0]
print thelist[4]
# print thelist[5] lanza una excepcion
print thelist[-1]
print thelist[-2]



#trabajando con diccionarios
#Si incializas una variable con {} interpreta que es un diccionario, significa que el valor va ligado a un identificador.
emptyDict = {}
thisdict = {'a':1, 'b':23, 'c':"eggs"}
del thisdict['b']
print thisdict;


