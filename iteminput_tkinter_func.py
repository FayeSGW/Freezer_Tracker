import csv
from datetime import date as dt
from turtle import bgcolor
import pandas as pd
import tkinter as tk
from tkinter import BROWSE, ttk
from tkcalendar import Calendar, DateEntry

root = tk.Tk()
root.title("Item input")
ttk.Style().configure("TMenubutton", background = "white", border = "1")

labelframe = ttk.Frame(root, padding = "10")
labelframe.grid(column = 0, row = 0)
inputframe = ttk.Frame(root, padding = "10")
inputframe.grid(column = 0, row = 1)

submitframe = ttk.Frame(root)
submitframe.grid(column = 0, row = 2)

def main():
    global newitems
    newitems = []
    global food #"type" is type of food in freezer, "time" is number of months before food quality starts to deteriorate
    food = [{'type': 'Hot Dog', 'time': '2'}, {'type': 'Luncheon Meat', 'time': '2'}, {'type': 'Bacon', 'time': '2'}, {'type': 'Sausage', 'time': '2'}, {'type': 'Burger', 'time': '4'}, {'type': 'Minced Meat', 'time': 
'4'}, {'type': 'Fresh Meat', 'time': '9'}, {'type': 'Fatty Fish', 'time': '3'}, {'type': 'White Fish', 'time': '8'}, {'type': 'Vacuum-Sealed Fish', 'time': '12'}, {'type': 'Quiche', 'time': '6'}, {'type': 'Meals', 'time': '6'}, {'type': 'Cooked Meat', 'time': '6'}, {'type': 'Pizza', 'time': '2'}, {'type': 'Fruit', 'time': '12'}, {'type': 'Veg', 'time': '12'}, {'type': 'Tomatoes', 'time': '2'}, {'type': 'Cheese', 'time': '6'}, {'type': 'Butter', 'time': '9'}, {'type': 'Milk', 'time': '3'}]
    
    foods = ["Hot Dog", "Luncheon Meat", "Bacon", "Sausage", "Burger", "Minced Meat", "Fresh Meat", "Fatty Fish", "White Fish", "Vacuum-Sealed Fish", "Quiche", "Meals", "Cooked Meat", "Pizza", "Fruit", "Veg", "Tomatoes", "Cheese", "Butter", "Milk"]

    global submitlbl
    #GUI
    datelbl = ttk.Label(inputframe, text = "Date Added to freezer:")
    datelbl.grid(column = 0, row = 0)
    itemlbl = ttk.Label(inputframe, text = "Item:")
    itemlbl.grid(column = 1, row = 0)
    typelbl = ttk.Label(inputframe, text = "Food Type:")
    typelbl.grid(column = 2, row = 0)
    submitlbl = ttk.Label(submitframe, text = "")
    submitlbl.grid(column = 0, row = 1)

    global cal
    cal = DateEntry(inputframe, width = 12, background = "darkblue", foreground = "white", borderwidth = 2, date = dt.today())
    cal.grid(column = 0, row = 1)

    submit = ttk.Button(submitframe, text = "Submit", command = submission)
    submit.grid(column = 0, row = 0)

    global newitem
    newitem = tk.StringVar()
    item_entry = ttk.Entry(inputframe, textvariable = newitem)
    item_entry.grid(column = 1, row = 1)

    global newtype
    global type_entry
    newtype = tk.StringVar()
    newtype.set(foods[0])
    type_entry = ttk.OptionMenu(inputframe, newtype, *foods)
    type_entry.config(width = 20)
    type_entry.grid(column = 2, row = 1, padx = "10")


    root.mainloop()

def submission():
    new_datein = cal.get_date()
    new_item = str(newitem.get())
    new_type = str(newtype.get())
    newitems.append({"date_in": new_datein, "item": new_item, "type": new_type, "use_by": ""})
    useby(newitems)
    submitlbl.config(text = f"{new_item} added")
    writedata()


def useby(lst):
    for item in lst:
        date = str(item["date_in"])
        year, month, day = date.split("-")
        datein = dt(int(year), int(month), int(day))
        m = int(time(item["type"]))
        useby = datein + pd.DateOffset(months = m)
        item["use_by"] = useby.date()

def time(x):
    for i in food:
        if x == i["type"]:
            return i["time"]

def writedata():
     #Write new database to file   
    with open("FreezerOutput.csv", "a", newline = "") as w:
        writer = csv.DictWriter(w, fieldnames = ["Date Added", "Item", "Type", "Use By"])
        for item in newitems:
            date_in = item["date_in"]
            fooditem = item["item"]
            kind = item["type"]
            date_out = item["use_by"]
            writer.writerow({"Date Added": date_in, "Item": fooditem, "Type": kind, "Use By": date_out})


main()


