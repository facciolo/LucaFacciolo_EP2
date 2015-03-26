import random
digitadas = []
acertos = []
erros = 0
lista1 = []
lista = open("entrada.txt","r+",encoding = "utf-8")
leitura = lista.readlines()
palavra = random.choice(leitura).lower()#comando para tirar acento
a = ''
print(palavra)#teste
while (erros < 6 or acertos != palavra):
    a = input("digite uma letra: ").lower()
    if a in palavra and len(a)==1:
            if a in digitadas:
                print("voce ja digitou essa letra")
            else:
                print("Acertou , digite outra letra")
                digitadas.append(a)
                acertos.append(a)
                print("letras digitadas",digitadas)
    elif a not in palavra and len(a)==1:
                if a in digitadas:
                    print("voce ja digitou essa letra")
                else:
                    print("Voce errou , tente novamente")
                    erros = erros + 1
                    digitadas.append(a)
                    print("letras digitadas",digitadas)
                    print("total de 6 tentativas.",erros,"erros atuais")
                    #1-
    else:
            print("Bugou , tente novamente")
            
                """1-if erros == 1:
                                #desenhar cabeça
                    if erros == 2:
                                #desenhar tronco
                    erros == 3:
                                #desenhar braço esquerdo
                    erros == 4:
                                #desenhar braço direito
                    erros == 5:
                                #desenhar perna esquerda
                    erros == 6:
                                #desenhar perna direita
                                print("voce perdeu")"""






