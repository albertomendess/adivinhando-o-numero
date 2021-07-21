import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")

    filename = "C:/Users/alber/Documents/arquivos_TXT/frutas.txt"
    palavras = []

    with open (filename) as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    
    print(f"{letras_acertadas}\n")

    while (not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"\nVocê errou! Restam apenas {6 - erros}")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(f"{letras_acertadas}\n")

    if (acertou):
        print("\nPARABENS! VOCÊ GANHOU!")
    else:
        print("\nVOCÊ PERDEU!")
        print(f"A palavra certa é {palavra_secreta.upper()}")

    print("\n*********************************")
    print("********** FIM DE JOGO! *********")
    print("*********************************")


if (__name__ == "__main__"):
    jogar()