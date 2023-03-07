import requests
import bs4
import spotify
import webbrowser
get  = requests.get(url ="https://www.billboard.com/charts/hot-100/" )
soup = bs4.BeautifulSoup(get.text,"html.parser")

name = soup.find_all(class_="o-chart-results-list-row-container")
store = {}
t= []
s = []
for test in name:
    t.append(test.h3.get_text(strip=True))
    s.append(test.h3.find_next('span').get_text(strip=True))
store = {s[i]:t[i] for i in range(len(t)) }
#print(store)
with open("top_100_songs.txt",mode="w") as file:
    i = 1
    for keys,values in store.items():
        file.write(f"{i})name: {keys} -> {values} \n")
        i+=1


