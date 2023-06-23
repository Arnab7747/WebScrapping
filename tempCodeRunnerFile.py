
priceList = soup.find_all('span', class_='a-price-whole')

df = pd.DataFrame(priceList)
# print(df.info())
print(df)

reviews = soup.find_all('span',class_='a-icon-alt')
df2 = pd.DataFrame(reviews)
print(df2)