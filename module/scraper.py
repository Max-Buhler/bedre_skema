from bs4 import BeautifulSoup
import requests

class Scraper:
  def __init__(self, cookies):
    self.__cookies = cookies

  #lectio's html-kode findes og defineres til __soup
  def getHTML(self, URL, week, year):
    #via betingelser findes der ud af om år og uge er defineret. Desuden sikres der at ugen er tocifret
    if(week is None):
      url = URL
    elif(year is None):
      if(int(week) < 10):
        week = f"0{week}"
      url = URL + "?week=" + week + "2025"
    else:
      if(int(week) < 10):
        week = f"0{week}"
      url = URL + "?week=" + week + year
    response = requests.get(url, cookies=self.__cookies)
    #html-koden laves om til en string
    clean_text = response.text.encode("utf-8", "ignore").decode("utf-8")
    self.__soup = BeautifulSoup(clean_text, "html.parser")

  def getModules(self):
    modules = []
    #html-modul-elementerne bliver udvalgt via deres class-attribut
    for module in self.__soup.findAll("a", attrs={"class":"s2skemabrik", "class": "s2bgbox"}):
      moduel_text = module.get("data-tooltip", "")
      if moduel_text:
        modules.append(moduel_text)
    return modules

