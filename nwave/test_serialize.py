import unittest

from .serialize import JsonSerializer
from .scene import Scene

class Test_Serialize(unittest.TestCase):

    def test_should_serialize_to_empty_json_when_scene_is_empty(self):
        radius=250
        scene = Scene(background_color=[102, 204, 255])
        json = JsonSerializer().serialize_scene(scene)
        self.assertEqual(json, '{"scene":[]}')
