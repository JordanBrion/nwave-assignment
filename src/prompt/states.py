from .enums import MainMenuStateEnum, SerializeSceneStateEnum, SaveSceneToImageStateEnum
from ..serialize import JsonSerializer, XmlSerializer
from ..filewriter import FileWriter
from ..renderer import Renderer
from ..viewport import Viewport
from ..entities import Disk

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
                self.save_image(scene, "/Users/jordanbrion/Downloads/bbb1.png") # TODO file path
                return MainMenuState()
            case SaveSceneToImageStateEnum.JPG:
                self.save_image(scene, "/Users/jordanbrion/Downloads/bbb1.jpg") # TODO file path
                return MainMenuState()
        
        return self        

    def save_image(self, scene, path):
        writer = FileWriter(path)
        renderer = Renderer(writer=writer)
        viewport = Viewport(width=1100, height=1000, renderer=renderer) # TODO store dimensions in consts
        viewport.render(scene)

class MainMenuState(BasePromptApplicationState):
    def __init__(self) -> None:
        pass

    def display_prompt_impl(self, _scene):
        print("""
            --- NWAVE ASSIGNMENT - CONSOLE MODE ---
            [{new_disk}] Add new disk
            [{serialize_to_file}] Serialize to file
            [{export_to_image}] Export to image
            [{quit}] Quit
        """.format(
            new_disk=MainMenuStateEnum.ADD_NEW_DISK, 
            serialize_to_file=MainMenuStateEnum.SERIALIZE,
            export_to_image=MainMenuStateEnum.SAVE_TO_IMAGE,
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