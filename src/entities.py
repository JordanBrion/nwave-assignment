class Disk:
    def __init__(self, radius, position, color) -> None:
        self.radius = radius
        self.position = position
        self.color = color

    def render(self, renderer):
        renderer.render_disk(self)

    def serialize(self, serializer):
        serializer.serialize_disk(self)