import re

class RegexExtractor:
  def __init__(self):
    #De forskællige regexes defineres
    self._dateRegex = r"(\d{1,2}/\d{1,2}-\d{4})"
    self._timeRegex = r"\d{1,2}/\d{1,2}-\d{4} (\d{1,2}:\d{2}) til (\d{1,2}:\d{2})"
    self._teacherRegex = r"Lærer: (([A-Z][a-z]+(?:\s[A-Z][a-z]+)*) \(([a-z]{1,4})\))+"
    self._roomRegex = r"Lokale: ([A-Z][0-9]{3}s)"
    self._teamRegex = r"Hold: ([A-Z][0-9][a-z]?\s+[A-Za-z]{2,3}\s+([A-Za-z]{2,3})*)"
    self._cancelledRegex = r"Aflyst!" 
    self._noteRegex = r"Note:(.*)"
    self._homeworkRegex = r"Lektier:(.*?)(Øvrigt indhold|Note|$)"
    self._otherRegex = r"Øvrigt indhold:(.*?)(Lektier|Note|$)"
    self._dueDateRegex = r"(\d{1,2}/\d{1,2}-\d{4}) (\d{1,2}:\d{2})"

  def getData(self):
     pass
  
  #En metode, som tester om regexen har fundet et match og returner værdien, hvis den er fundet (den extraherer altså regexens output)
  def _extractGroup(self, regex, text, group_num):
    match = re.search(regex, text, re.DOTALL)
    return match.group(group_num) if match else ""



class SkemaRegexExtractor(RegexExtractor):
  def __init__(self):
    super().__init__()

  #de specifikke informationer bliver fundet i html-stringen via regexene og __extractGroup metoden, hvorefter de bliver returneret som en dictionary
  def getData(self, indhold):
      
      result = {
        "date": self._extractGroup(self._dateRegex, indhold, 1),
        "timeFrom": self._extractGroup(self._timeRegex, indhold, 1),
        "timeTo": self._extractGroup(self._timeRegex, indhold, 2),
        "teacher": self._extractGroup(self._teacherRegex, indhold, 1),
        "room": self._extractGroup(self._roomRegex, indhold, 1),
        "team": self._extractGroup(self._teamRegex, indhold, 1),
        "cancelled": True if re.search(self._cancelledRegex, indhold) else False,
        "note": self._extractGroup(self._noteRegex, indhold, 1),
        "homework": self._extractGroup(self._homeworkRegex, indhold, 1),
        "other": self._extractGroup(self._otherRegex, indhold, 1)
      }
      return result


class OpgaveRegexExtractor(RegexExtractor):
  def __init__(self):
    super().__init__()
  
  def getData(self, indhold):
    result = {
      "dueDate": self._extractGroup(self._dueDateRegex, indhold, 1),
      "dueTime": self._extractGroup(self._dueDateRegex, indhold, 2)
    }
    return result