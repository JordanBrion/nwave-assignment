import json
from dict2xml import dict2xml

class BaseSerializer:
    def serialize_scene(self, scene):
        pass
class JsonSerializer(BaseSerializer):
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
        print(json)

    def serialize_disk(self, disk):
        return json.dumps(disk.__dict__ | { "type": "DISK" })

class XmlSerializer(BaseSerializer):
    def __init__(self) -> None:
        pass

    def serialize_disk(self, disk):
        return self.wrap(disk.__class__.__name__, dict2xml(disk.__dict__))

    def wrap(self, root_tag_name, xml):
        return "<{root_tag}>{xml_body}</{root_tag}>".format(root_tag=root_tag_name, xml_body=xml)
