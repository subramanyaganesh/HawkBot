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

      hawk_bot.add("https://www.iit.edu/coursera")
      hawk_bot.add("https://www.iit.edu/sites/default/files/2023-11/Coursera-Guide-to-Registration_v4.pdf", data_type='pdf_file')
      hawk_bot.add("https://www.iit.edu/coursera/coursera-faqs")
      hawk_bot.add("https://www.iit.edu/coursera/course-offerings")
      hawk_bot.add("https://www.iit.edu/coursera/coursera-academic-calendar")

      return hawk_bot.serialize()