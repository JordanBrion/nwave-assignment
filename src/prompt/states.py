from enum import IntEnum

class MainMenuStateEnum(IntEnum):
    ADD_NEW_DISK = 1
    SERIALIZE_TO_FILE = 2
    EXPORT_TO_IMAGE = 3
    QUIT = 4

class SerializeSceneStateEnum(IntEnum):
    XML = 1
    JSON = 2

class BasePromptApplicationState:
    def __init__(self) -> None:
        pass

    def display_prompt(self):
        try:
            return self.display_prompt_impl()
        except:
            self.print_error()

    def display_prompt_impl(self):
        pass

    def ask_user_choice(self):
        return int(input("What do you want to do ? "))

    def print_error(self):
        print("This is an invalid value.")

class SerializeSceneState(BasePromptApplicationState):
    def __init__(self) -> None:
        pass

    def display_prompt_impl(self):
        print("""
            Select the serialization format:
            [{xml}] XML
            [{json}] JSON
        """.format(
            xml=SerializeSceneStateEnum.XML, 
            json=SerializeSceneStateEnum.JSON))

        match self.ask_user_choice():
            case SerializeSceneStateEnum.XML:
                return MainMenuState()
            case SerializeSceneStateEnum.JSON:
                return MainMenuState()
        
        return self

class MainMenuState(BasePromptApplicationState):
    def __init__(self) -> None:
        pass

    def display_prompt_impl(self):
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