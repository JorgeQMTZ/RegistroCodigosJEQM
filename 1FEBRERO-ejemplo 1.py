#Buscar palabra, y caracter donde inicia y termina

import re

texto = "en esta cadena hay una palbra magica"

x = re.search('magica', texto)

if x:
    print("Si se ha encontrado")
else:
    print("No se ha encontrado")