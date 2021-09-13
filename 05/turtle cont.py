import turtle as t

def Right():
    t.setheading(0)
    t.forward(50)
    
def Up():
    t.setheading(90)
    t.forward(50)
    
def Left():
    t.setheading(180)
    t.forward(50)

def Down():
    t.setheading(270)
    t.forward(50)

def Reset():
    t.goto(0,0)
    t.clear()
    
    
t.speed(0)
t.onkeypress(Up,"w")
t.onkeypress(Left,"a")
t.onkeypress(Down,"s")
t.onkeypress(Right,"d")
t.onkeypress(Up,"W")
t.onkeypress(Left,"A")
t.onkeypress(Down,"S")
t.onkeypress(Right,"D")
t.onkeypress(Reset,"Escape")
t.listen()

