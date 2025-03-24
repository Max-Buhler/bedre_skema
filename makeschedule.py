import tkinter as tk
from tkinter import ttk

# class Schelude
#   def __init__(self):

def create_schedule():
    root = tk.Tk()
    root.title("Weekly Schedule")
    
    days = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
    times = ["08:15 - 09:00", "09:00 - 09:45", "10:00 - 10:45", "10:45 - 11:30","12:00 - 12:45",
             "12:45 - 13:30", "13:30 - 14:15", "14:30 - 15:15", "15:15 - 16:00"]
    
    for col, day in enumerate(["Tid"] + days):
        label = ttk.Label(root, text=day, borderwidth=1, relief="solid", padding=5)
        label.grid(row=0, column=col, sticky="nsew")
    
    entries = {}
    
    for row, time in enumerate(times, start=1):
        label = ttk.Label(root, text=time, borderwidth=1, relief="solid", padding=5)
        label.grid(row=row, column=0, sticky="nsew")
        
        for col in range(1, len(days) + 1):
            entry = ttk.Entry(root, width=15)
            entry.grid(row=row, column=col, sticky="nsew")
            entries[(row, col)] = entry
    
    root.mainloop()

create_schedule()