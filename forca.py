import random
import funcoes_do_jogo as fdj

def jogar():

    fdj.imprimir_mensagem_de_abertura()
    palavra_secreta = fdj.carregar_palavra_secreta()

    letras_acertadas = fdj.inicializa_letras_acertadas(palavra_secreta)
    print(f"{letras_acertadas}\n")

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = fdj.chute_do_jogador()

        if (chute in palavra_secreta):
            fdj.marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            fdj.desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(f"{letras_acertadas}\n")

    if (acertou):
        fdj.imprime_mensagem_vencedor()
    else:
        fdj.imprime_mensagem_perdedor(palavra_secreta)

    fdj.imprimir_mensagem_final()


if (__name__ == "__main__"):
    jogar()