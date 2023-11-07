from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Player import *
import time
import pandas as pd

def GrabAgents(browser):
    p = Player()
    players = []

    team_table_class = "teams"
    try:
        WebDriverWait(browser, timeout=20).until(EC.presence_of_element_located((By.XPATH, f"//div[@class={team_table_class}]")))
        players_grid = browser.find_element(By.XPATH, f"//div[@class={team_table_class}]")
    except:
        return -1
    else:
        return players_grid



def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # Removes CSRI error message

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    browser.get('http://spotrac.com/mlb/free-agents')

    close_button = "mc-closeModal"

    WebDriverWait(browser,timeout=20).until(EC.presence_of_element_located((By.XPATH,f'//div[@class={close_button}]')))
    browser.find_element(By.XPATH, '//div[@class="mc-closeModal"]').click()

    time.sleep(5)

    browser.quit()


if __name__ == '__main__':
    main()
