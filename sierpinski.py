import turtle
t= turtle.Turtle()
#t.pu()
#t.ht()
t.right(30)
t.shape('triangle')
t.color('green')
t.speed(1)

def sierpiski(size,order):
    if order ==0:
        t.stamp()
    else:
        
        for i in range(0,3):
            t.forward(size)
            sierpiski(size/2,order-1)
            t.backward(size)
            t.left(120)
sierpiski(100,3)
