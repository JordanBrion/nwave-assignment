import json
from dict2xml import dict2xml

class JsonSerializer:
    def __init__(self) -> None:
        pass

    def serialize_scene(self, scene):
        json = """
            {
                "scene" : [
        """
        for entity in scene.entities():
            json += entity.serialize(self) + ","
        
        json += """
                ]
            }
        """
        return json

    def serialize_disk(self, disk):
        return json.dumps(disk.__dict__ | { "type": "DISK" })

class XmlSerializer:
    def __init__(self) -> None:
        pass

    def serialize_scene(self, scene):
        xml = ""
        for entity in scene.entities():
            xml += entity.serialize(self)
        
        xml = self.wrap("Scene", xml)

        return xml

    def serialize_disk(self, disk):
        return self.wrap(disk.__class__.__name__, dict2xml(disk.__dict__))

    def wrap(self, root_tag_name, xml):
        return "<{root_tag}>{xml_body}</{root_tag}>".format(root_tag=root_tag_name, xml_body=xml)
