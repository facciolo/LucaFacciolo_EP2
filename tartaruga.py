import turtle               # Usa a biblioteca de turtle graphics
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
window.exitonclick()
