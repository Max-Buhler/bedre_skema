from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import re
load_dotenv()
sessionId = os.getenv('SESSION_ID')
autoLoginKey = os.getenv('AUTO_LOGIN_KEY')


class Scraper:
  def __init__(self, sessionId, autoLoginKey, URL):
    self.cookies = {
      "ASP.NET_SessionId": sessionId,
      "autologinkeyV2": autoLoginKey,
    }
    self.URL = URL
    self.soup = self.getHTML()

  def getHTML(self):
    response = requests.get(self.URL, cookies=self.cookies)
    response.encoding = "utf-8"
    clean_text = clean_text = response.text.lstrip("\ufeff")
    soup = BeautifulSoup(clean_text, "html.parser")
    return soup
  
  def getClasses(self):
    for module in self.soup.findAll("a", attrs={"class":"s2skemabrik"}):
      moduel_text = module.get("data-tooltip", "")
      if moduel_text:
        print(moduel_text)






LectioScraper = Scraper(sessionId, autoLoginKey, "https://www.lectio.dk/lectio/518/SkemaNy.aspx")
LectioScraper.getClasses()



