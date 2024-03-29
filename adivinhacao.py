import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\n")

    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"\nTentativa: {rodada} de {total_de_tentativas}")

        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou: " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!\n")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou!")
            print(f"Sua pontuação foi: {pontos}\n")
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto!\n")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto!\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("FIM DE JOGO!")

if (__name__ == "__main__"):
    jogar()