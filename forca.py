def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")

    palavra_secreta = "BaNAna".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0
    
    print(letras_acertadas)

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
            print(f"\nVocê errou! Restam apenas {6 - erros}\n")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("\nPARABENS! VOCÊ GANHOU!")
    else:
        print("\nVOCÊ PERDEU!")

    print("\n*********************************")
    print("********** FIM DE JOGO! *********")
    print("*********************************")


if (__name__ == "__main__"):
    jogar()