costA = float(input("Precio por libra paquete A: "))
porcA = float(input("Porcentaje magro paquete A: "))
costB = float(input("Precio por libra paquete B: "))
porcB = float(input("Porcentaje magro paquete B: "))

A = costA/porcA
B = costB/porcB
print()
print("Costo por libra de carne magra Paquete A: ","{0:.4f}".format(A))
print("Costo por libra de carne magra Paquete B: ","{0:.4f}".format(B))

if A < B:
    print()
    print("El paquete A es el de mejor valor.")
else:
    print()
    print("El paquete B es el de mejor valor.")