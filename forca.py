import random, sys
def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
def carrega_palavra_secreta(nome_arquivo="palavras.txt", primeira_linha_valida=0):
    arquivo_palavras=open(nome_arquivo)
    palavras=arquivo_palavras.read().split("\n")
    try:
        if(primeira_linha_valida<0 or primeira_linha_valida>len(palavras)):
            raise ValueError("Índice inválido para a primeira palavra secreta")
    except ValueError as e:
        print("Erro: ", e, file=sys.stderr)
    palavra_secreta=palavras[random.randrange(primeira_linha_valida-1, len(palavras))].upper().replace("\n", "").replace("\r", "")
    return palavra_secreta
def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]
def pede_chute():
    return input("Digite uma letra").strip().upper()
def imprime_mensagem_perdedor():
    print("Você foi enforcado!")
def imprime_mensagem_vencedor():
    print("Você ganhou!")
def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    indice=0
    for letra in palavra_secreta:
        indice+=1
        if(letra==chute):
            letras_acertadas[indice-1]=letra
            print("Encontrei a letra {} na posição {}".format(letra, indice))
    print(letras_acertadas)
    if("_" not in letras_acertadas):
        imprime_mensagem_vencedor()
        return True
    else:
        return False
def jogar():
    imprime_mensagem_abertura()
    palavra_secreta=carrega_palavra_secreta()
    letras_acertadas=inicializa_letras_acertadas(palavra_secreta)
    erros=0
    while(True):
        chute=pede_chute()
        if(chute not in palavra_secreta):
            erros+=1
            if(erros<6):
                errosRestantes=6-erros
                print("Você ainda tem {} {} antes de ser enforcado".format(errosRestantes, "erros permitidos" if errosRestantes>1 else "erro permitido"))
                continue
            else:
                imprime_mensagem_perdedor()
                break
        if(marca_chute_correto(chute, palavra_secreta, letras_acertadas)):
            break
    print("Fim do jogo")
if(__name__=="__main__"):
    jogar()