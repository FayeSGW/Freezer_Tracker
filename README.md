# FreezerTracker
 Two programmes to track items in the freezer.

 The first programme has three variations - one purely text-based (iteminput_text.py) and two with a tkinter GUI (one made using functions - iteminput_tkinter_func.py, and one using classes - iteminput_tkinter_classes.py).
 This programme allows you to add new items to the freezr database. Input requires the date you added the items, the name of the item, and what kind of food it is. The programme then uses the date and the kind of food to calculate a "use-by" date, based on freezer shelf-life recommendations.

 The second programme (useby_alert_ifttt.py) checks through the database, and if an item's "use-by" date is within 5 days of today's date, will send a message (using webhooks and Telegram via IFTTT) to let you know. This can be set up to run automatically once per day using Windows Task Scheduler (unsure about other OSes, sorry!)
 Note that you will need to set up your own applet on IFTTT.com for this!

 Required libraries: csv, datetime, pandas, requests, tkinter, tkcalendar.