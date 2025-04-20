import tkinter as tk
from tkinter import ttk
from module import *
from datetime import datetime, timedelta
from module import *
import tkinter.messagebox as msgbox
class Schelude:
    def __init__(self,root):
        #Giver dage og tid, som skal skrives ind i skemaet
        self.__days = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
        self.__times = ["08:15 - 09:00", "09:00 - 09:45", "10:00 - 10:45", "10:45 - 11:30","11:30 - 12:00","12:00 - 12:45",
                "12:45 - 13:30", "13:30 - 14:15","14:15 - 14:30", "14:30 - 15:15", "15:15 - 16:00","16:00 - 16:45"]
        

        #Laver en tom liste til moduler
        self.__entries = []
        #Lav root sådan at tkinter kan køre
        self.__root = root




        
        

    def createSchedule(self,data,year,week):
        #Laver en titel til programmet
        self.__root.title("Weekly Schedule")

        # Denne finder først dag i ugen
        start_of_week = datetime.fromisocalendar(year, week, 1)  # 1 = mandag

       

        # Generer datoer til dagene i ugen
        self.__week_dates = [(start_of_week + timedelta(days=i)).strftime("%Y/%m/%d") for i in range(7)]


        #Definere data som er hentet i control klassen til et atribut
        self.__moduleData = data

        #Laver en kollone til hver dag
        for col, day in enumerate([f"Uge {week}"] + self.__days):
            label = ttk.Label(self.__root, text=day, borderwidth=1, relief="solid", padding=15)
            label.grid(row=0, column=col, sticky="nsew")
        
        #Lav en række til hvert tidsinterval
        for row, time in enumerate(self.__times, start=1):
            label = ttk.Label(self.__root, text=time, borderwidth=1, relief="solid", padding=15)
            label.grid(row=row, column=0, sticky="nsew")

        #Laver modulerne
        self.createEntrys()
        #Tegner modulerne
        self.drawEntrys()




        
        self.__root.mainloop()

    


    def createEntrys(self):
        #Sletter de gamle entries hvis ugen er blevet ændret
        self.__entries = []
        #Laver et entry for hver modul der er i dataen
        for module in self.__moduleData:   
            #Hvis modullet ikke er aflyst er det et standard modul         
            if module["cancelled"]:
                self.__entries.append(EntryCancelled(module))
            #Ellers er det et aflyst modul
            else:    
                self.__entries.append(Entry(module))
        
    
    def drawEntrys(self):
        #Køre alle moduler drawEntry metode
        for entry in self.__entries:
            entry.drawEntry(self.__week_dates,self.__root,self.__times)





class Entry:
    def __init__(self, data):
        #Anvender igen data hentet med kontrol
        self.__data = data

    def drawEntry(self, week_dates, root, times):
        #Finder modulets egen data
        self.__ownDate = datetime.strptime(self.__data["date"], "%d/%m-%Y").strftime("%Y/%m/%d")

        # Finder kolonen for den givne dag
        col = None
        for i, date in enumerate(week_dates):
            if self.__ownDate == date:
                col = i + 1  
                break
        
        if col is None:
            return  # Skip hvis dagen ikke findes

        #Definere starten og slutningen af modulet
        start_time = self.__data["timeFrom"]
        end_time = self.__data["timeTo"]

        # Finder start kollonnen for modullet
        start_row = None
        for i, time in enumerate(times, start=1):
            #Splitter alle intervaller i 2 og sammenligner dem med start tidspunktet
            time_range = time.split(" - ")
            #Hvis tidspunktet matcher med timesplit eller er mindre.
            if start_time >= time_range[0]:   #(hvis den er større er tidspunktet for modulet ikke standard og dermed bliver den bare sat til det nærmeste)
                start_row = i
                

        #Samme princip som før men blot til at finde slutningen på modulet
        end_row = None
        for i, time in enumerate(times, start=1):
            time_range = time.split(" - ")
            if end_time <= time_range[1]: 
                end_row = i + 1
                break   #Her stoppes der eftersom at først gang at if statementet er true vil det øverste tidspunkt være nået

        if start_row is None or end_row is None:
            return  # Skip hvis start tidspunktet er uden for rækkevide

        rowspan = max(1, end_row - start_row)  # Sikre at mindst en række bliver taget af modulet

        # Her skabes selve den visuel representaiton af modulet
        label = ttk.Label(root, text=self.__data["team"], borderwidth=1, relief="solid",
                        padding=5 if rowspan == 1 else 15,  # Justere padding sådan den i teorien er mindre når modulet kun er 1 interval langt
                        background="lightblue" if not isinstance(self, EntryCancelled) else "red") #Her er et check for om modulet er aflyst, hvis det er aflyst laves modulet rødt ellers blåt

        #Her sættes modulet ind på dens plads i skemaet
        label.grid(row=start_row, column=col, rowspan=rowspan, sticky="nsew")
        #Her gøres sådan at hvis man klikker på modulet kaldes  on click funktionen
        label.bind("<Button-1>", lambda event: self.on_click())




    def on_click(self):
        #Her hvises en textbox med relevant info til det klikkede modul
        msgbox.showinfo("Entry Details", f"Hold: {self.__data['team']}\nTid: {self.__data['timeFrom']} - {self.__data['timeTo']}\nLærer:  {self.__data['teacher']}\n{self.__data['room']}\n{self.__data['note']}\n{self.__data['homework']}\n{self.__data['other']}")

#Denne klasse er tom eftersom det blot bruges til et if statement (:
class EntryCancelled(Entry):
    pass

