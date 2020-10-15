def mas_grande(num1, num2, num3):
    menor = min(num1, num2, num3)
    mayor = max(num1, num2, num3)
    medio = (num1 + num2 + num3) - menor - mayor
    print("los valores son: {}, {}, {}.".format(mayor, medio, menor))


print("Dame Tres valores: ")
val1 = int(input())
print("Dame el segundo valor: ")
val2 = int(input())
print("Dame el tercer valor: ")
val3 = int(input())

mas_grande(val1, val2, val3)
