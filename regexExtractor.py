import re

class RegexExtractor:
  def __init__(self):
    #De forskællige regexes defineres
    self.__dateRegex = r"\d{1,2}/\d{1,2}-2025"
    self.__timeRegex = r"\d{1,2}/\d{1,2}-2025 (\d{1,2}:\d{2}) til (\d{1,2}:\d{2})"
    self.__teacherRegex = r"Lærer: ([A-Z][a-z]+(?:\s[A-Z][a-z]+)*) \(([a-z]{1,4})\)"
    self.__roomRegex = r"Lokale: ([A-Z][0-9]{3}s)"
    self.__teamRegex = r"Hold: ([A-Z][0-9][a-z] [A-Za-z]{2,3})"
    self.__cancelledRegex = r"Aflyst!" 
    self.__noteRegex = r"Note:(.*)"
    self.__homeworkRegex = r"Lektier:(.*?)(Øvrigt indhold|Note|$)"
    self.__otherRegex = r"Øvrigt indhold:(.*?)(Lektier|Note|$)"

  #de specifikke informationer bliver fundet i html-stringen via regexene og __extractGroup metoden, hvorefter de bliver returneret som en dictionary
  def getData(self, indhold):
      result = {
        "date": self.__extractGroup(self.__dateRegex, indhold, 0),
        "timeFrom": self.__extractGroup(self.__timeRegex, indhold, 1),
        "timeTo": self.__extractGroup(self.__timeRegex, indhold, 2),
        "teacher": self.__extractGroup(self.__teacherRegex, indhold, 1),
        "room": self.__extractGroup(self.__roomRegex, indhold, 1),
        "team": self.__extractGroup(self.__teamRegex, indhold, 1),
        "cancelled": True if re.search(self.__cancelledRegex, indhold) else False,
        "note": self.__extractGroup(self.__noteRegex, indhold, 1),
        "homework": self.__extractGroup(self.__homeworkRegex, indhold, 1),
        "other": self.__extractGroup(self.__otherRegex, indhold, 1)
      }
      return result

  #En metode, som tester om regexen har fundet et match og returner værdien, hvis den er fundet (den extraherer altså regexens output)
  def __extractGroup(self, regex, text, group_num):
      """Helper function to safely extract a regex match group."""
      match = re.search(regex, text, re.DOTALL)
      return match.group(group_num) if match else None
