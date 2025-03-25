from regexExtractor import *
from scraper import *
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
    #En opslags variabel, hvis klassen engang skal håndtere flere requests
    self.__urldict = {
      'skema': 'https://www.lectio.dk/lectio/518/skemany.aspx'
    }
    #Laver instandser af importerede klasser
    self.__scraper = Scraper(self.__cookies)
    self.__regexExtractor = RegexExtractor()

  #Ved brug af scraperen og regex-klassen reuturneres en liste af den specificerede uges moduler
  def getSkema(self, req):
    #et udvalgt stykke af html-koden returneres som string

    if int(req.get("week", None)) < 10:
      self.__weekStr = f"0{req.get("week", None)}"
    else:
      self.__weekStr = f"{req.get("week", None)}"

    self.__scraper.getHTML(self.__urldict[req['type']], self.__weekStr, req.get("year", None))
    modulesList = self.__scraper.getModules()
    #html-stringen omdannes til dictionaries
    moduleData = []
    for module in modulesList:
      moduleData.append(self.__regexExtractor.getData(module,req.get("year", None)))
    return moduleData
#eksempel
um = UserModel()
# print(um.getSkema({'type': 'skema', 'week': '13', 'year': '2025'}))
# print(um.getSkema({'type': 'skema'}))
