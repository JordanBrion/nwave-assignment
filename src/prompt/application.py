from .states import MainMenuState
from ..scene import Scene
from ..entities import Disk

class PromptApplication:
    def __init__(self) -> None:
        self.scene = self.make_scene_with_default_values()
        self.state = MainMenuState()

    def make_scene_with_default_values(self):
        radius=250
        scene = Scene(background_color=[102, 204, 255])
        scene.add_entity(Disk(radius=radius, position=[0, 216], color=[255, 0, 0]))
        scene.add_entity(Disk(radius=radius, position=[-250, -216], color=[0, 255, 0]))
        scene.add_entity(Disk(radius=radius, position=[250, -216], color=[0, 0, 255]))
        return scene

    def run(self):
        while self.state is not None:
            self.state = self.state.display_prompt(self.scene)