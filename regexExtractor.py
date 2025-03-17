import re

class RegexExtractor:
  def __init__(self):
    self.dateRegex = r"\d{1,2}/\d{1,2}-2025"
    self.timeRegex = r"\d{1,2}/\d{1,2}-2025 (\d{1,2}:\d{2}) til (\d{1,2}:\d{2})"
    self.teacherRegex = r"Lærer: ([A-Z][a-z]+(?:\s[A-Z][a-z]+)*) \(([a-z]{1,4})\)"
    self.roomRegex = r"Lokale: ([A-Z][0-9]{3}s)"
    self.teamRegex = r"Hold: ([A-Z][0-9][a-z] [A-Za-z]{2,3})"

  def getData(self, indhold):
      result = {
        "date": self._extract_group(self.dateRegex, indhold, 0),
        "timeFrom": self._extract_group(self.timeRegex, indhold, 1),
        "timeTo": self._extract_group(self.timeRegex, indhold, 2),
        "teacher": self._extract_group(self.teacherRegex, indhold, 1),
        "room": self._extract_group(self.roomRegex, indhold, 0),
        "team": self._extract_group(self.teamRegex, indhold, 0),
      }
      return result

  def _extract_group(self, regex, text, group_num):
      """Helper function to safely extract a regex match group."""
      match = re.search(regex, text)
      return match.group(group_num) if match else None
