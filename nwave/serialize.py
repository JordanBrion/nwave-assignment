import json
from dict2xml import dict2xml

class JsonSerializer:
    def __init__(self) -> None:
        pass

    def serialize_scene(self, scene):
        start_of_json = """{"scene":["""
        end_of_json = """]}"""

        if len(scene.entities()) == 0:
            return start_of_json + end_of_json
        else:
            json = ""
            entities = scene.entities()
            for entity in entities[:-1]:
                json += entity.serialize(self) + ","
            json += entities[-1:][0].serialize(self)
            return start_of_json + json + end_of_json

    def serialize_disk(self, disk):
        return json.dumps(disk.__dict__ | { "type": "DISK" })

class XmlSerializer:
    def __init__(self) -> None:
        pass

    def serialize_scene(self, scene):
        xml = ""
        for entity in scene.entities():
            xml += entity.serialize(self)
        
        xml = self.wrap(scene.__class__.__name__, xml)

        return xml

    def serialize_disk(self, disk):
        return self.wrap(disk.__class__.__name__, dict2xml(disk.__dict__))

    def wrap(self, root_tag_name, xml):
        return "<{root_tag}>{xml_body}</{root_tag}>".format(root_tag=root_tag_name, xml_body=xml)
