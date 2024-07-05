def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    palavra_secreta="BANANA"
    acertou=False
    enforcou=False
    letras_acertadas=["_", "_", "_", "_", "_", "_"]
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