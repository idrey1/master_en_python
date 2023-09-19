from coche import Coche

carro = Coche('Amarillo','Renault','Clio',150,200,4)
carro1 = Coche('Verde','Seat','Panda',250,200,4)
carro2 = Coche('Azul','Citroen','Xara',100,180,4)
carro3 = Coche('Rojo','Mercedez','Clase A',350,400,4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado
if type(carro3) == Coche:
    print('Es un objeto correcto')
else:
    print('No es un objeto')

# Visibilidad
print(carro.soy_publico)
#print(carro.__soy_privado)
print(carro.getPrivado())
