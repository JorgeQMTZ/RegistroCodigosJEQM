positivos = 0
suma = 0

n = int(input("Ingrese un numero ya sea positivo o negativo: "))
while n!=0:
    if n>0:
        positivos+=1
        suma = suma + n
    n = int(input("Ingrese un numero ya sea positivo o negativo: "))

print("la suma de los numeros positivos es de:", suma)
print("Cantidad de numeros positivos:", positivos)