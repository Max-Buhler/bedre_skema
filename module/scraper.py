from bs4 import BeautifulSoup
import requests

class Scraper:
  def __init__(self, cookies):
    self._cookies = cookies
  
  #HTML kode hentes som string
  def getHTML(self, URL):
    response = requests.get(URL, cookies=self._cookies)
    #html-koden laves om til en string
    cleanText = response.text.encode("utf-8", "ignore").decode("utf-8")
    self._soup = BeautifulSoup(cleanText, "html.parser")

  def getItems(self):
    raise NotImplementedError("Subclasses must implement this method.")

#subklasse af scraper, der scraper lectioskemaet
class SkemaScraper(Scraper):
  def __init__(self, cookies):
    super().__init__(cookies)

  #lectio's skema-html-kode hentes og defineres til _soup
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
    super().getHTML(url)

  #html-koden bliver reduceret til de enkelte timers beskrivelser
  def getItems(self):
    modules = []
    #html-modul-elementerne bliver udvalgt via deres class-attribut
    for module in self._soup.findAll("a", attrs={"class":"s2skemabrik", "class": "s2bgbox"}):
      moduel_text = module.get("data-tooltip", "")
      if moduel_text:
        modules.append(moduel_text)
    return modules

#subklasse af scraper, der scraper lectioopgaver
class OpgaveScraper(Scraper):
  def __init__(self, cookies):
    super().__init__(cookies)
    #navne til opgave-dictionarys nøgler
    self.__dictKeys = ["week", "team", "title", "dueDate", "studyTime", "status", "absence", "waiting", "note", "grade", "studentNote"]
  
  #html-kode bliver reduceret til et dictionary med opgavernes oplysninger
  def getItems(self):
    tasks = []
    for task in self._soup.findAll("tr", attrs={"class": "separationCell"}):
      taskDict = {}
      #hvert td-element har en af værdierne til en af de forigt definerede nøgler. Via forloopens index flættes nøglen og td-elementets værdi sammen i et dictionary
      for index, element in enumerate(task.findAll("td", attrs={"class": "OnlyDesktop"})):
        tekst = element.get_text(separator='\n', strip=True)
        taskDict[self.__dictKeys[index]] = tekst
      tasks.append(taskDict)
    return tasks
