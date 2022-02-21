frase = input("Frase: ")

letra=input("Letra: ")
i=0

while i!=len(frase):
    if letra!=frase[i]:
        print("No se encontró en la posición numero ", i)
        i+=1
        continue
    print("Se encontró en la posición numero ", i)
    break