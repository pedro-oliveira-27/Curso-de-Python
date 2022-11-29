#Saudação bom dia, boa tarde e boa noite 

print(30*"-")
nome = input("Qual é o seu nome: ")
horas = input("Escreva somente as horas: ")

try: 

    horas_int = int(horas)
    if 0 <= horas_int <12:
        print(f"{nome}, bom dia")
        print(30*"-")
    elif 12 <= horas_int <= 17: 
        print(f"{nome}, boa tarde")
        print(30*"-")
    elif 17 < horas_int <= 23: 
        print(f"{nome}, boa noite")
        print(30*"-")
    else: 
        print("Não conheço essas horas")
        print(30*"-")

except: 
    print(f"{nome}, entrada inválida. tente novamente!!")
    print(30*"-")
