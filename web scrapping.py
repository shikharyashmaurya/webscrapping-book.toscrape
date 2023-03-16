import requests
import csv
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://books.toscrape.com/'
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the book titles, prices, and links
books = soup.find_all('article', class_='product_pod')

# Open a CSV file for writing
with open('books.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Title', 'Price', 'Link'])

    # Write the book data to the CSV file
    for book in books:
        title = book.h3.a.attrs['title']
        price = book.select('div p.price_color')[0].get_text()
        link = book.h3.a.attrs['href']
        book_url = url + link.replace('../../', '')
        writer.writerow([title, price, book_url])

print('Book data exported to books.csv file.')
