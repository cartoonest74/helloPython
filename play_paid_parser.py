from bs4 import BeautifulSoup as bs
import requests
from Billboard import Billboard

url = "https://www.billboard.com/charts/hot-100/"
res = requests.get(url)

soup = bs(res.text,'html.parser')
chart_list = soup.select('div.o-chart-results-list-row-container>ul')

charts = []
for i in chart_list:
    charts.append(Billboard(i))

with open('billboard_hot100.csv','w', encoding='utf-8') as file:
    file.write('Rank\tTitle\tSinger\n')
    for billboard in charts:
        file.write(billboard.to_str() + '\n')