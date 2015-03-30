from random import choice
import turtle    
from time import sleep
import unicodedata
#Listas
digitadas = []
acertos = []
erros = 0
lista1 = []
#Escolhendo a palavra 
lista = open("entrada.txt","r+",encoding = "utf-8")
leitura = lista.readlines()
if leitura != "":
    palavra = choice(leitura).lower().strip()# + comando para tirar acento
a = ''
for i in palavra:
    if i not in lista1 and i != " ":
        lista1.append(i)
        lista1.sort()
#Cursores da interface
window = turtle.Screen()
window.bgcolor("black")
window.title("Forca")
window.bgpic("planofundo.gif")

tartaruga = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(1000)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(200,0)
tartaruga.pendown()
tartaruga.color("white")

tartaruga2 = turtle.Turtle()
tartaruga2.speed(1000)
tartaruga2.penup()
tartaruga2.setpos(-100,0)
tartaruga2.pendown()
tartaruga2.color("white")
tartaruga2.hideturtle()

tartaruga3 = turtle.Turtle()
tartaruga3.speed(1000)
tartaruga3.penup()
tartaruga3.setpos(-100,0)
tartaruga3.pendown()
tartaruga3.color("white")
tartaruga3.hideturtle()

tartaruga4 = turtle.Turtle()
tartaruga4.speed(1000)
tartaruga4.penup()
tartaruga4.setpos(-250,-250)
tartaruga4.pendown()
tartaruga4.color("white")
tartaruga4.hideturtle()

tartaruga5 = turtle.Turtle()
tartaruga5.speed(1000)
tartaruga5.penup()
tartaruga5.setpos(-247,-248)
tartaruga5.pendown()
tartaruga5.color("white")
tartaruga5.hideturtle()
#Desenhos na interface
def tronco(erros):
    if erros ==1:#cabeça
        tartaruga.penup()
        tartaruga.setpos(250,200)
        tartaruga.pendown()
        tartaruga.rt(90)
        tartaruga.circle(20)    
    if erros == 2:#tronco
        tartaruga.penup()
        tartaruga.setpos(250,160)
        tartaruga.pendown()
        tartaruga.rt(270)
        tartaruga.forward(65)    
    if erros == 3:#braço esquerdo
        tartaruga.penup()
        tartaruga.setpos(250,140)
        tartaruga.pendown()
        tartaruga.rt(260)
        tartaruga.forward(30)    
    if erros == 4:#braço direito
        tartaruga.penup()
        tartaruga.setpos(250,140)
        tartaruga.pendown()
        tartaruga.rt(230)
        tartaruga.forward(30)    
    if erros == 5:#perna esquerda
        tartaruga.penup()
        tartaruga.setpos(250,95)
        tartaruga.pendown()
        tartaruga.rt(170)
        tartaruga.forward(50)
    if erros == 6:#perna direita
        tartaruga.penup()
        tartaruga.setpos(250,95)
        tartaruga.pendown()
        tartaruga.rt(110)
        tartaruga.forward(50)
#Textos na interface    
def escrever_textostemporal(c):
    tartaruga2.penup()
    tartaruga2.setpos(-250,-130)
    tartaruga2.write(c,font = ("arial",15,"normal"))
    sleep(0.8)
    tartaruga2.clear()
def escrever_textos(b):
    tartaruga.penup()
    tartaruga.setpos(0,250)
    tartaruga.write(b,font = ("arial",15,"normal"))    
def escrever_digitadas():
    digitadas.append(a)
    tartaruga3.penup()
    tartaruga3.setpos(-60,-200)
    tartaruga3.pendown()
    tartaruga3.write(digitadas,font = ("arial",15,"normal"))
    sleep(1.5)
    tartaruga3.clear()    
def escrever_textocomtitulo2(titulo,conteudo):
    tartaruga.penup()
    tartaruga.setpos(-300,200)
    tartaruga.pendown()
    tartaruga.write(titulo,font = ("arial",20,"normal"))
    tartaruga.penup()
    tartaruga.setpos(-300,170)
    tartaruga.write(conteudo,font = ("arial",20,"normal"))
    
#DESENHO FORCA:    
for i in range(1):
    tartaruga.pensize(5)
    tartaruga.left(90)  # Vira o angulo pedido
    tartaruga.forward(250) # Avança a distancia pedida
    tartaruga.hideturtle()    
for i in range(2):
    tartaruga.left(270)
    tartaruga.forward(50)
    tartaruga.hideturtle()
for i in palavra:
    if i != " ":
        tartaruga4.forward(20)
    if i == " ":
        tartaruga4.penup()
        tartaruga4.forward(20)
        tartaruga4.pendown()
    tartaruga4.penup()
    tartaruga4.forward(5)
    tartaruga4.pendown()
    
escrever_textocomtitulo2(palavra,lista1)
while (erros != 6 and acertos != lista1):
    a = window.textinput("","digite uma letra ou a palavra misteriosa").lower()
    if a == palavra:
        break
    if a != " " and a in lista1 and len(a)==1 :
                if a in digitadas:
                    escrever_textostemporal("Voce ja digitou essa letra!")
                else:
                    escrever_textostemporal("acertou")
                    z = 0
                    while z < len(palavra):
                        if a == palavra[z]:
                            tartaruga5.penup()
                            tartaruga5.forward(z*25)
                            tartaruga5.pendown()
                            tartaruga5.write(a, font = ("arial",20,"normal"))
                            tartaruga5.penup()
                            tartaruga5.backward(z*25)
                        z += 1
                    escrever_digitadas()
                    digitadas.sort()                    
                    acertos.append(a)
                    acertos.sort()
    elif a not in lista1 and len(a)==1:
                if a in digitadas:
                    escrever_textostemporal("voce ja digitou essa letra")
                else:
                    escrever_textostemporal("voce errou , tente novamente")
                    erros = erros + 1
                    escrever_digitadas()
                    digitadas.sort()
                    tronco(erros)
    else:
        escrever_textostemporal("Bugou , tente novamente")
if erros == 6:
     escrever_textostemporal("Voce perdeu!!")
     escrever_textocomtitulo2("A palavra era:",palavra)
     sleep(2)
     window.bye()
else:
     escrever_textostemporal("Voce ganhou!")
     sleep(2)
     window.bye()
window.exitonclick()
