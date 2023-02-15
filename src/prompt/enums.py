from enum import IntEnum

class MainMenuStateEnum(IntEnum):
    ADD_NEW_DISK = 1
    SERIALIZE_TO_FILE = 2
    EXPORT_TO_IMAGE = 3
    QUIT = 4

class SerializeSceneStateEnum(IntEnum):
    XML = 1
    JSON = 2