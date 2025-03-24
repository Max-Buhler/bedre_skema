import tkinter as tk
from tkinter import ttk
from module import *
from datetime import datetime, timedelta
from module import *
class Schelude:
    def __init__(self,moduleData):
        self.days = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
        self.times = ["08:15 - 09:00", "09:00 - 09:45", "10:00 - 10:45", "10:45 - 11:30","12:00 - 12:45",
                "12:45 - 13:30", "13:30 - 14:15", "14:30 - 15:15", "15:15 - 16:00"]
        self.moduleData = moduleData
        # Get the current year and ISO week number
        year, week, _ = datetime.today().isocalendar()

        # Get the Monday of the given ISO week
        start_of_week = datetime.fromisocalendar(year, week, 1)  # 1 = Monday

        # Hent data fra module ud fra hvilken uge vi er i

        # Generate the dates for the entire week (Monday to Sunday)
        self.week_dates = [(start_of_week + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]

    def createSchedule(self):
        root = tk.Tk()
        root.title("Weekly Schedule")
        
        
        for col, day in enumerate(["Tid"] + self.days):
            label = ttk.Label(root, text=day, borderwidth=1, relief="solid", padding=5)
            label.grid(row=0, column=col, sticky="nsew")
        
        for row, time in enumerate(self.times, start=1):
            label = ttk.Label(root, text=time, borderwidth=1, relief="solid", padding=5)
            label.grid(row=row, column=0, sticky="nsew")


            # for col in range(1, len(self.days) + 1):
            #     entry = ttk.Label(root, borderwidth=1, relief="solid", padding=5)
            #     entry.grid(row=row, column=col, sticky="nsew")
            #     entries[(row, col)] = entry
        
        root.mainloop()
    
    def createEntrys(self):
        for module in self.moduleData:
            if module["cancelled"]:
                EntryCancelled(module)
            else:
                Entry(module)




class Entry:
    def __init__(self,data):
        self.data = data

    def drawEntry(self):
        
        self.data["date"]
        pass

class EntryCancelled:
    def __init__():
        super().__init__()
        pass