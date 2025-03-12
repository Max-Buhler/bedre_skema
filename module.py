from regexExtractor import *
from scraper import *
from dotenv import load_dotenv
import os
class UserModel():
  def __init__(self):
    self.regexExtractor = RegexExtractor()
    load_dotenv()
    sessionId = os.getenv('SESSION_ID')
    autoLoginKey = os.getenv('AUTO_LOGIN_KEY')
    self.cookies = { 
      "asp.net_sessionid": sessionId,
      "autologinkeyv2": autoLoginKey,
    } 
    self.scraper = Scraper(self.cookies)
    self.urldict = {
      'skema': 'https://www.lectio.dk/lectio/518/skemany.aspx'
    }
  def getSkema(self, req):
    self.scraper.getHTML(self.urldict[req['type']])
    modulesList = self.scraper.getModules()
    moduleData = []
    for module in modulesList:
      moduleData.append(self.regexExtractor.getData(module))
    return moduleData
um = UserModel()
print(um.getSkema({'type': 'skema'}))