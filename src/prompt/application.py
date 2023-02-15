from .states import MainMenuState

class PromptApplication:
    def __init__(self) -> None:
        self.state = MainMenuState()

    def run(self):
        self.state.display_prompt()