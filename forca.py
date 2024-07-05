def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    palavra_secreta="BANANA"
    acertou=False
    enforcou=False
    letras_acertadas=["_", "_", "_", "_", "_", "_"]
    erros=0
    while(not acertou and not enforcou):
        chute=input("Digite uma letra").strip().upper()
        indice=0
        for letra in palavra_secreta:
            if(letra==chute):
                letras_acertadas[indice]=letra
                print("Encontrei a letra {} na posição {}".format(letra, indice+1))
            else:
                erros+=1
                if(erros<6):
                    print("Você ainda tem {} erros permitidos antes de ser enforcado".format(6-erros))
            indice+=1
        print(letras_acertadas)
        enforcou=erros==6
        acertou="_" not in letras_acertadas
    if(acertou):
        print("Você ganhou!")
    else:
        print("Você foi enforcado!")
    print("Fim do jogo")
if(__name__=="__main__"):
    jogar()