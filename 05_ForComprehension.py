# -*- coding: utf-8 -*-


#Funcion strip elimina los espacios iniciales y finales de cada string o un caracter en el caso de que se le pase.
frutafresca = ['  banana', '  mora de Logan ', 'maracuya  ']
print [arma.strip() for arma in frutafresca]

#Bucles con condiciones sobre la x.
vec = [2, 4, 6]
print [3*x for x in vec]
print [3*x for x in vec if x > 3]
print [3*x for x in vec if x < 2]

#Cuando a un numero le pones x ** 3 significa que le pones el exponente 3
print [[x,x**2] for x in vec]
#El vector también se puede poner con parentesis.
print [(x, x**2) for x in vec]

#Maneras de interactuar en un bucle con dos vectores sin necesitar bucles anidados.
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print [x*y for x in vec1 for y in vec2]
print [x+y for x in vec1 for y in vec2]
print [vec1[i]*vec2[i] for i in range(len(vec1))]


mat = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
      ]

# Manera de recorrer un bucle por columnas.
for i in [0, 1, 2]:
    for fila in mat:
        print fila[i],
    print