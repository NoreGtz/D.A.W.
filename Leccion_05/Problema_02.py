tanque = int(input("Capacidad del tanque: "))
medi = int(input("Lectura del medidor: "))
millas = int(input("Millas por galón: "))
gas = tanque * (medi/100) * millas

if gas < 200:
    print("Distancia que puede recorrer: {0:.2f}".format(gas), "millas")
    print("¡Consigue gas!")
else:
    print("Distancia que puede recorrer: {0:.2f}".format(gas), "millas")
    print("Es seguro proceder")
    
