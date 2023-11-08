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

    try:
        WebDriverWait(browser, timeout=20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="teams"]')))
        players_grid = browser.find_element(By.XPATH, '//div[@class="teams"]')
    except:
        return -1
    else:

        rows = players_grid.find_elements(By.TAG_NAME, "tr")
        lst_of_players = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 3:
                name = cells[0].text
                position = cells[2].text
                if len(cells) > 7:
                    age = cells[3].text
                    bats = cells[4].text
                    throws= cells[5].text
                    if len(cells) > 9:
                        team = cells[6].text
                        prev_salary = cells[7].text
                        expect_salary = cells[8].text

                        player = Player(name, age, position, prev_salary, expect_salary, team, [bats, throws])
                        lst_of_players.append(player)
                    else:
                        player = Player(name=name, position=position)
                        lst_of_players.append(player)
                else:
                        player = Player(name=name, position=position)
                        lst_of_players.append(player)

        return lst_of_players
        



def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # Removes CSRI error message

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    browser.get('http://spotrac.com/mlb/free-agents')

    WebDriverWait(browser,timeout=20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="mc-closeModal"]')))
    browser.find_element(By.XPATH, '//div[@class="mc-closeModal"]').click()

    time.sleep(5)

    free_agents = GrabAgents(browser)
    for agent in free_agents:
        print(agent)

    browser.quit()


if __name__ == '__main__':
    main()
