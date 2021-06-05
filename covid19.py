# Get the details about the covid situation in india
import requests
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier
import pandas as pd
from re import search

header = {"User-Agent":"Mozilla"}
req = requests.get("https://covidindia.org/", headers = header)
obj = bs(req.text, 'html.parser')
table_body=obj.find('tbody')
rows = table_body.find_all('tr')
state=input("State Name : ")
a=state.capitalize()
df = pd.DataFrame() 
case_dict = {"State":[],"Total Cases":[],"Recoveries":[], "Death":[]}

for row in rows:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    #print(cols)
    if(cols[0]=="Unassigned"):
        pass
    else:
        case_dict["State"].append(cols[0])
        case_dict["Total Cases"].append(cols[1])
        case_dict["Recoveries"].append(cols[2])
        case_dict["Death"].append(cols[3])
    
    if(cols[0]==a or search(a, cols[0])):
        notifier = ToastNotifier()
        message  = "Total Cases - "+ cols[1]+"\nRecoveries - "+cols[2]+"\nDeath - "+cols[3]
        message
        notifier.show_toast(title="COVID-19 Update for "+cols[0], msg=message, duration=5, icon_path=r"virus.ico")
        
df = pd.DataFrame(case_dict)
df.to_excel('corona_results.xlsx', index = False) 
