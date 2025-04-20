from module.regexExtractor import *
from module.scraper import *
from dotenv import load_dotenv
import os
class UserModel():
  def __init__(self):
    #henter og definerer variabler fra .env fil
    load_dotenv()
    sessionId = os.getenv('SESSION_ID')
    autoLoginKey = os.getenv('AUTO_LOGIN_KEY')
    self.__cookies = { 
      "asp.net_sessionid": sessionId,
      "autologinkeyv2": autoLoginKey,
    }
    #dictionary, som holder alle scraper/extractor objekter
    self.__scrapers = {}
    self.__extractors = {}

  #slags getter-metode, der samtidig tjekker om der allereded findes en instands af klassen
  def __get_scraper(self, scraper_cls):
      if scraper_cls not in self.__scrapers:
          self.__scrapers[scraper_cls] = scraper_cls(self.__cookies)
      return self.__scrapers[scraper_cls]
  
  def __get_extractor(self, extractor_cls):
      if extractor_cls not in self.__extractors:
          self.__extractors[extractor_cls] = extractor_cls()
      return self.__extractors[extractor_cls]

  #Ved brug af scraperen og regex-klassen reuturneres en liste af den specificerede uges moduler
  def getSkema(self, req):
    scraper = self.__get_scraper(SkemaScraper)
    extractor = self.__get_extractor(SkemaRegexExtractor)
    #et udvalgt stykke af html-koden returneres som liste af moduler (moduler er strings)
    scraper.getHTML('https://www.lectio.dk/lectio/518/skemaNy.aspx', req.get("week", None), req.get("year", None))
    modulesList = scraper.getItems()
    #html-strings omdannes til dictionaries via regexklassen
    moduleData = []
    for module in modulesList:
      moduleData.append(extractor.getData(module))
    return moduleData
  
  #Ved brug af scraperen og regex-klassen reuturneres en liste af årets opgaver
  def getOpgaver(self):
    scraper = self.__get_scraper(OpgaveScraper)
    extractor = self.__get_extractor(OpgaveRegexExtractor)
    #et udvalgt stykke af html-koden returneres som en liste af opgaver (opgaver er dictionaries)
    scraper.getHTML('https://www.lectio.dk/lectio/518/OpgaverElev.aspx')
    taskList = scraper.getItems()
    taskData = []
    #dictionaryen modificeres lidt via regexklassen, for at splitte frist op i dato og tid
    for task in taskList:
      regResult = extractor.getData(task["dueDate"])
      taskData.append({
        "week": task["week"],
        "team": task["team"],
        "title": task["title"],
        "dueDate": regResult["dueDate"],
        "dueTime": regResult["dueTime"],
        "studyTime": task["studyTime"],
        "status": task["status"],
        "absence": task["absence"],
        "waiting": task["waiting"],
        "note": task["note"],
        "grade": task["grade"],
        "studentNote": task["studentNote"]
      })
    return taskData

#eksempel
# um = UserModel()
# print(um.getSkema({'type': 'skema', 'week': '15', 'year': '2025'}))
# print(um.getOpgaver())
# print(um.getSkema({'type': 'skema', 'week': '14', 'year': '2025'}))

