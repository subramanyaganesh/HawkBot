import os
from embedchain import Pipeline as App
from django.conf import settings

class Core:
    @staticmethod
    def core():
      os.environ["OPENAI_API_KEY"] =  settings.OPENAI_KEY
      configPath = os.path.join(os.path.dirname(__file__), "openai.yaml")
      print(configPath)
      hawk_bot = App.from_config(config_path=configPath)

      hawk_bot.add(os.path.join(os.path.dirname(__file__), "Admin Guide.jsonl"))
      hawk_bot.add(os.path.join(os.path.dirname(__file__), "fingate.jsonl"))

      return hawk_bot.serialize()
