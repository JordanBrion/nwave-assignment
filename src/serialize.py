import json

class JsonSerializer:
    def __init__(self) -> None:
        pass

    def serialize_scene(self, scene):
        for entity in scene.entities():
            entity.serialize(self)

    def serialize_disk(self, disk):
        return json.dumps(disk.__dict__)
