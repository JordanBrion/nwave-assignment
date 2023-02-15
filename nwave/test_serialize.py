import unittest
import os
from PIL import Image
import imagehash

from .serialize import JsonSerializer, XmlSerializer
from .scene import Scene
from .entities import Disk
from .viewport import Viewport
from .filewriter import FileWriter
from .renderer import Renderer
import uuid
import tempfile

class NwaveTestCase(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.disk_radius=250

    def make_scene_with_3_disks(self):
        scene = Scene(background_color=[102, 204, 255])
        scene.add_entity(Disk(radius=self.disk_radius, position=[0, 216], color=[255, 0, 0]))
        scene.add_entity(Disk(radius=self.disk_radius, position=[-250, -216], color=[0, 255, 0]))
        scene.add_entity(Disk(radius=self.disk_radius, position=[250, -216], color=[0, 0, 255]))
        return scene

    def get_golden_directory(self):
        return os.path.join("nwave", "golden")

    def assert_with_golden_file(self, json, golden_fullpath):
        with open(golden_fullpath, "r") as f:
            expected_json = f.read()
            self.assertEqual(json, expected_json)
class Test_Serialize(NwaveTestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def get_serialize_golden_directory(self):
        return os.path.join(self.get_golden_directory(), "serialize")        

    def test_should_serialize_to_empty_json_when_scene_is_empty(self):
        empty_scene = Scene(background_color=[102, 204, 255])
        
        json = JsonSerializer().serialize_scene(empty_scene)
        
        self.assertEqual(json, '{"scene":[]}')

    def test_should_serialize_to_3_disks_in_json_when_scene_has_3_disks(self):
        json = JsonSerializer().serialize_scene(self.make_scene_with_3_disks())

        self.assert_with_golden_file(
            json, 
            golden_fullpath=os.path.join(self.get_serialize_golden_directory(), "three_disks.json")
        )

    def test_should_serialize_to_empty_xml_when_scene_is_empty(self):
        empty_scene = Scene(background_color=[102, 204, 255])
        
        xml = XmlSerializer().serialize_scene(empty_scene)
        
        self.assertEqual(xml, '<Scene></Scene>')

    def test_should_serialize_to_3_disks_in_xml_when_scene_has_3_disks(self):        
        json = XmlSerializer().serialize_scene(self.make_scene_with_3_disks())

        self.assert_with_golden_file(
            json, 
            golden_fullpath=os.path.join(self.get_serialize_golden_directory(), "three_disks.xml")
        )

class Test_Renderer(NwaveTestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def get_renderer_golden_directory(self):
        return os.path.join(self.get_golden_directory(), "renderer")        

    def get_fullpath_temporary_image(self, image_extension):
        return os.path.join(tempfile.gettempdir(), str(uuid.uuid4()) + image_extension)

    def assert_image_to_golden(self, image_fullpath, golden_fullpath):
        _, file_extension = os.path.splitext(image_fullpath)
        _, golden_file_extension = os.path.splitext(golden_fullpath)

        self.assertEqual(file_extension, golden_file_extension)

        with Image.open(image_fullpath) as image:
            with Image.open(golden_fullpath) as golden_image:
                image_hash = imagehash.average_hash(golden_image)
                golden_hash = imagehash.average_hash(image)
                self.assertEqual(image_hash, golden_hash)

    def test_should_be_the_same_as_the_golden_png(self):
        png_writer = FileWriter(self.get_fullpath_temporary_image(".png"))
        renderer = Renderer(writer=png_writer)
        viewport = Viewport(width=1100, height=1000, renderer=renderer)
        viewport.render(self.make_scene_with_3_disks())

        self.assert_image_to_golden(
            png_writer.fullpath, 
            os.path.join(self.get_renderer_golden_directory(), "three_disks.png")
        )

    def test_should_be_the_same_as_the_golden_jpg(self):
        png_writer = FileWriter(self.get_fullpath_temporary_image(".jpg"))
        renderer = Renderer(writer=png_writer)
        viewport = Viewport(width=1100, height=1000, renderer=renderer)
        viewport.render(self.make_scene_with_3_disks())

        self.assert_image_to_golden(
            png_writer.fullpath, 
            os.path.join(self.get_renderer_golden_directory(), "three_disks.jpg")
        )