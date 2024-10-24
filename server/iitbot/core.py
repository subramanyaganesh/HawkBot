import os
from embedchain import Pipeline as App
from django.conf import settings

class Core:
    @staticmethod
    def core():
      os.environ["OPENAI_API_TYPE"] = "azure"
      os.environ["AZURE_OPENAI_ENDPOINT"] = settings.AZURE_OPENAI_ENDPOINT
      os.environ["AZURE_OPENAI_API_KEY"] = settings.AZURE_OPENAI_API_KEY
      os.environ["OPENAI_API_VERSION"] = settings.OPENAI_API_VERSION

      configPath = os.path.join(os.path.dirname(__file__), "openai.yaml")
      print(configPath)
      hawk_bot = App.from_config(config_path=configPath)

      hawk_bot.add(os.path.join(os.path.dirname(__file__), "Admin Guide.jsonl"))
      hawk_bot.add(os.path.join(os.path.dirname(__file__), "fingate.jsonl"))

      return hawk_bot.serialize()
