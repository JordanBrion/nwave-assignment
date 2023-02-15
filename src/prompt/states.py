from enum import IntEnum

class PromptApplicationState:
    def __init__(self) -> None:
        pass

    def print_error(self):
        print("This is an invalid value.")

class MainMenuStateEnum(IntEnum):
    ADD_NEW_DISK = 1
    SERIALIZE_TO_FILE = 2
    EXPORT_TO_IMAGE = 3

class MainMenuState(PromptApplicationState):
    def __init__(self) -> None:
        pass

    def display_prompt(self):
        print("""
            --- NWAVE ASSIGNMENT - CONSOLE MODE ---
            [{new_disk}] Add new disk
            [{serialize_to_file}] Serialize to file
            [{export_to_image}] Export to image
        """.format(
            new_disk=MainMenuStateEnum.ADD_NEW_DISK, 
            serialize_to_file=MainMenuStateEnum.SERIALIZE_TO_FILE,
            export_to_image=MainMenuStateEnum.EXPORT_TO_IMAGE))

        try:
            match int(input("What do you want to do ? ")):
                case MainMenuStateEnum.ADD_NEW_DISK:
                    print("ADD_NEW_DISK")
                case MainMenuStateEnum.SERIALIZE_TO_FILE:
                    print("SERIALIZE_TO_FILE")
                case MainMenuStateEnum.EXPORT_TO_IMAGE:
                    print("EXPORT_TO_IMAGE")
                case _:
                    self.print_error()
        except:
            self.print_error()