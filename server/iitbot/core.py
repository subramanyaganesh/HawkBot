import os
from embedchain import Pipeline as App

class Core:
    @staticmethod
    def core(question):
      os.environ["OPENAI_API_KEY"] = "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"

      hawk_bot = App()
      configPath = os.path.join(os.path.dirname(__file__), "openai.yaml")
      print(configPath)
      hawk_bot = App.from_config(config_path=configPath)

      hawk_bot.add("https://ots.iit.edu/printing/student-guest-printers")

      hawk_bot.add("https://www.iit.edu/housing/housing-options/residence-halls")

      hawk_bot.add("https://www.iit.edu/housing/housing-options/housing-rates")

      hawk_bot.add("https://iit.libcal.com/hours/")

      hawk_bot.add("https://bulletin.iit.edu/graduate/colleges/engineering/ece/master-engineering-artificial-intelligence-computer-vision-control")

      # while True:
      #   question = input("Enter question:\n")
      #   if question in ['q', 'exit', 'quit']:
      #     break

      answer = hawk_bot.query(question)
      print(answer)
      return answer

