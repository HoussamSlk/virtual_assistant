# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:33:29 2021

@author: qihus
"""
## Import Libraries ***
import pandas as pd
import wolframalpha
client = wolframalpha.Client("QQLV9J-P4WX73G35E")
import wikipedia
import JarvisAI
obj = JarvisAI.JarvisAssistant()
import PySimpleGUI as sg
##############################################################################
### LOAD DB SAMPLE
path = 'C:/Users/qihus/Desktop/spyder/DataSources/archive'
Orders = pd.read_csv(path+'/List of Orders.csv') #all orders , cus_nam , _loc
Order_details = pd.read_csv(path+'/Order Details.csv') #items in order , amount , qnt, category
Sales = pd.read_csv(path+'/Sales target.csv') #total sales per category per month
#Clean
Orders = Orders.drop(Orders.index[500:])
Sales = Sales.rename(columns = {'Month of Order Date':'Date'})
##############################################################################

###Functions #########################################################################################################
def access_db(users_id=[]):
    allowed_users = list(range(1500,1600,5))
    if set(users_id).issubset(allowed_users) and len(users_id) > 0 :
        return("Access granted")
    else:
        not_granted = [item for item in users_id if item not in allowed_users]
        return("Access denied user number {0} cant access the database".format(not_granted))

def total_sales(month='Apr',year='18', category =''):
    date = str(month+'-'+year)
    return int(Sales.loc[(Sales['Date'] == date),['Target']].sum())
######################################################################################################################

#Launch a window
sg.theme('SystemDefault')
layout =[[sg.Text('Enter a command'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('Virtual Asisstant Box', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    if values[0] == 'goodbye'and event == 'Ok':
        break
    if 'our database' in values[0] and event == 'Ok':
        res = access_db(users_id=[1500,1510])
        #res = access_db(users_id=[1800])
        sg.PopupNonBlocking(res)
        obj.text2speech(text=res, lang='en')
        continue
    if 'total sales' in values[0] and event == 'Ok':
        res = access_db(users_id=[1500,1510])
        if res == 'Access granted':
            sg.PopupNonBlocking(total_sales())
            obj.text2speech(text='total sales = {0}'.format(total_sales()), lang='en')
        continue
    try:
        wolfram_res = next(client.query(values[0]).results).text
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res)
        obj.text2speech(text=wolfram_res, lang='en')
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res)
        obj.text2speech(text=wolfram_res, lang='en')
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        sg.PopupNonBlocking(wolfram_res)
        obj.text2speech(text=wolfram_res, lang='en')
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        sg.PopupNonBlocking("Wiki Result: "+wiki_res)
        obj.text2speech(text=wiki_res, lang='en')
    #engine.runAndWait()

    print (values[0])

window.close()

##ask google seach 

## Google calender / google drive apis 
#Set up OAuth 
import pickle
from apiclient.discovery import build
#from google.auth.transport.requests import Request
#from google.oauth2.credentials import Credentials
scopes = ['https://www.googleapis.com/auth/calendar']
credentials = pickle.load(open("C:/Users/qihus/Desktop/spyder/VAsst/token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
result = service.calendarList().list().execute()

result['items'][0]

#get appointment 
calendar_id = result['items'][0]['id']
time_zone = result['items'][0]['timeZone']
result = service.events().list(calendarId=calendar_id, timeZone=time_zone).execute()

#update appointment - change del 

#add appointment

