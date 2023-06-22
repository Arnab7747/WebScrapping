from bs4 import BeautifulSoup
import requests

url = input("Enter url :")
print(" This is the website link that you entered", url)

# pg = requests.get("https://www.amazon.in/s?k=headphones&ref=nb_sb_noss")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}

pg = requests.get(url=url, headers=headers)

cnt = pg.content

soup = BeautifulSoup(cnt, 'html.parser')


# headline = soup.find_all('div', class_="a-section a-spacing-none", id="titleSection")
# print(headline)
# for title in headline:
#     print(title.find('span').get_text())
title = soup.find('span', class_='a-size-large product-title').text
price = soup.find('span', class_='a-price a-color-price').text
rating = soup.find('span', class_='a-icon-alt').text
number_of_reviews = soup.find('span', class_='a-size-small a-color-secondary').text

    
print("title :",title)
print('price :', price)
print('rating:', rating)
print('number_of_reviews:',number_of_reviews)
    

