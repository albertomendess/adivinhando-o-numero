"""Funções usadas no Jodo da Forca"""
import random

def imprimir_mensagem_de_abertura():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")


def imprimir_mensagem_final():
    print("\n*********************************")
    print("********** FIM DE JOGO! *********")
    print("*********************************")


def carregar_palavra_secreta():
    
    filename = "C:/Users/alber/Documents/arquivos_TXT/frutas.txt"
    palavras = []

    with open (filename) as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def chute_do_jogador():
    chute = input("Qual a letra? ")
    return chute.strip().upper()


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("\nPARABENS! VOCÊ GANHOU!")


def imprime_mensagem_perdedor():
    print("\nVOCÊ PERDEU!")

