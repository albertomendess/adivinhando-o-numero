
def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")

    palavra_secreta = "BaNAna"

    enforcou = False
    acertou = False
    
    while (not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if ((chute.lower()) == (letra.lower())):
                print(f"Encontrei a letra {letra.lower()} na posição {index}")
            index = index + 1

        print("...")

    print("FIM DE JOGO!")

if (__name__ == "__main__"):
    jogar()