import csv
from datetime import date as dt
import pandas as pd
import tkinter as tk
from tkinter import BROWSE, ttk
from tkcalendar import Calendar, DateEntry

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #Lists & Variables
        self.items = []
        self.newitems = []
        #"type" is type of food in freezer, "time" is number of months before food quality starts to deteriorate
        self.food = [{'type': 'Hot Dog', 'time': '2'}, {'type': 'Luncheon Meat', 'time': '2'}, {'type': 'Bacon', 'time': '2'}, {'type': 'Sausage', 'time': '2'}, {'type': 'Burger', 'time': '4'}, {'type': 'Minced Meat', 'time': 
'4'}, {'type': 'Fresh Meat', 'time': '9'}, {'type': 'Fatty Fish', 'time': '3'}, {'type': 'White Fish', 'time': '8'}, {'type': 'Vacuum-Sealed Fish', 'time': '12'}, {'type': 'Quiche', 'time': '6'}, {'type': 'Meals', 'time': '6'}, {'type': 'Cooked Meat', 'time': '6'}, {'type': 'Pizza', 'time': '2'}, {'type': 'Fruit', 'time': '12'}, {'type': 'Veg', 'time': '12'}, {'type': 'Tomatoes', 'time': '2'}, {'type': 'Cheese', 'time': '6'}, {'type': 'Butter', 'time': '9'}, {'type': 'Milk', 'time': '3'}]
        
        self.foods = ["Hot Dog", "Luncheon Meat", "Bacon", "Sausage", "Burger", "Minced Meat", "Fresh Meat", "Fatty Fish", "White Fish", "Vacuum-Sealed Fish", "Quiche", "Meals", "Cooked Meat", "Pizza", "Fruit", "Veg", "Tomatoes", "Cheese", "Butter", "Milk"]
        self.m = 0

        #GUI Base
        self.title("Item input")
        ttk.Style().configure("TMenubutton", background = "white", border = "1")
        self.labelframe = ttk.Frame(self, padding = "10")
        self.labelframe.grid(column = 0, row = 0)
        self.inputframe = ttk.Frame(self, padding = "10")
        self.inputframe.grid(column = 0, row = 1)
        self.submitframe = ttk.Frame(self)
        self.submitframe.grid(column = 0, row = 2)

        #GUI Labels
        datelbl = ttk.Label(self.inputframe, text = "Date Added to freezer:")
        datelbl.grid(column = 0, row = 0)
        itemlbl = ttk.Label(self.inputframe, text = "Item:")
        itemlbl.grid(column = 1, row = 0)
        typelbl = ttk.Label(self.inputframe, text = "Food Type:")
        typelbl.grid(column = 2, row = 0)
        self.submitlbl = ttk.Label(self.submitframe, text = "")
        self.submitlbl.grid(column = 0, row = 1)

        #Calendar input
        self.cal = DateEntry(self.inputframe, width = 12, background = "darkblue", foreground = "white", borderwidth = 2, date = dt.today())
        self.cal.grid(column = 0, row = 1, sticky = "n")

        #Item Name input
        self.newitem = tk.StringVar()
        self.item_entry = ttk.Entry(self.inputframe, textvariable = self.newitem)
        self.item_entry.grid(column = 1, row = 1, sticky = "n")

        #Item Type input
        self.newtype = tk.StringVar()
        self.newtype.set(self.foods[0])
        self.type_entry = ttk.OptionMenu(self.inputframe, self.newtype, *self.foods)
        self.type_entry.config(width = 20)
        self.type_entry.grid(column = 2, row = 1, padx = "10")

        #Submit
        self.submit = ttk.Button(self.submitframe, text = "Submit", command = self.submission)
        self.submit.grid(column = 0, row = 0)


    

    def submission(self):
        new_datein = self.cal.get_date()
        new_item = str(self.newitem.get())
        new_type = str(self.newtype.get())
        self.newitems.append({"date_in": new_datein, "item": new_item, "type": new_type, "use_by": ""})
        self.useby(self.newitems)
        self.submitlbl.config(text = f"Added {new_item}")
        self.writedata()


    def useby(self, lst):
        for item in lst:
            date = str(item["date_in"])
            year, month, day = date.split("-")
            datein = dt(int(year), int(month), int(day))

            for i in self.food:
                if item["type"] == i["type"]:
                    self.m = int(i["time"])

            useby = datein + pd.DateOffset(months = self.m)
            item["use_by"] = useby.date()


    def writedata(self):
        #Write new database to file   
        with open("FreezerOutput.csv", "a", newline = "") as w:
            writer = csv.DictWriter(w, fieldnames = ["Date Added", "Item", "Type", "Use By"])
            for item in self.newitems:
                date_in = item["date_in"]
                fooditem = item["item"]
                kind = item["type"]
                date_out = item["use_by"]
                writer.writerow({"Date Added": date_in, "Item": fooditem, "Type": kind, "Use By": date_out})

if __name__ == "__main__":
    app = App()
    app.mainloop()


