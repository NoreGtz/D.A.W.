tornillo = 5
tuerca = 3
arandela = 1

print("VERIFICADOR DE PEDIDOS")
a = int(input("Número de tuercas: "))
b = int(input("Número de tornillos: "))
c = int(input("Numero de arandelas: "))
d = (a * tuerca) + ( b * tornillo) + (c * arandela)

if b > a:
    print("Verifique el pedido")
    print("Costo total: ", d, "centavos")
if b == a: 
    print("La orden está bien")
    print("Costo total: ", d, "centavos")
if a > b:
    print("Exelente decisión")
    print("Costo total: ", d, "centavos")

