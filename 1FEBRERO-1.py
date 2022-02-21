import re

texto = "En esta cadena se encuentra una palabra mágica"
x = re.search('palabra mágica', texto)

if x:
    print("SI se ha encontrado!")

else:
    print("NO encontrado")
