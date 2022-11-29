# Strings são interáveis 
#nome = "pedro"
#print(nome[2])
#print(nome[-3])
#print(30*'-')
#print('a' in nome)
#print('z' in nome)
#print('ed' in nome)

nome = input('nome: ')

encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else: 
    print(f'{encontrar} não está em {nome}')





