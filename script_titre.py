import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_reddit(driver, driver2, driver3):
    url1 = "https://www.reddit.com/"
    url2 = "https://www.youtube.com"
    url3 = "https://play.pokemonshowdown.com"
    driver.set_window_size(1600, 1200)
    driver.get(url1)
    driver2.set_window_size(1600, 1200)
    driver2.get(url2)
    driver3.set_window_size(1600, 1200)
    driver3.get(url3)

    title = driver.title
    title2 = driver2.title
    title3 = driver3.title
    taille = ""

    L1 = len(title)
    L2 = len(title2)
    L3 = len(title3)

    tab =[L1, L2, L3]

    for i in tab :
        taille=max(tab)
        



    button = driver.find_elements(by=By.ID, value="focus-Popular")
    if not button:
            print("window is too small")
    else:
        button[0].click()
        time.sleep(5)
        driver.quit()




    #cette méthode affichera les 2 url des 2 titres les plus grands si ils ont par hasard la même taille

    to_return=[]
    if L1 == taille :
        # print (url1)
        to_return.append(url1)
    if L2 == taille :
        # print (url2)
        to_return.append(url2)
    if L3 == taille :
        # print (url3)
        to_return.append(url3)

    print(to_return)
    return to_return



def create_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    #chrome options.add_argument('headless')
    return webdriver.Chrome(options = chrome_options)

test_reddit(create_chrome_driver(), create_chrome_driver(), create_chrome_driver())


