
class Viewport:
    def __init__(self, width, height, renderer):
        self.__renderer = renderer
        self.width = width
        self.height = height
        
    def render(self, scene):
        self.__renderer.setup(self.width, self.height)
        for entity in scene.entities():
            entity.render(self.__renderer)
        self.__renderer.done()