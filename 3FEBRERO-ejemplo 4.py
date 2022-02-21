# [a-z]+ : indica una secuencia de letras minúsculas.
# [A-Z]+ : se usa para encontrar secuencias de letras mayúsculas.
# [a-zA-Z]+ : es para secuencias de letras mayúsculas o minúsculas.
# [A-Z][a-z]+ : secuencias de una letra mayúscula seguida de una o más letras mayúsculas.
# [0-9]+ : para secuencias de números de uno o más dígitos.

import re

frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[0-9]+'
print(re.findall(patron, frase))