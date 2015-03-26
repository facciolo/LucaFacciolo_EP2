import random
digitadas = []
acertos = []
erros = 0
lista1 = []
lista = open("entrada.txt","r+",encoding = "utf-8")
leitura = lista.readlines()
palavra = random.choice(leitura)
palavra.index
a = ''

def letras(a):
    global erros
    a = input("digite uma letra: ").lower()
    while (erros != 6):
        if a in palavra and len(a)==1:
            if a in digitadas:
                print("voce ja digitou essa letra")
                break
            print("Acertou , digite outra letra")
            digitadas.append(a)
            acertos.append(a)
            print("letras digitadas",digitadas)
            break
        elif a not in palavra and len(a)==1:
            if a in digitadas:
                print("voce ja digitou essa letra")
                break
            print("Voce errou , tente novamente")
            erros = erros + 1
            digitadas.append(a)
            print("letras digitadas",digitadas)
            print("total de 6 tentativas.",erros,"erros atuais")
            break
        else:
            print("Bugou , tente novamente")
            break
        


print(palavra)#teste
while(erros != 6):
    letras(a)

if erros != 6:
    print("voce ganhou")
    print("a palavra era", palavra)
else:
    print("voce perdeu")
    print("a palavra era", palavra)

