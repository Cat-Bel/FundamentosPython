print("Por favor introduce la siguiente información: ")
n_a = int(input("Número de años a ahorrar: "))
m = int(input("Periodicidad de sus aportaciones: "))
R = float(input("Monto: "))
j = float(input("Tasa de interes (expresada en porcentaje): "))/100

#Cálculos
i = j/m
print(type(i))
n = n_a*m

M = R*((1+i)**n-1)/i

numUno = 1
numDos = 2

num_uno = 1
num_dos = 2

print(f'Si ahorras {R} pesos {m} al año, al final de {n_a} años habrás ahorrado {M:.2f}')