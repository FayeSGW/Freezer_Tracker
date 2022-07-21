import csv
from datetime import date as dt
import pandas as pd





def main():
    newitems = []
    global food
    food = [{'type': 'Hot Dog', 'time': '2'}, {'type': 'Luncheon Meat', 'time': '2'}, {'type': 'Bacon', 'time': '2'}, {'type': 'Sausage', 'time': '2'}, {'type': 'Burger', 'time': '4'}, {'type': 'Minced Meat', 'time': 
'4'}, {'type': 'Fresh Meat', 'time': '9'}, {'type': 'Fatty Fish', 'time': '3'}, {'type': 'White Fish', 'time': '8'}, {'type': 'Vacuum-Sealed Fish', 'time': '12'}, {'type': 'Quiche', 'time': '6'}, {'type': 'Meals', 'time': '6'}, {'type': 'Cooked Meat', 'time': '6'}, {'type': 'Pizza', 'time': '2'}, {'type': 'Fruit', 'time': '12'}, {'type': 'Veg', 'time': '12'}, {'type': 'Tomatoes', 'time': '2'}, {'type': 'Cheese', 'time': '6'}, {'type': 'Butter', 'time': '9'}, {'type': 'Milk', 'time': '3'}]



    #New item input
    new_datein = input("Date Added: ")
    new_item = input("Item Name: ")
    new_type = input("Item Type: ")
    newitems.append({"date_in": new_datein, "item": new_item, "type": new_type, "use_by": ""})
    useby(newitems)
    print(newitems)

    #Write new database to file   
    with open("FreezerOutput2.csv", "a", newline = "") as w:
        writer = csv.DictWriter(w, fieldnames = ["Date Added", "Item", "Type", "Use By"])
        for item in newitems:
            date_in = item["date_in"]
            food = item["item"]
            kind = item["type"]
            date_out = item["use_by"]
            writer.writerow({"Date Added": date_in, "Item": food, "Type": kind, "Use By": date_out})

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
        if x.lower() == i["type"].lower():
            return i["time"]


main()


