from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.amazon.in/s?bbn=1389401031&rh=n%3A1389401031%2Cp_89%3AOnePlus&dc&qid=1687486000&rnid=3837712031&ref=lp_1389401031_nr_p_89_0"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}

pg = requests.get(url=url, headers=headers)
cnt = pg.content

soup = BeautifulSoup(cnt, 'html.parser')

headline = soup.find_all('div',class_='a-section a-spacing-none a-spacing-top-small s-title-instructions-style')
for title in headline:
    header= title.h2.text
    
    print(header)


priceList = soup.find_all('span', class_='a-price-whole')

df = pd.DataFrame(priceList)

print(df)

ratings = soup.find_all('span',class_='a-icon-alt')
df2 = pd.DataFrame(ratings)
print(df2)

reviews =soup.find_all('div',class_='review-collapsed')
for re in reviews:
    x=re.text
    print(x)


