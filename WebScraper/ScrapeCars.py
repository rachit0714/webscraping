from bs4 import BeautifulSoup
import requests

def scrapeSite(link):
    car = input('Car make: ')
    scrapeCars(link, car)

def scrapeCars(website, make):
    print('Do you want a new car? y/Y for yes or n/N for used')
    if (input('>') in ['y', 'Y']):
        html_text = requests.get(f'https://www.{website}/cars-for-sale/new-cars/{make}').text
        soup = BeautifulSoup(html_text, 'lxml')
        print('soup has been processed')
        vehicles = {}
        names = soup.find_all('h2',class_='text-bold text-size-400 text-size-sm-500 link-unstyled')
        prices = soup.find_all('span', class_='first-price')
        for i in range(len(names)):
            vehicles[names[i]] = prices[i]
        for name, price in vehicles.items():
            print(f'{name.text} for ${price.text}')


def main():
    print('What is the site you want to scrape? ')
    site = input('>')
    scrapeSite(site)

if __name__ == '__main__':
    main()