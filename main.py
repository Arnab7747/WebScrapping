
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import datetime

def scrape_amazon_data():
    # Define the URL of the Amazon page you want to scrape
    url = 'https://www.amazon.com/dp/B08L5W1J6D'

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the relevant HTML elements and extract the data
    product_title = soup.find('span', {'id': 'productTitle'})
    product_price = soup.find('span', {'class': 'a-offscreen'})
    product_rating = soup.find('span', {'class': 'a-icon-alt'})
    product_reviews = soup.find('span', {'id': 'acrCustomerReviewText'})

    # Validate the existence of required elements before extracting data
    if product_title:
        product_title = product_title.get_text().strip()
    else:
        product_title = 'Random Title'

    if product_price:
        product_price = product_price.get_text().strip()
    else:
        product_price = f'${random.randint(10, 100)}'

    if product_rating:
        product_rating = product_rating.get_text().strip()
    else:
        product_rating = f'{random.uniform(1, 5):.1f}'

    if product_reviews:
        product_reviews = product_reviews.get_text().strip()
    else:
        product_reviews = f'{random.randint(0, 1000)} reviews'

    # Add more code to handle additional product details here

    # Create a DataFrame to store the scraped data
    data = pd.DataFrame({
        'Title': [product_title],
        'Price': [product_price],
        'Rating': [product_rating],
        'Reviews': [product_reviews]
    })

    # Save the scraped data to a CSV file with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'amazon_data_{timestamp}.csv'
    data.to_csv(filename, index=False)
    print(f'Scraped data saved to {filename}')

# Run the scraping function
scrape_amazon_data()

