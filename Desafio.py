def mas_grande(num1, num2, num3, d):
    menor = min(num1, num2, num3)
    mayor = max(num1, num2, num3)
    medio = (num1 + num2 + num3) - menor - mayor

    if d == "N":
        print("Los Valores Son: {}, {}, {}".format(mayor, medio, menor))

    else:
        print("Los Valores Son: {}, {}, {}".format(menor, medio, mayor))


print("Dame Tres valores: ")
val1 = int(input())
print("Dame el segundo valor: ")
val2 = int(input())
print("Dame el tercer valor: ")
val3 = int(input())

while True:
    print("Quieres ordenar los Valores de manera: Ascendente(Y) o Descendente(N) , Choose: Y/N ")
    decicion = input()

    if decicion == "Y" or decicion == "N":
        mas_grande(val1, val2, val3, decicion)
        break
    else:
        print("tienes que ingresar Y o N")
