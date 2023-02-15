from .states import MainMenuState

class PromptApplication:
    def __init__(self) -> None:
        self.state = MainMenuState()

    def run(self):
        while self.state is not None:
            self.state = self.state.display_prompt()