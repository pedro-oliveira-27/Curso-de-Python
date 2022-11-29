# caça-palavras correção 

import os 


palavra_secreta = 'perfume'
letras_acertadas = ' '
numero_tentativa = 0

while True: 
    #os.system('cls')
    letra_digitada = input('Digite uma letra: ')
    numero_tentativa += 1

    if len(letra_digitada) > 1: 
        print('Digite apenas uma letra')
        continue 
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta: 
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else: 
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        
        print(15*'-')
        print(f'Palavra secreta: {palavra_secreta}')
        print('Tentativas: ', numero_tentativa)
      
        if numero_tentativa == (len(palavra_secreta) - 1):
            print('Você é um gênio')
        else:
            print('Você pode melhorar') 

        print('GAME OVER')
        print(15*'-')



        







