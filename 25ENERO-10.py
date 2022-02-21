class MiCarro:
    def __init__(self, convertible, valor, nombre):
        self.convertible=convertible
        self.valor=valor
        self.nombre=nombre
        
m1=MiCarro("convertible rojo", 60000, "Fer")
print("---------------------------")
print("Datos del primer vehiculo: ")
print("---------------------------")
print(m1.convertible)
print(m1.valor)
print(m1.nombre)

print("--------------------------")

m1=MiCarro("van azul", 10000, "Jump")
print("---------------------------")
print("Datos del segundo vehiculo: ")
print("---------------------------")
print(m1.convertible)
print(m1.valor)
print(m1.nombre)