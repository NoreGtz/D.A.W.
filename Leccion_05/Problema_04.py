import math

print("INDICE DE SENSACIÓN TERMICA (WCI)")
v = float(input("Velocidad del viento en millas por hora: "))
t = float(input("Temperatura en grados Fahrenheit: "))
wci = 0.0
if(0 <= v <= 4):
    wci = t
    print()
    print("Indice de Sensación Termica: ",wci)
elif v >= 45:
    print()
    wci = ((1.6 * t ) - 55)
    print("Indice de Sensación Termica: {0:.2f}".format(wci))
else:
    print()
    wci = ((91.4) + ((91.4 - t)*((0.0203 * (math.sqrt(v))) - 0.474)))
    print ("Indice de Sensación Termica: {0:.2f}".format(wci))
