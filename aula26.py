secreta = 'doido'
tentativa = ' '
i = 0
while tentativa != secreta: 
    i += 1
    tentativa = input('Dê o seu chute: ')
    if tentativa in secreta:
        print(f'correto ({i}): {tentativa}')
        print(15*'-')
        continue
    else: 
        print(f'incorreto ({i}): *')
        print(15*'-')
        continue 
else: 
    print('Parabéns você acertou!!')
    print(15*'-')
    
