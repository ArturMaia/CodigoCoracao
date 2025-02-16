import turtle

def exibir_mensagem():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.setup(width=800, height=600)
    t = turtle.Turtle()
    t.hideturtle()  
    t.color("red")
    t.penup()
    t.goto(0, 150) 
    t.pendown()
    t.write("i love my girlfriend", align="center", font=("Times New Roman", 12, "italic"))  
    turtle.done()

def draw_heart():
    heart = turtle.Turtle()  
    heart.speed(10)
    heart.penup()
    heart.goto(0, -100) 
    heart.pendown()
    
    heart.begin_fill()
    heart.color("pink")

    heart.left(50)
    heart.forward(200) 
    heart.circle(80, 200) 
    heart.right(140)
    heart.circle(80, 200) 
    heart.forward(200) 

    heart.end_fill()
    heart.hideturtle()
    
draw_heart()

exibir_mensagem()

turtle.done()
