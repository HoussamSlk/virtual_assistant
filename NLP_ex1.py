# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 12:10:13 2021

@author: qihus
"""

#Importing required libraries: 
import pandas as pd
import JarvisAI

#Loading Datasouce
path = 'C:/Users/qihus/Desktop/spyder/DataSources/archive'
Orders = pd.read_csv(path+'/List of Orders.csv') #all orders , cus_nam , _loc
Order_details = pd.read_csv(path+'/Order Details.csv') #items in order , amount , qnt, category
Sales = pd.read_csv(path+'/Sales target.csv') #total sales per category per month

Orders = Orders.drop(Orders.index[500:])
Sales = Sales.rename(columns = {'Month of Order Date':'Date'})


###############################################################################
##Simple Virtual Assitant using Jarvis AI Library
obj = JarvisAI.JarvisAssistant()
obj.text2speech(text="Hello my name is JarvisAI , how can i help you? ", lang='en')
response = obj.mic_input_ai(record_seconds=10) # mic_input() can be also used

if 'date' in response:
    res = obj.tell_me_date()
    obj.text2speech(text=res, lang='en')
    
if 'time' in response:
    res = obj.tell_me_time()
    obj.text2speech(text=res, lang='en')

if 'data' in response:
    access_db(users_id=["3000","1512",'1500'])
    

###Functions #########################################################################################################
def access_db(users_id=[]):
    allowed_users = ['1500','1515','1520','1570']
    if set(users_id).issubset(allowed_users) and len(users_id) > 0 :
        obj.text2speech(text="Access granted", lang='en')
    else:
        not_granted = [item for item in users_id if item not in allowed_users]
        obj.text2speech(text="Access denied user number {0} cant access the database".format(not_granted), lang='en')

######################################################################################################################



obj.website_opener("gmail")

news = obj.news()
obj.text2speech(text=news[1], lang='en')

 res= obj.weather(city='Kuwait')
 obj.text2speech(text=res, lang='en')
 
 res = obj.tell_me(topic='weather in amsterdam in January 2011')
 obj.text2speech(text=res, lang='en')