from module.regexExtractor import *
from module.scraper import *
from dotenv import load_dotenv
import os
class UserModel():
  def __init__(self):
    #henter variabler fra .env fil
    load_dotenv()
    sessionId = os.getenv('SESSION_ID')
    autoLoginKey = os.getenv('AUTO_LOGIN_KEY')
    self.__cookies = { 
      "asp.net_sessionid": sessionId,
      "autologinkeyv2": autoLoginKey,
    } 

  #Ved brug af scraperen og regex-klassen reuturneres en liste af den specificerede uges moduler
  def getSkema(self, req):
    self.__scraper = SkemaScraper(self.__cookies)
    self.__regexExtractor = SkemaRegexExtractor()
    #et udvalgt stykke af html-koden returneres som string
    self.__scraper.getHTML('https://www.lectio.dk/lectio/518/skemaNy.aspx', req.get("week", None), req.get("year", None))
    modulesList = self.__scraper.getItems()
    #html-stringen omdannes til dictionaries
    moduleData = []
    for module in modulesList:
      moduleData.append(self.__regexExtractor.getData(module))
    return moduleData
  
  def getOpgaver(self, req):
    self.__scraper = OpgaveScraper(self.__cookies)
    self.__regexExtractor = OpgaveRegexExtractor()
    #et udvalgt stykke af html-koden returneres som string
    self.__scraper.getHTML('https://www.lectio.dk/lectio/518/OpgaverElev.aspx')
    taskList = self.__scraper.getItems()
    taskData = []
    for task in taskList:
      regResult = self.__regexExtractor.getData(task["dueDate"])
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
um = UserModel()
# print(um.getSkema({'type': 'skema', 'week': '15', 'year': '2025'}))
# print(um.getSkema({'type': 'skema'}))
# print(um.getOpgaver({}))
