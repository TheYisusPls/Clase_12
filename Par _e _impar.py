def par_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


print("Dime un numero: ")
valor = int(input())

if par_impar(valor):
    print("tu numero es par")
else:
    print("tu numero es impar")
