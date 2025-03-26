import tkinter as tk
from tkinter import ttk
from makeschedule import *
from module import *
from datetime import datetime, timedelta
class View:
    def __init__(self):
        self.root = tk.Tk()
        self.skema = Schelude(self.root)
        self.root.geometry("500x700")

        self.__year, self.__week, _ = datetime.today().isocalendar()
        #Går uge læsbar for getSkema funktionen

    
    def draw(self,data,controller):
        self.controller = controller

        if self.__week >= 53:
            self.__week = 1
            self.__year += 1

        if self.__week <= 0:
            self.__week = 52
            self.__year -= 1


        for widget in self.root.winfo_children():
            widget.destroy()

        ahead = tk.Button(self.root, text="Næste uge", command=self.plusWeek)
        back = tk.Button(self.root, text="Forrige uge", command=self.minusWeek)

        ahead.place(x=100,y=650)
        back.place(x=0,y=650)

        self.skema.createSchedule(data,self.__year,self.__week)

    def plusWeek(self):
        self.__week += 1

        self.controller.updateView()

    def minusWeek(self):
        self.__week -= 1

        self.controller.updateView()

    @property
    def week(self):
        return self.__week
    
    @property
    def year(self):
        return self.__year

