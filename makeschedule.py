import tkinter as tk
from tkinter import ttk
from module import *
from datetime import datetime, timedelta
from module import *
import tkinter.messagebox as msgbox
class Schelude:
    def __init__(self,root):
        self.__days = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
        self.__times = ["08:15 - 09:00", "09:00 - 09:45", "10:00 - 10:45", "10:45 - 11:30","11:30 - 12:00","12:00 - 12:45",
                "12:45 - 13:30", "13:30 - 14:15","14:15 - 14:30", "14:30 - 15:15", "15:15 - 16:00","16:00 - 16:45"]
        # Get the current year and ISO week number


        self.__entries = []

        self.__root = root




        
        

    def createSchedule(self,data,year,week):

        self.__root.title("Weekly Schedule")

        # Get the Monday of the given ISO week
        start_of_week = datetime.fromisocalendar(year, week, 1)  # 1 = Monday

        # Hent data fra module ud fra hvilken uge vi er i

        # Generate the dates for the entire week (Monday to Sunday)
        self.__week_dates = [(start_of_week + timedelta(days=i)).strftime("%Y/%m/%d") for i in range(7)]


        #Henter data med getSkema funktionen
        self.__moduleData = data

        for col, day in enumerate([f"Uge {week}"] + self.__days):
            label = ttk.Label(self.__root, text=day, borderwidth=1, relief="solid", padding=15)
            label.grid(row=0, column=col, sticky="nsew")
        
        for row, time in enumerate(self.__times, start=1):
            label = ttk.Label(self.__root, text=time, borderwidth=1, relief="solid", padding=15)
            label.grid(row=row, column=0, sticky="nsew")

        self.createEntrys()
        self.drawEntrys()




        
        self.__root.mainloop()

    


    def createEntrys(self):
        self.__entries = []
        for module in self.__moduleData:            
            if module["cancelled"]:
                self.__entries.append(EntryCancelled(module))

            else:    
                self.__entries.append(Entry(module))
        
    
    def drawEntrys(self):
        for entry in self.__entries:
            entry.drawEntry(self.__week_dates,self.__root,self.__times)





class Entry:
    def __init__(self, data):
        self.__data = data

    def drawEntry(self, week_dates, root, times):

        self.__ownDate = datetime.strptime(self.__data["date"], "%d/%m-%Y").strftime("%Y/%m/%d")

        # Find the column for the given date
        col = None
        for i, date in enumerate(week_dates):
            if self.__ownDate == date:
                col = i + 1  # +1 because column 0 is for time labels
                break
        
        if col is None:
            return  # Skip if date is not found

        start_time = self.__data["timeFrom"]
        end_time = self.__data["timeTo"]

        # Find the start row (earliest matching time slot)
        start_row = None
        for i, time in enumerate(times, start=1):
            time_range = time.split(" - ")
            if start_time >= time_range[0]:  # If entry starts at or after this time slot
                start_row = i

        # Find the end row (earliest time slot where it should end)
        end_row = None
        for i, time in enumerate(times, start=1):
            time_range = time.split(" - ")
            if end_time <= time_range[1]:  # If entry should end at or before this time slot
                end_row = i + 1
                break  # We stop at the first matching time slot

        if start_row is None or end_row is None:
            return  # Skip if entry time is out of bounds

        rowspan = max(1, end_row - start_row)  # Ensure at least 1 row is taken

        # Create a label with adjusted rowspan
        label = ttk.Label(root, text=self.__data["team"], borderwidth=1, relief="solid",
                        padding=5 if rowspan == 1 else 15,  # Adjust padding for shorter entries
                        background="lightblue" if not isinstance(self, EntryCancelled) else "red")

        label.grid(row=start_row, column=col, rowspan=rowspan, sticky="nsew")
        label.bind("<Button-1>", lambda event: self.on_click())




    def on_click(self):
        msgbox.showinfo("Entry Details", f"Hold: {self.__data['team']}\nTid: {self.__data['timeFrom']} - {self.__data['timeTo']}\nLærer:  {self.__data['teacher']}\n{self.__data['room']}\n{self.__data['note']}\n{self.__data['homework']}\n{self.__data['other']}")

class EntryCancelled(Entry):
    pass

