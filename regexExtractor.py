import re

class RegexExtractor:
  def __init__(self):
    self.dateRegex = r"\d{1,2}/\d{1,2}-2025"
    self.timeRegex = r"\d{1,2}/\d{1,2}-2025 (\d{1,2}:\d{2}) til (\d{1,2}:\d{2})"
    self.teacherRegex = r"Lærer: ([A-Z][a-z]+(?:\s[A-Z][a-z]+)*) \(([a-z]{1,4})\)"
    self.roomRegex = r"Lokale: ([A-Z][0-9]{3}s)"
    self.teamRegex = r"Hold: ([A-Z][0-9][a-z] [A-Z]{2,3})"

  def getData(self, indhold):
    result = {
      "date": re.search(self.dateRegex, indhold).group(0), 
      "timeFrom": re.search(self.timeRegex, indhold).group(1), 
      "timeTo": re.search(self.timeRegex, indhold).group(2), 
      "teacher": re.search(self.teacherRegex, indhold).group(1), 
      "room": re.search(self.roomRegex, indhold).group(0), 
      "team": re.search(self.teamRegex, indhold).group(0), 
    }
    return result
