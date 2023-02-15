import unittest

from .serialize import JsonSerializer, XmlSerializer
from .scene import Scene
from .entities import Disk

class Test_Serialize(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.disk_radius=250

    def assertGoldenJson(self, json, golden_fullpath):
        file = open(golden_fullpath, "r")
        expected_json = file.read()

        self.assertEqual(json, expected_json)

    def test_should_serialize_to_empty_json_when_scene_is_empty(self):
        scene = Scene(background_color=[102, 204, 255])
        
        json = JsonSerializer().serialize_scene(scene)
        
        self.assertEqual(json, '{"scene":[]}')

    def test_should_serialize_to_3_disks_in_json_when_scene_has_3_disks(self):
        scene = Scene(background_color=[102, 204, 255])
        scene.add_entity(Disk(radius=self.disk_radius, position=[0, 216], color=[255, 0, 0]))
        scene.add_entity(Disk(radius=self.disk_radius, position=[-250, -216], color=[0, 255, 0]))
        scene.add_entity(Disk(radius=self.disk_radius, position=[250, -216], color=[0, 0, 255]))
        
        json = JsonSerializer().serialize_scene(scene)

        self.assertGoldenJson(json, golden_fullpath="nwave/golden/three_disks.json")

    def test_should_serialize_to_empty_xml_when_scene_is_empty(self):
        scene = Scene(background_color=[102, 204, 255])
        
        xml = XmlSerializer().serialize_scene(scene)
        
        self.assertEqual(xml, '<Scene></Scene>')