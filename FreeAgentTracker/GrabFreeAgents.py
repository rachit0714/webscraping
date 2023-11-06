from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import pandas as pd

def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # Removes CSRI error message

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    browser.get('http://spotrac.com/mlb/free-agents')
    
    WebDriverWait(browser,timeout=20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="mc-closeModal"]')))
    browser.find_element(By.XPATH, '//div[@class="mc-closeModal"]').click()

    time.sleep(5)

    browser.quit()


if __name__ == '__main__':
    main()
