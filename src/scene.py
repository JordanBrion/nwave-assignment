class Scene:
    def __init__(self, background_color) -> None:
        self.__background_color = background_color
        self.__entities = []

    def add_entity(self, entity) -> None:
        self.__entities.append(entity)

    def entities(self):
        return self.__entities