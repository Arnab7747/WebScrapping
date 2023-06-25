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

header_list = []
price_list = []
review_list = []

headline = soup.find_all('div', class_='a-section a-spacing-none a-spacing-top-small s-title-instructions-style')
print(headline)
for title in headline:
    header = title.h2.text
    header_list.append(header)

priceList = soup.find_all('span', class_='a-price-whole')
for price in priceList:
    price_list.append(price.text)

reviews = soup.find_all('span', class_='a-icon-alt')
for review in reviews:
    review_list.append(review.text)

# minimum length as unneccesy data comming and difficult to merge as array should be of same 
min_length = min(len(header_list), len(price_list), len(review_list))

# Truncate the lists to the minimum length
header_list = header_list[:min_length]
price_list = price_list[:min_length]
review_list = review_list[:min_length]

df = pd.DataFrame({
    'Header': header_list,
    'Price': price_list,
    'Review': review_list
})

print(df)
