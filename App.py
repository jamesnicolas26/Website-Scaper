import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        return None

url = input('Enter URL to scrape: ')
soup = scrape_website(url)

if soup:
    print("Website Title: ", soup.title.string)
    print("\nAll Paragraphs:")
    for paragraph in soup.find_all('p'):
        print(paragraph.get_text())
else:
    print("Failed to retrieve the website.")