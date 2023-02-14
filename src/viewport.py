
class Viewport:
    def __init__(self, renderer):
        self.__renderer = renderer

    def render(self, scene):
        for entity in scene.entities():
            entity.render(self.__renderer)
        self.__renderer.done()