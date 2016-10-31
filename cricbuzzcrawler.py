
import requests, bs4

res = requests.get("http://www.cricbuzz.com")
soup = bs4.BeautifulSoup(res.text, "html.parser")
element = soup.find_all('div', {'class': 'cb-col cb-col-25 cb-mtch-blk'})
country = str(input("enter a country whose score you want to know: "))
for i in range (0, 5):
    if country in str(element[i].getText()):
        msg = element[i].getText()
        break
    else:
        msg="scores for the country you requested not found."

