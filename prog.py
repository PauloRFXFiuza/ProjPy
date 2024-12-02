import math as m
from capTexts import capText

print(" -- Programa Iniciado -- \n")

a = m.pi
print("π = ", a , "\n")

b = m.sqrt(a)
print("√π = ", b , "\n")

c = float(input("Insira um numero ao qual sera a base da potenciacao: "))
print("O numero inserido foi ", c , "\n")

d = float(input("Insira um numero ao qual sera o expoente da potenciacao: "))
print("O numero inserido foi ", d , "\n")

e = m.pow(c,d)
print(" ", c , "^" , d ,"=" , e , "\n")

f= 'arroz e feijao   '

print(f)
print(capText(f))

print(" -- Programa Concluído -- \n")