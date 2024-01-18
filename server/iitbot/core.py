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

      hawk_bot.add("https://www.iit.edu/coursera")
      hawk_bot.add("https://www.iit.edu/sites/default/files/2023-11/Coursera-Guide-to-Registration_v4.pdf", data_type='pdf_file')
      hawk_bot.add("https://www.iit.edu/coursera/coursera-faqs")
      hawk_bot.add("https://www.iit.edu/coursera/course-offerings")
      hawk_bot.add("https://www.iit.edu/coursera/coursera-academic-calendar")

      # while True:
      #   question = input("Enter question:\n")
      #   if question in ['q', 'exit', 'quit']:
      #     break

      answer, sources =hawk_bot.query(question, citations=True)   
      firstValue = set(t[1] for t in sources)
      ans='\n'
      for i,element in enumerate(firstValue):
        ans = ans + f"Source {i+1} :{element}\n"
      return answer+ans