def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")

    palavra_secreta = "BaNAna"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    
    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if ((chute.lower()) == (letra.lower())):
                letras_acertadas[index] = letra.lower()
            index = index + 1

        print(letras_acertadas)

    print("FIM DE JOGO!")

if (__name__ == "__main__"):
    jogar()