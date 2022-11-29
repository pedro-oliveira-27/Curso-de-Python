# Exercício: Cálculo do IMC

print('*******************************')
#Entrada de dados 

print('CALCULADORA DE IMC')
print('------------')
nome = input("Nome:")
altura = float(input("Altura: "))
peso = float(input("Peso: "))

print('------------')
#Cálculo do IMC

imc = peso//(altura**2)

print( f"{nome}, seu IMC é de: {imc}")

# analises dos IMC's

if imc < 16: 
    print("Classificação: Magreza grave")
elif 16 <= imc <=17: 
    print("Classificação: Magreza moderada")
elif 18.5 <= imc <=25: 
    print("Classificação: Saudavel")
#elif 25 < imc: 
else: 
    print("Classificação: Sobrepeso")

print()
print('*******************************')

    

