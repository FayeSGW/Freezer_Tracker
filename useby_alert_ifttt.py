import csv
from datetime import date
import pandas as pd
import requests

#Note that you will need to set up an applet on IFTTT.com for this!
ifttt_webhooks_url = "https://maker.ifttt.com/trigger/{}/with/key/{your key}"
items = []

def main():
    with open("FreezerOutput.csv") as file:
            reader = csv.DictReader(file, delimiter = ",")
            for row in reader:
                if row["Date Added"] == "":
                    pass
                else:
                    items.append({"date_in": row["Date Added"], "item": row["Item"], "type": row["Type"], "use_by": row["Use By"]})


    for item in items:
        use = str(item["use_by"])
        #Whenever csv file is saved in Excel, dates revert to dd/mm/yyyy format - this converts them to datetime format if necessary.
        if "/" in use:
            day, month, year = use.split("/")
            useby = date(int(year), int(month), int(day))
        #If csv file not saved in Excel since new entries added, dates are already in datetime format
        else:
            useby = use
        alert = date.today() + pd.DateOffset(days = 5)   
        if date.today() <= useby <= alert.date(): 
            post_IFTTT_webhook("useby_approaching", item["item"], str(useby))


def post_IFTTT_webhook(event, item, date):
    data = {"value1": item, "value2": date}
    ifttt_event_url = ifttt_webhooks_url.format(event)
    requests.post(ifttt_event_url, json = data)

if __name__ == "__main__":
    main()
    

