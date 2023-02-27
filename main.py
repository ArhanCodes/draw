t.write("red = r, blue = b, green = g, white = w, black = k, yellow = y, penup = u, pendown = d, increase_pensize = i and decrease_pensize = j", align = "left", font = ('Arial', 10, 'bold'))
t.penup()
t.goto(0, 0)
t.pendown()

size = 5
def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y)) # start drawing with the help of the mouse
    t.goto(x, y)
    t.ondrag(dragging)

def clickright(x, y):
    t.clear()
    
def penup():
    t.penup()

def pendown():
    t.pendown()

def red():
    t.color("red")

def blue():
    t.color("blue")

def green():
    t.color("green")

def white():
    t.color("white")

def black():
    t.color("black")

def yellow():
    t.color("yellow")

def increase_pensize():
    t.pensize(size+5)

def decrease_pensize():
    t.pensize(size-5)

s.listen()
t.ondrag(dragging)
s.onkey(penup, "u")
s.onkey(pendown, "d")
s.onkey(red, "r")
s.onkey(blue, "b")
s.onkey(green, "g")
s.onkey(white, "w")
s.onkey(black, "k")
s.onkey(yellow, "y")
s.onkey(increase_pensize, "i")
s.onkey(decrease_pensize, "j")
s.onscreenclick(clickright, 3)
s.mainloop()
