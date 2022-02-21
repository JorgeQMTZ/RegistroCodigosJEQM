#Encontrar palabra y contarlas

import re

texto = "hola adios hola hola"

#encontar palabra hola
print (re.findall('hola', texto))

#contar numero de palabra hola
print (len(re.findall('hola', texto)))