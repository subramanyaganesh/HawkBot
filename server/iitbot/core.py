import os
from embedchain import Pipeline as App
from django.conf import settings

class Core:
    @staticmethod
    def core():
      os.environ["OPENAI_API_KEY"] =  settings.OPENAI_KEY
      configPath = os.path.join(os.path.dirname(__file__), "openai.yaml")
      # print(configPath)
      hawk_bot = App.from_config(config_path=configPath)

      hawk_bot.add("https://www.iit.edu/coursera")
      #hawk_bot.add("https://iit.libcal.com/hours/")
      hawk_bot.add("https://www.iit.edu/sites/default/files/2023-11/Coursera-Guide-to-Registration_v4.pdf", data_type='pdf_file')
      hawk_bot.add("https://www.iit.edu/coursera/coursera-faqs")
      hawk_bot.add("https://www.iit.edu/coursera/course-offerings")
      hawk_bot.add("https://www.iit.edu/coursera/coursera-academic-calendar")
      hawk_bot.add("https://www.iit.edu/coursera/mba-pba")

      #hawk_bot.add("https://ots.iit.edu/printing/student-guest-printers")

      #hawk_bot.add("https://www.iit.edu/housing/housing-options/residence-halls")

      #hawk_bot.add("https://www.iit.edu/housing/housing-options/housing-rates")

  

      #hawk_bot.add("https://bulletin.iit.edu/graduate/colleges/engineering/ece/master-engineering-artificial-intelligence-computer-vision-control")

      # print(f'This is the test------------{hawk_bot.get_data_sources()}')

      return hawk_bot.serialize()
