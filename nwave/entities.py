# The Disk entity is displayed within the Viewport.
# If you want to add a new entity:
# 1/ define the new class and its attributes
# 2/ override render() + serialize() methods
# 3/ add the corresponding methods within the renderer and serialize classes
# 4/ at that point, you should be able to add instances of that new entity within the Scene

class Disk:
    def __init__(self, radius, position, color) -> None:
        self.radius = radius
        self.position = position
        self.color = color

    def render(self, renderer):
        renderer.render_disk(self)

    def serialize(self, serializer):
        return serializer.serialize_disk(self)