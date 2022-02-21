def EsPar():
    print("El numero es par")
    
def EsImpar():
    print("El numero es impar")
    
num = int(input("Ingresa un numero ENTERO: "))

if num%2==0:
    EsPar()
if num%2!=0:
    EsImpar()