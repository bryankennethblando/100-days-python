import turtle

# Create a screen
screen = turtle.Screen()
screen.title("My First Turtle Program")

# Create a turtle instance
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

color = 'red'
for steps in range(50):
    if steps == 45:
       color = 'black'

    t.color(color)
    t.forward(steps)
    t.right(70)
    t.circle(70)
    t.circle(10)
    t.circle(30)
    t.circle(50)
    t.left(10)

# Keep the window open
turtle.done()


