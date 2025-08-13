import math
#for name in dir(math):
#        print(name,end=',')
# ceil,floor,trunc
print(math.ceil(4.2))  # 5
print(math.floor(4.9))  # 4
print(math.trunc(4.2))  # 4

print(math.factorial(4))
print(math.sqrt(16))  # 4.0
print(math.hypot(3, 4))  # 5.0
print(math.pow(2, 3))  # 8.0
print(math.sin(90))


angulo_graus = math.degrees(math.pi/2)  # Converte pi radianos para graus
print(angulo_graus)  # Saída: 180.0