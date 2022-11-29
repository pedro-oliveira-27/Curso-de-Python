# Calculadora com While  

#enquanto o while for True a calcuadora nbão irá parar 
while True: 
    
    # entrada de dados
    print(20*'-')
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    operadores_permitidos = '+-/*'

    num_1_float = 0
    num_2_float = 0

    #checagem de numeros inteiros
    try:
        #transformando o str em float
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        
        #checagem de apenas um operador
        if len(operador) >1: 
            print(20*'-')
            print('Digite apenas um operador!') 
            print(20*'-')
        
        #checagem de operadores permitidos
        if operador not in operadores_permitidos:
            print(20*'-')
            print('Operador Inválido!!')
            print(20*'-')

        #Operação de soma
        if operador == '+':
            soma = num_1_float + num_2_float 
            print(20*'-')
            print(f'O resultado da soma é: {soma}') 
            print(20*'-')

        #operação de subtração
        elif operador == '-':
            subtração = num_1_float - num_2_float 
            print(20*'-')
            print(f'O resultado da subtração é: {subtração}') 
            print(20*'-')

        #operação de multiplicação
        elif operador == '*':
            multiplicação = num_1_float * num_2_float 
            print(20*'-')
            print(f'O resultado da soma é: {multiplicação}') 
            print(20*'-')

        #operação de divisão
        elif operador == '/':
            divisão = num_1_float / num_2_float 
            print(20*'-')
            print(f'O resultado da soma é: {divisão}')     
            print(20*'-')
        else: 
            print("NUNCA DEVERIA APARECER")
    #caso o número não seja inteiro 
    except: 
        print(20*'-')
        print('Você deve digitar um número inteiro. Tente novamente!')
        print(20*'-')

    sair = input ("Que Sair? [s]im: ").lower().startswith('s')
    
    #Para sair so sistema
    if sair is True: 
        print(20*'-')
        break
     


