import turtle

class Renderer:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(800, 800)
        self.screen.colormode(255)
        turtle.tracer(False)
        self.canvas = turtle.Turtle()

    def render_disk(self, disk):
        self.canvas.setposition([disk.position[0], disk.position[1] - disk.radius])
        self.canvas.pendown()
        self.canvas.fillcolor(disk.color[0], disk.color[1], disk.color[2])
        self.canvas.begin_fill()
        self.canvas.circle(radius=disk.radius)
        self.canvas.end_fill()
        self.canvas.penup()

    def done(self):
        turtle.done()
