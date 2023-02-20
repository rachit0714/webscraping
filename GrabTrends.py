from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import openai
import os


def scrapeTrends(driver):
    
    # Navigate to Google Trends website
    driver.get('https://trends.google.com/trends/')

    time.sleep(2)

    #open menu
    menu = driver.find_element("id", "sidenav-menu-btn")
    menu.click()
    
    trending_button = driver.find_element("id", "sidenav-list-group-trends")
    trending_button.click()

    try:
        wrapper = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "feed-list-wrapper"))
    )
    except:
        print("wrapper did not load")
        driver.quit()

    tags = wrapper.find_elements(By.TAG_NAME, "md-list")
    trends = []
    for tag in tags:
        trend = tag.find_element(By.CLASS_NAME, "details-top")
        trends.append(trend.text)
    return trends

def generateArticle(prompt, api_key):
    model_engine = "text-davinci-002"
    openai.api_key = api_key
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=3072,
        n=1,
        stop=None,
        temperature=0.7,
    )
    article = response.choices[0].text
    return article

def main():
    # Open a new Chrome browser window
    driver = webdriver.Chrome()
    trends = scrapeTrends(driver)
    
    api_key = os.environ.get("OPENAI_API_KEY")
    for i in range(10):
        trend = trends[i]
        article = generateArticle(trend, api_key)
        print(f"Generated an Article for {trend} below")
        print(article)
        time.sleep(10*60)

    time.sleep(5)
    # Close the browser window
    driver.quit()

if __name__ == "__main__":
    main()
