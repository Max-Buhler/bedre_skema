from bs4 import BeautifulSoup
import requests

class Scraper:
  def __init__(self, cookies):
    self._cookies = cookies
  
  def getHTML(self, URL):
    response = requests.get(URL, cookies=self._cookies)
    #html-koden laves om til en string
    clean_text = response.text.encode("utf-8", "ignore").decode("utf-8")
    self._soup = BeautifulSoup(clean_text, "html.parser")
    # print(self._soup)

  def getItems(self):
    pass

class SkemaScraper(Scraper):
  def __init__(self, cookies):
    super().__init__(cookies)

  #lectio's html-kode findes og defineres til _soup
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

  def getItems(self):
    modules = []
    #html-modul-elementerne bliver udvalgt via deres class-attribut
    for module in self._soup.findAll("a", attrs={"class":"s2skemabrik", "class": "s2bgbox"}):
      moduel_text = module.get("data-tooltip", "")
      if moduel_text:
        modules.append(moduel_text)
    return modules

class OpgaveScraper(Scraper):
  def __init__(self, cookies):
    super().__init__(cookies)
    self.__dictNøgler = ["week", "team", "title", "dueDate", "studyTime", "status", "absence", "waiting", "note", "grade", "studentNote"]
  
  def getItems(self):
    tasks = []
    for task in self._soup.findAll("tr", attrs={"class": "separationCell"}):
      taskDict = {}
      for index, element in enumerate(task.findAll("td", attrs={"class": "OnlyDesktop"})):
        tekst = element.get_text(separator='\n', strip=True)
        taskDict[self.__dictNøgler[index]] = tekst
      tasks.append(taskDict)
    return tasks

