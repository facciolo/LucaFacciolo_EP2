import turtle
import time               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("Black")
window.title("Forca")

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(1000)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(-100,0)
tartaruga.pendown()
tartaruga.color("Red")
angulo = 90
dist = 150
dist2 = 50
def cabeça():
    tartaruga.penup()
    tartaruga.setpos(-50,200)
    tartaruga.pendown()
    tartaruga.rt(90)
    tartaruga.circle(20)
def tronco():
    tartaruga.penup()
    tartaruga.setpos(-50,160)
    tartaruga.pendown()
    tartaruga.rt(270)
    tartaruga.forward(65)
def braço_esquerdo():
    tartaruga.penup()
    tartaruga.setpos(-50,140)
    tartaruga.pendown()
    tartaruga.rt(260)
    tartaruga.forward(30)
def braço_direito():
    tartaruga.penup()
    tartaruga.setpos(-50,140)
    tartaruga.pendown()
    tartaruga.rt(230)
    tartaruga.forward(30)
def perna_esquerda():
    tartaruga.penup()
    tartaruga.setpos(-50,95)
    tartaruga.pendown()
    tartaruga.rt(170)
    tartaruga.forward(50)
    
def perna_direita():
    tartaruga.penup()
    tartaruga.setpos(-50,95)
    tartaruga.pendown()
    tartaruga.rt(110)
    tartaruga.forward(50)
def escrever_digitadas(a):
    listadigitadas = []
    listadigitadas.append(a)
    tartaruga.penup()
    tartaruga.setpos(100,-200)
    tartaruga.pendown()
    tartaruga.write(listadigitadas,font = ("arial",15,"normal"))
def escrever_textocomtitulo(titulo,conteudo):
    tartaruga.penup()
    tartaruga.setpos(0,-100)
    tartaruga.pendown()
    tartaruga.write(titulo,font = ("arial",20,"normal"))
    tartaruga.penup()
    tartaruga.setpos(0,-80)
    tartaruga.write(conteudo,font = ("arial",15,"normal"))
def escrever_textos(a):
    tartaruga.penup()
    tartaruga.setpos(75,-100)
    tartaruga.write(a,font = ("arial",15,"normal"))
    tartaruga.clear()
def escrever_textostemporal(a):
    tartaruga.penup()
    tartaruga.setpos(0,-100)
    tartaruga.write(a,font = ("arial",15,"normal"))
    time.sleep(3)
    tartaruga.clear()
    
    
    



for i in range(1):
    tartaruga.pensize(5)
    tartaruga.left(90)  # Vira o angulo pedido
    tartaruga.forward(250) # Avança a distancia pedida
    tartaruga.hideturtle()
    
for i in range(2):
    tartaruga.left(270)
    tartaruga.forward(50)
    tartaruga.hideturtle()
cabeça()
tronco()
braço_esquerdo()
braço_direito()
perna_esquerda()
perna_direita()
escrever_digitadas("a")
escrever_digitadas("d")

window.exitonclick()