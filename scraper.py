from bs4 import BeautifulSoup
import requests

class Scraper:
  def __init__(self, cookies):
    self.cookies = cookies


  def getHTML(self, URL, week, year):
    if(week is None):
      response = requests.get(URL, cookies=self.cookies)
    else:
      if(year is None):
        response = requests.get(URL + "?week=" + week + "2025", cookies=self.cookies)
      else:
        response = requests.get(URL + "?week=" + week + year, cookies=self.cookies)
    response.encoding = "utf-8"
    clean_text = response.text.encode("utf-8", "ignore").decode("utf-8")
    self.soup = BeautifulSoup(clean_text, "html.parser")

  def getModules(self):
    modules = []
    for module in self.soup.findAll("a", attrs={"class":"s2skemabrik", "class": "s2bgbox"}):
      moduel_text = module.get("data-tooltip", "")
      if moduel_text:
        modules.append(moduel_text)
    return modules

