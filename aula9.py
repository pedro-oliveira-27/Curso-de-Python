print('-------------------')
#Entrada de dados 
entrada = input("[E]ntrar ou [S]air: ")

# Entrar no sistema
if (entrada == "E") or (entrada == "e"):
    senha_digitada = input("Digite sua senha: ")
    senha_cadastrada = "123456"

    #Senha Valida
    if senha_digitada == senha_cadastrada:
        print("Bem vindo ao sistema") 
        
    #Senha inválida 
    elif senha_digitada != senha_cadastrada: 
        print("Senha incorreta") 
        print("Reinicie o programa e tente novamente")
        
#Sair do sistema
if (entrada == "s") or (entrada == "S"):
    print("Sair do sistema")
    
if not entrada: 
    print("Você não digitou nada")
    print("Reinicie o programa e tente novamente")

#Digito invalido 
else: 
    print("Você deve digitar E ou S")
    print("Reinicie o programa e tente novamente")

print('-------------------')