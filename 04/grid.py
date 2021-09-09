import turtle as t

index = 0
index2 = 0
t.penup()
t.goto(-200,-200)
while (index != 500):
    t.penup()
    while(index2 != 500):
        t.goto(index-200,index2-200)
        t.pendown()
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        index2 += 100
    index += 100
    index2 = 0
    
    
t.exitonclick()
