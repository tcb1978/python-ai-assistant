from command_processing import CommandProcessing
from openai_agent import OpenAIAgent
from speech_processing import SpeechProcessing
from todo_manager import TodoManager


class MainApp:
  def __init__(self):
        self.command_processor = CommandProcessing()
        self.openai_agent = OpenAIAgent()
        self.speech_processor = SpeechProcessing()
        self.todo_manager = TodoManager()

  def run(self):
      while True:
          command = self.speech_processor.listen()

if __name__ == "__main__":
    app = MainApp()
    app.run()