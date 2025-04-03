from command_processing import CommandProcessing
from openai_agent import OpenAIAgent
from speech_processing import SpeechProcessing
from todo_manager import TodoManager


class MainApp:
    def __init__(self) -> None:
        """Initialize the MainApp with necessary components."""
        self.command_processor = CommandProcessing()
        self.openai_agent = OpenAIAgent()
        self.speech_processor = SpeechProcessing()
        self.todo_manager = TodoManager()

    def run(self) -> None:
        """Run the main loop to listen for voice commands."""
        while True:
            command = self.speech_processor.listen()
            # Process the command here if needed


if __name__ == "__main__":
    app = MainApp()
    app.run()