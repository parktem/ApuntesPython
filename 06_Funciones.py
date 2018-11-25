# -*- coding: utf-8 -*-

#Si a una función le pones param1=2, si no le pasas param1, tomará por defecto 2.
defaultVarForParam1 = 1;
defaultVarForParam2 = 2;
def sumatory(param1=defaultVarForParam1, param2=defaultVarForParam2):
    result = param1 + param2
    print "Resultado de la suma %d" % (result)
    return (param1, param2)

integer1 = 3;
integer2 = 4;
sumatory(integer1, integer2)


#Así puedes llamar a una función, la función tomará los valores que se le han asignado si es null, pero a y b se inicializarán con ese valor también.
a, b = sumatory();#  (1, 2)
print a
print b

#Si solo llamas a la función con una variable, y por defecto recibe y tiene dos valores, la varible tomará los dos valores en forma de lista.
c = sumatory();
print c

#Si llamas a la función pasandole un valor, tomará el valor pasado y tomará el valor por defecto al valor que no se haya pasado.
sumatory(integer1)

#Si especificas el valor que tendrá el parametro 2, pero no el 1, el 2 tendrá el valor pasado y el 1 tendrá el valor por defecto
sumatory(param2=integer1)

#Explica que si el valor por omisión es number=i, y despuès de la declaración de la función, haces que i tenga otro valor, la función seguirá usando el valor 
#de la i anterior a la declaración de la función.
i = 5

def f(number=i):
    print number

i = 6
f()

# Advertencia importante: Si el valor por omisión es una lista, cada vez que vayas llamando a la función de abajo, la lista será mutable e irá adoptando los nuevos valores.
def f1(a, L=[]):
    L.append(a)
    return L

print f1(1)
print f1(2)
print f1(3)

#Si no quieres que el valor por omisión se vaya cargando entre llamadas, se puede escribir así
def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print f2(1)
print f2(2)


#Los asteriscos son varios parametros en uno, los cuales funcionan en forma de lista.
def ventadequeso(tipo, *argumentos, **palabrasclaves):
    print "-- ¿Tiene", tipo, "?"
    print "-- Lo siento, nos quedamos sin", tipo
    for arg in argumentos:
        print arg
    print "-"*40
    claves = palabrasclaves.keys()
    claves.sort()
    for c in claves:
        print c, ":", palabrasclaves[c]

ventadequeso("Kingurger", "Es muy liquido, sr.",
           "Realmente es muy muy liquido, sr.",
           cliente="Juan Garau",
           vendedor="Miguel Paez",
           puesto="Venta de Queso Peruano")

def loro(tension, estado='rostizado', accion='explotar'):
    print "-- Este loro no va a", accion,
    print "si le aplicas", tension, "voltios.",
    print "Esta", estado, "!"

d = {"tension": "cuatro millones", "estado": "demacrado",
     "accion": "VOLAR"}

loro(**d)
