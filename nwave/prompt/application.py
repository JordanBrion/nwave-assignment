from .states import MainMenuState
from ..scene import Scene
from ..entities import Disk

class PromptApplication:
    def __init__(self) -> None:
        self.scene = self.make_scene_with_default_values()
        self.current_state = MainMenuState()

    def make_scene_with_default_values(self):
        radius=250
        scene = Scene(background_color=[102, 204, 255])
        scene.add_entity(Disk(radius=radius, position=[0, 216], color=[255, 0, 0]))
        scene.add_entity(Disk(radius=radius, position=[-250, -216], color=[0, 255, 0]))
        scene.add_entity(Disk(radius=radius, position=[250, -216], color=[0, 0, 255]))
        return scene

    def run(self):
        while self.current_state is not None:
            self.current_state = self.current_state.display_prompt(self.scene)