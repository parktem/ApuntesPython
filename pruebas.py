# -*- coding: utf-8 -*-

defaultVarForParam1 = 1;
defaultVarForParam2 = 2;
def sumatory(param1=defaultVarForParam1, param2=defaultVarForParam2):
    result = param1 + param2
    print "Resultado de la suma %d" % (result)
    return (param1, param2)

integer1 = 3;
integer2 = 4;
sumatory(integer1, integer2)

