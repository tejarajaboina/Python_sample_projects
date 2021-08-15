import turtle

def draw_hex(a):
    
    for i in range(1,10):
        a.forward(50)
        a.right(45)
 
def draw_shape():
    window=turtle.Screen()
    window.bgcolor('red')

    s=turtle.Turtle()
    s.shape('turtle')
   # s.color('black')
    s.speed(100000000000)

    

    for j in range(1,109):
        s.color('blue')
        s.forward(100)
        s.right(30)
        s.forward(100)
        s.right(120)
        s.forward(100)


    window.exitonclick()

draw_shape()  
