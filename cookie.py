import turtle
import time
import threading

wn = turtle.Screen()
wn.title("CookieClicker")
wn.bgcolor("black")

wn.register_shape("c:\\Users\\iCan Student\\Downloads\\cookie.gif")
wn.register_shape("c:\\Users\\iCan Student\\Downloads\\cursor.gif")
wn.register_shape("c:\\Users\\iCan Student\\Downloads\\grandma.gif")

cookie = turtle.Turtle()
cookie.shape("c:\\Users\\iCan Student\\Downloads\\cookie.gif")
cookie.speed(0)

cursor = turtle.Turtle()
cursor.penup()
cursor.speed(10000)
cursor.goto(400, 0)
cursor.shape("c:\\Users\\iCan Student\\Downloads\\cursor.gif")

granny = turtle.Turtle()
granny.penup()
granny.speed(10000)
granny.goto(-400, 0)
granny.shape("c:\\Users\\iCan Student\\Downloads\\grandma.gif")

clicks = 0
increase_numbers = 1
increase_number_time = 0
cursor_cost = 50
granny_cost = 100
cursors_count = 0
granny_count = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.speed(1000)
pen.goto(10, 150)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.color("white")
pen2.penup()
pen2.speed(1000)
pen2.goto(400, -150)
pen2.write(f"Cursors: {cursors_count}", align="center", font=("Courier New", 32, "normal"))

pen3 = turtle.Turtle()
pen3.hideturtle()
pen3.color("white")
pen3.penup()
pen3.speed(1000)
pen3.goto(-400, -150)
pen3.write(f"Grannys: {granny_count}", align="center", font=("Courier New", 32, "normal"))

pen4 = turtle.Turtle()
pen4.hideturtle()
pen4.color("lime")
pen4.penup()
pen4.speed(1000)
pen4.goto(-400, 150)
pen4.write(f"Grannys cost: {granny_cost}", align="center", font=("Courier New", 32, "normal"))

pen5 = turtle.Turtle()
pen5.hideturtle()
pen5.color("lime")
pen5.penup()
pen5.speed(1000)
pen5.goto(400, 150)
pen5.write(f"Cursors cost: {cursor_cost}", align="center", font=("Courier New", 32, "normal"))



def clicked(x,  y):
    global clicks
    clicks += increase_numbers
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
    

cookie.onclick(clicked)

def clicker(x, y):
        global clicks
        global increase_numbers
        global cursors_count
        global cursor_cost
        if clicks >= cursor_cost: 
            clicks -= cursor_cost
            increase_numbers += 1 
            cursors_count += 1    
            cursor_cost += 50
           
            pen.clear()
            pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))      
            
            pen2.clear()
            pen2.write(f"Cursors: {cursors_count}", align="center", font=("Courier New", 32, "normal"))   
            
            pen5.clear()  
            pen5.write(f"Cursors cost: {cursor_cost}", align="center", font=("Courier New", 32, "normal"))      

cursor.onclick(clicker)

def time_bla_bla():
    global increase_number_time
    global clicks
    while True:
         time.sleep(1)
         clicks += increase_number_time
         pen.clear()
         pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))  
def cricker(x, y):
        global clicks
        global increase_number_time
        global granny_count
        global granny_cost
        if clicks >= granny_cost:
            clicks -= granny_cost
            increase_number_time += 1
            granny_count += 1
            granny_cost += 100
            
            pen.clear()
            pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))     
            
            pen3.clear()
            pen3.write(f"Grannys: {granny_count}", align="center", font=("Courier New", 32, "normal")) 
            
            pen4.clear()   
            pen4.write(f"Grannys cost: {granny_cost}", align="center", font=("Courier New", 32, "normal"))      

granny.onclick(cricker)

t1 = threading.Thread(target=time_bla_bla, name='t1')
t1.start()

wn.mainloop()