#jogo caça-palavras 
secreta = 'doido'
tentativa = input('Digite uma letra da palavra secreta: ')

i = ' ' n

if tentativa in secreta:
    print (f'Tem na palavra: {tentativa}')
else: 
    print('*')

while tentativa != secreta: 
    print('tente outra vez')
    continue
else: 
    print("Parabéns")


""" 
for i in tentativa:
    i += tentativa 

"""

    
       



