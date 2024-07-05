import random
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    arquivo_palavras=open("palavras.txt")
    palavras=arquivo_palavras.read().split("\n")
    palavra_secreta=palavras[random.randint(0, len(palavras)-1)].upper().replace("\n", "").replace("\r", "")
    letras_acertadas=["_" for letra in palavra_secreta]
    erros=0
    while(True):
        chute=input("Digite uma letra").strip().upper()
        if(chute not in palavra_secreta):
            erros+=1
            if(erros<6):
                errosRestantes=6-erros
                print("Você ainda tem {} {} antes de ser enforcado".format(errosRestantes, "erros permitidos" if errosRestantes>1 else "erro permitido"))
                continue
            else:
                print("Você foi enforcado!")
                break
        indice=0
        for letra in palavra_secreta:
            indice+=1
            if(letra==chute):
                letras_acertadas[indice-1]=letra

                print("Encontrei a letra {} na posição {}".format(letra, indice))
        print(letras_acertadas)
        if("_" not in letras_acertadas):
            print("Você ganhou!")
            break
    print("Fim do jogo")
if(__name__=="__main__"):
    jogar()