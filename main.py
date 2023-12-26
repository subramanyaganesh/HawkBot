import os
from embedchain import Pipeline as App

# bot instance
os.environ["OPENAI_API_KEY"] = "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"

hawk_bot = App()
hawk_bot = App.from_config(yaml_path="openai.yaml")

hawk_bot.add("https://ots.iit.edu/printing/student-guest-printers")

hawk_bot.add("https://www.iit.edu/housing/housing-options/residence-halls")

hawk_bot.add("https://www.iit.edu/housing/housing-options/housing-rates")

hawk_bot.add("https://iit.libcal.com/hours/")

hawk_bot.add("https://bulletin.iit.edu/graduate/colleges/engineering/ece/master-engineering-artificial-intelligence-computer-vision-control")

while True:
  question = input("Enter question:\n")
  if question in ['q', 'exit', 'quit']:
    break

  answer = hawk_bot.query(question)
  print(answer)
