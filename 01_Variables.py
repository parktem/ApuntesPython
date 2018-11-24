# -*- coding: utf-8 -*-

#Import math as math_lib es poner un alias a la librería importada, que en este caso sería math_lib.
#from math import * significa que de math importamos todo.
#import os es simplemente importar la librería os.
import math as math_lib;
from math import *;
import os


#asignacion de variables
#Lo interesante aqui es que si multiplicas por 5 un string, lo que hace es repetirlo las veces que haya sido multiplicado. 
variable = '123';
print(variable)
print(variable * 5);

#Función sin devuelve el seno (de la librería math)
variable = 1;
seno = sin(variable)
print(variable);
print(seno);

#Si sacas por pantalla un booleano, te devolverá literalmente "False/True".
variable = False;
print(variable);

#Python es capaz de asignar distintos valores a distintas variables de este modo.
a, b = 0 , 1
print(a)
print(b)
print(a + b)
a, b, c = 0 , 1, 2
print(a , b , c) 


