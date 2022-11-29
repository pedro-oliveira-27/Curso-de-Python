#Introdução ao try/except 

print(30*"-")
numero = input("Digite um número inteiro: ")
try:
    numero_int = int(numero)
    numero_teste = numero_int%2 
    if (numero_teste) == 0:
        print("Numero par")
        print(30*"-")
    else:
        print("Numero impar")
        print(30*"-")
except: 
    print("Você deve digitar um número inteiro")
    print(30*"-")