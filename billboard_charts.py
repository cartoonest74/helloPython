# from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
from Billboard import Billboard

url = f"https://www.billboard.com/charts/hot-100/"
res = requests.get(url)
soup = bs(res.text,'html.parser')

chart_list = soup.select('div.o-chart-results-list-row-container>ul') 

print('Rank\tTitle\tSinger\t')
bilbords =[]
for i in chart_list:
    bilbords.append(Bilbord(i))

with open('bilbord_hot100.csv','w', encoding='UTF-8') as file:
    file.write("Rank\tTitle\tSinger\n")
    for info in  bilbords:
        file.write(info.to_str() + "\n")