def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    palavra_secreta="banana"
    acertou=False
    enforcou=False
    while(not acertou and not enforcou):
        chute=input("Digite uma letra").strip()
        indice=0
        for letra in palavra_secreta:
            if(letra.upper()==chute.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, indice+1))
            indice+=1
    print("Fim do jogo")
if(__name__=="__main__"):
    jogar()