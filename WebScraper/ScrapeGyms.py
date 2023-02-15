import requests
from bs4 import BeautifulSoup

'''
BeautifulSoup is a Python library used for web scraping and data extraction 
from HTML and XML files. It is designed to make it easy to parse and extract
data from HTML and XML documents, even if they are not well-formed. 
The library provides methods to search and manipulate the HTML/XML document
tree, allowing you to extract the data you need. The library also provides 
options to specify the parser to use, so you can choose a parser that best 
suits your needs.

BeautifulSoup provides a simple and elegant way to extract data from 
web pages, making it a popular choice for web scraping projects in Python. 
It is easy to use and provides a lot of functionality out of the box, 
making it a great choice for both beginners and experienced users.
'''

def scrape_gyms(city):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    url = "https://www.google.com/maps/dir//gym+" + city
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    gyms = soup.find_all("div", class_="section-result-content")
    for gym in gyms:
        name = gym.find("span", class_="section-result-title").get_text()
        address = gym.find("span", class_="section-result-location").get_text()
        print(name, address)
if __name__ == "__main__":
    city = input("Enter a city name: ")
    print("Gyms in", city, ":")
    scrape_gyms(city)
