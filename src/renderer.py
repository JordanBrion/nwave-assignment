import turtle

class Renderer:
    def __init__(self):
        pass

    def setup(self, width, height, background_color):
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.colormode(255)
        turtle.tracer(False)
        self.canvas = turtle.Turtle()
        self.screen.bgcolor(background_color[0], background_color[1], background_color[2])

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
