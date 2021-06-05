# Get a list of the top 100 best movies on imdb
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from re import search

pd.set_option("display.max_rows", None, "display.max_columns", None)

url = requests.get("https://www.imdb.com/list/ls091520106/")
requests=url.text
soup=bs(requests,"html.parser")
soup.title.text
movies=soup.findAll('div',{'class':'lister-item mode-detail'})
first_movie=movies[0]
first_movie.h3.a.text0
first_movie.find('span',{"class":"lister-item-year text-muted unbold"}).text[1:5]
first_movie.find('span',{"class":"ipl-rating-star__rating"}).text.strip()
first_movie.find('div',{"class":"inline-block ratings-metascore"}).span.text.strip()

Name=[]
Year=[]
Rating=[]
Meta_score = []
j=0
for i in movies:
    Name.append(i.h3.a.text)
    Year.append(i.find('span',{"class":"lister-item-year text-muted unbold"}).text[1:5])
    Rating.append(i.find('span',{"class":"ipl-rating-star__rating"}).text.strip())

data = list(zip(Name,Year,Rating))

df = pd.DataFrame(data,columns=["Name","Year","Rating"])
print(df)
df.to_excel('imdb.xlsx', index = False) 