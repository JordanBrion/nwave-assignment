from .enums import MainMenuStateEnum, SerializeSceneStateEnum, SaveSceneToImageStateEnum
from ..serialize import JsonSerializer, XmlSerializer
from ..filewriter import FileWriter
from ..renderer import Renderer
from ..viewport import Viewport
from ..entities import Disk
from .fs import get_unique_image_fullpath
import os

class BasePromptApplicationState:
    def __init__(self) -> None:
        pass

    def display_prompt(self, scene):
        try:
            return self.display_prompt_impl(scene)
        except:
            self.print_error()
            return MainMenuState()
          
    def display_prompt_impl(self, scene):
        pass

    def ask_user_choice(self, msg = "What do you want to do ? "):
        return int(input(msg))

    def print_error(self):
        print("This is an invalid value.")

class AddNewDiskState(BasePromptApplicationState):
    def __init__(self) -> None:
        pass

    def display_prompt_impl(self, scene):
        print("Enter the location of the sphere. (0, 0) is at the center.")
        x = self.ask_user_choice("[X] ? ")
        y = self.ask_user_choice("[Y] ? ")

        scene.add_entity(Disk(radius=250, position=[x, y], color=[0, 0, 255]))

        return MainMenuState()

class SerializeSceneState(BasePromptApplicationState):
    def __init__(self) -> None:
        pass

    def display_prompt_impl(self, scene):
        print("""
            Select the serialization format:
            [{xml}] XML
            [{json}] JSON
        """.format(
            xml=SerializeSceneStateEnum.XML, 
            json=SerializeSceneStateEnum.JSON))

        match self.ask_user_choice():
            case SerializeSceneStateEnum.XML:
                self.serialize_to_xml(scene)
                return MainMenuState()
            case SerializeSceneStateEnum.JSON:
                self.serialize_to_json(scene)
                return MainMenuState()
        
        return self        

    def serialize_to_xml(self, scene):
        print(XmlSerializer().serialize_scene(scene))

    def serialize_to_json(self, scene):
        print(JsonSerializer().serialize_scene(scene))

class SaveSceneToImageState(BasePromptApplicationState):
    def __init__(self) -> None:
        pass

    def display_prompt_impl(self, scene):
        print("""
            Select the image extension:
            [{png}] .PNG
            [{jpg}] .JPG
        """.format(
            png=SaveSceneToImageStateEnum.PNG, 
            jpg=SaveSceneToImageStateEnum.JPG))

        match self.ask_user_choice():
            case SaveSceneToImageStateEnum.PNG:
                self.save_image(scene, get_unique_image_fullpath(".png"))
                return MainMenuState()
            case SaveSceneToImageStateEnum.JPG:
                self.save_image(scene, get_unique_image_fullpath(".jpg"))
                return MainMenuState()
        
        return self        

    def save_image(self, scene, fullpath):
        writer = FileWriter(fullpath)
        renderer = Renderer(writer=writer)
        viewport = Viewport(width=1100, height=1000, renderer=renderer) # TODO store dimensions in variables
        viewport.render(scene)
        print("Image saved to " + fullpath)

class MainMenuState(BasePromptApplicationState):
    def __init__(self) -> None:
        pass

    def display_prompt_impl(self, _scene):
        print("""
            --- NWAVE ASSIGNMENT - CONSOLE MODE ---
            [{add_new_disk}] Add new disk
            [{serialize}] Serialize
            [{save_to_image}] Save to image
            [{quit}] Quit
        """.format(
            add_new_disk=MainMenuStateEnum.ADD_NEW_DISK, 
            serialize=MainMenuStateEnum.SERIALIZE,
            save_to_image=MainMenuStateEnum.SAVE_TO_IMAGE,
            quit=MainMenuStateEnum.QUIT))

        match self.ask_user_choice():
            case MainMenuStateEnum.ADD_NEW_DISK:
                return AddNewDiskState()
            case MainMenuStateEnum.SERIALIZE:
                return SerializeSceneState()
            case MainMenuStateEnum.SAVE_TO_IMAGE:
                return SaveSceneToImageState()
            case MainMenuStateEnum.QUIT:
                return None

        return self