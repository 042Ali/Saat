import turtle
from datetime import datetime


months = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avqust",
 "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]


screen = turtle.Screen()
screen.setup(500,500,0,0)
screen.screensize(480,480, bg="#aaa")
screen.tracer(0)

tisbaga = turtle.Turtle()

def draw_lines(length,rotation):
    tisbaga.penup()
    tisbaga.home()
    tisbaga.color("black")
    tisbaga.right(rotation)
    tisbaga.forward(170)
    tisbaga.pendown()
    tisbaga.forward(length)
    tisbaga.penup()

def draw_watchface():
    for i in range(0, 360, 30):
        draw_lines(20, i)

    for i in range(0, 360, 6):
        draw_lines(10, i)  

def draw_hands(length, rotation):
    tisbaga.penup()
    tisbaga.home()          
    tisbaga.right(1 * rotation + 90 * 3)          
    tisbaga.pendown()          
    tisbaga.forward(length)          
    tisbaga.penup()          

def draw_time(time):
    h= time.hour
    m= time.minute
    s= time.second
    day= time.day
    month= time.month
    year= time.year
    
    tisbaga.penup()
    tisbaga.color("white")
    tisbaga.goto(-220,-220)
    tisbaga.pendown()
    formatted_time = f"{day}, {months[month-1]},{year} {h}:{m}:{s}"   
    tisbaga.write(formatted_time, move=False,align="left",font=("Arial",16,"normal")) 
    tisbaga.penup()

def draw_clock(h,m,s):
    draw_watchface()
    tisbaga.pensize(5)
    tisbaga.color("blue")
    draw_hands(100, (h + m / 60)*30)
    tisbaga.pensize(3)
    tisbaga.color("red")
    draw_hands(130,m*6)
    tisbaga.color("green")
    tisbaga.pensize(1)
    draw_hands(160,s*6)


while True:
    time= datetime.now()
    hours = time.hour
    minutes = time.minute
    seconds= time.second    
    tisbaga.hideturtle()

    tisbaga.clear()
    draw_time(time)
    draw_clock(hours,minutes,seconds)
    screen.update()

