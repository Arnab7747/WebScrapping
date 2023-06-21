from bs4 import BeautifulSoup
import requests


url = "https://www.amazon.in/Sony-WH-XB910N-Cancelling-Headphones-transactions/dp/B09CG2P4Z2/?_encoding=UTF8&content-id=amzn1.sym.1283f517-922c-41ca-ab35-5002e1091e9b&ref_=pd_gw_pd_pss_gwp_d_0&th=1"
# pg = requests.get("https://www.amazon.in/s?k=headphones&ref=nb_sb_noss")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}

pg = requests.get(url=url, headers=headers)

cnt = pg.content

soup = BeautifulSoup(cnt, 'html.parser')


headline = soup.find_all('div', class_="a-section a-spacing-none", id="titleSection")
print(headline)
for title in headline:
    print(title.find('span').get_text())