import csv
from datetime import date as dt
import pandas as pd


def main():
    global items
    items = []
    global food
    food = []

    
    importdata()
    useby(items)
    exportdata()


def importdata():
    #Import existing database of freezer contents
    with open("Database2.csv") as file:
        reader = csv.DictReader(file, delimiter = ",")
        for row in reader:
            if row["In"] == "":
                pass
            else:
                items.append({"date_in": row["In"], "item": row["Item"], "type": row["Type"], "use_by": row["Out"]})
    
    #Import database of food types
    with open("Types.csv") as f:
        read = csv.DictReader(f)
        for row in read:
            food.append({"type": row["Type"], "time": row["Months"]})

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

def exportdata():
        #Write new database to file   
    with open("Output.csv", "w", newline = "") as w:
        writer = csv.DictWriter(w, fieldnames = ["Date Added", "Item", "Type", "Use By"])
        writer.writeheader()
        for item in items:
            date_in = item["date_in"]
            food = item["item"]
            kind = item["type"]
            date_out = item["use_by"]
            writer.writerow({"Date Added": date_in, "Item": food, "Type": kind, "Use By": date_out})

if __name__ == "__main__":
    main()


