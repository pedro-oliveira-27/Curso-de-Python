#Este jogo adivinha um número entre 1 e 100.    
import random
def adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("Bem-vindo ao jogo de adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")

    while not acertou:
        palpite = input("Digite seu palpite (ou 'sair' para encerrar): ")

        if palpite.lower() == 'sair':
            print("Jogo encerrado. Obrigado por jogar!")
            break

        if not palpite.isdigit():
            print("Por favor, digite um número válido.")
            continue

        palpite = int(palpite)
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            acertou = True
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")


adivinhacao()