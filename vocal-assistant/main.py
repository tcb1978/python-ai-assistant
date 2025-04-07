from command_processing import CommandProcessing
from openai_agent import OpenAIAgent
from speech_processing import SpeechProcessing
from todo_manager import TodoManager
from speech_recognition import WaitTimeoutError

class MainApp:
  def __init__(self):
        self.command_processor = CommandProcessing()
        self.openai_agent = OpenAIAgent()
        self.speech_processor = SpeechProcessing()
        self.todo_manager = TodoManager()

  def run(self):
      while True:
          try:
              command = self.speech_processor.listen()
              if command != "":
                  gpt_answer = self.openai_agent.get_response(command)
                  print(f"ChatGPT Answered: {gpt_answer}")
          except WaitTimeoutError:
              print("Listening timed out while waiting for phrase to start")

if __name__ == "__main__":
    app = MainApp()
    app.run()