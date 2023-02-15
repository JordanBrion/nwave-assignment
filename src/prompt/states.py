from enums import MainMenuStateEnum, SerializeSceneStateEnum
from ..serialize import JsonSerializer, XmlSerializer

class BasePromptApplicationState:
    def __init__(self) -> None:
        pass

    def display_prompt(self, scene):
        #try:
        #    return self.display_prompt_impl()
        #except:
        #    self.print_error()
        return self.display_prompt_impl(scene)

    def display_prompt_impl(self, scene):
        pass

    def ask_user_choice(self):
        return int(input("What do you want to do ? "))

    def print_error(self):
        print("This is an invalid value.")

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
            serialize_to_file=MainMenuStateEnum.SERIALIZE_TO_FILE,
            export_to_image=MainMenuStateEnum.EXPORT_TO_IMAGE,
            quit=MainMenuStateEnum.QUIT))

        match self.ask_user_choice():
            case MainMenuStateEnum.ADD_NEW_DISK:
                print("ADD_NEW_DISK")
            case MainMenuStateEnum.SERIALIZE_TO_FILE:
                return SerializeSceneState()
            case MainMenuStateEnum.EXPORT_TO_IMAGE:
                print("EXPORT_TO_IMAGE")
            case MainMenuStateEnum.QUIT:
                return None

        return self