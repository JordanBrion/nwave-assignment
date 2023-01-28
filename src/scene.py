class Scene:
    def __init__(self) -> None:
        self.__background_color = []
        self.__drawables = []

    def add_drawable(self, drawable) -> None:
        self.__drawables.append(drawable)