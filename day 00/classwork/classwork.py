from turtle import *

shape("turtle")

speed(12) 
width(12) 

color("blue")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill() 

forward(70)
color("brown") 
begin_fill()
left(90)
forward(120)

right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()
color("blue") 
left(220)

color("red")
begin_fill()
forward(150)


right(262)
forward(155)
end_fill()

color("lightblue")
begin_fill()
penup()
goto(170,90)
pendown()
right(48)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
end_fill()

begin_fill()
penup()
goto(50,90)
pendown()
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
end_fill()

penup()
goto(0,0)
pendown()

penup()
begin_fill()
color("green")
goto(0,-5)
pendown()
right(90)
forward(470)
penup()
goto(0,-5)
pendown()
left(180)
forward(460)
right(90)

forward(300)
right(90)

forward(928)
right(90)
forward(300)
end_fill()

color("yellow")
penup() 
goto(-120,300)
pendown()

circle(70)
begin_fill()

color("brown")
penup()
goto(-400,0)
pendown()
forward(101)
begin_fill()
color("green")
left(90)
forward(20)
left(180)
forward(40)

left(45)
forward(30)
left(45)
forward(30)

left(45)
forward(30)

left(45)
forward(30)

left(45)
forward(30)

left(45)
forward(30)

left(45)
forward(30)
end_fill()
penup()
goto(0,0)
pendown()



exitonclick()