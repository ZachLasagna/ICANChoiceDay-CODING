import turtle

wn = turtle.Screen()
wn.title("CookieClicker")
wn.bgcolor("black")

wn.register_shape("c:\\Users\\iCan Student\\Downloads\\cookie.gif")

cookie = turtle.Turtle()
cookie.shape("c:\\Users\\iCan Student\\Downloads\\cookie.gif")
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(10, 150)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x,  y):
    global clicks
    clicks += 100
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
cookie.onclick(clicked)

wn.mainloop()