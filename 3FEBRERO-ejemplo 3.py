# * : indica la repetición de un carácter cero o más veces.
# + : indica la repetición de un carácter una o más veces.
# ? : Es el carácter reluctant o cuantificador reacio.

#Añadido a cualquiera de los anteriores se contará con la ocurrencia más corta posible.

import re

frase = "Ramón y Román programan en Python"
patron = '.+n'
print(re.findall(patron, frase))

patron = '.+?n'
print(re.findall(patron, frase))