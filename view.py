import tkinter as tk
from tkinter import ttk
from makeschedule import *
from module import *
from datetime import datetime, timedelta
class View:
    def __init__(self):
        #Her laves nogle basale ting som tkinter skal bruge for at køre
        self.__root = tk.Tk()
        self.__root.geometry("500x700")
        #En skema klasse laves
        self.__skema = Schelude(self.__root)
        
        #Her defineres året og ugen til at være det nuværende år og uge
        self.__year, self.__week, _ = datetime.today().isocalendar()
        #Går uge læsbar for getSkema funktionen

    
    def draw(self,data,controller):
        #Definere controlleren sådan at denne kan kaldes
        self.__controller = controller

        #Hvis man befinder sig i uge 53 eller 0 er man i et nyt år
        #Dermed opdateres ugen og året
        if self.__week >= 53:
            self.__week = 1
            self.__year += 1

        if self.__week <= 0:
            self.__week = 52
            self.__year -= 1

        #Alt i det gamle skema slettes
        for widget in self.__root.winfo_children():
            widget.destroy()
        #En knap til at gå en uge frem og tilbage laves
        ahead = tk.Button(self.__root, text="Næste uge", command=self.plusWeek)
        back = tk.Button(self.__root, text="Forrige uge", command=self.minusWeek)
        #Begge placeres
        ahead.place(x=100,y=650)
        back.place(x=0,y=650)
        #Skemaet laves
        self.__skema.createSchedule(data,self.__year,self.__week)

    def plusWeek(self):
        #Hvis uge frem knappen er blevet kliket opdateres ugen
        self.__week += 1
        #Controlleren bliver kaldt og giver ny data
        self.__controller.updateView()


    def minusWeek(self):
        #Hvis uge tilbage knappen er blevet kliket opdateres ugen
        self.__week -= 1
        #Controlleren bliver kaldt og giver ny data
        self.__controller.updateView()

    #Uge ligges så den er let tilgængelig i koden
    @property
    def week(self):
        return self.__week
    #År ligges så den er let tilgængelig i koden
    @property
    def year(self):
        return self.__year

