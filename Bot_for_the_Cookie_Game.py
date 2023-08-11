# Game bot. Which play a online game: Cookie Clicker.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

URL = 'https://orteil.dashnet.org/cookieclicker/'
game_play = True
n = 0
TIME_CLICKING = 15

# connect to game
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get(URL)

cookies_accept = driver.find_element(By.CLASS_NAME, "fc-button-label")
cookies_accept.click()
driver.implicitly_wait(500)
choose_english = driver.find_element(By.ID, "langSelect-EN")
choose_english.click()
driver.implicitly_wait(500)


# Function to clik cookie
def button_clik():
    click_start = True
    start_time = int(time.time())
    while click_start:
        cookie_button = driver.find_element(By.ID, 'bigCookie')
        cookie_button.click()
        actual_time = int(time.time())
        if actual_time == (start_time+TIME_CLICKING):
            click_start = False


# function to check number
def price_check(price_to_check):
    money_dict = {'million': 1000000, 'billion': 100000000}
    price_text = price_to_check.split()

    number = float(price_text[0].replace(',', ''))

    if len(price_text) >= 2:
        number_name = price_to_check.split()[1]
        if number_name in money_dict:
            price = number * money_dict[number_name]
            return price
        else:
            price = number
            return price
    else:
        price = number
        return price


# Function to buy items
def buy_item():
    li = [number for number in range(20)]
    for i in li[::-1]:
        amount_text = driver.find_element(By.ID, 'cookies').text
        amount = price_check(amount_text)
        item_text = driver.find_element(By.ID, f'productPrice{i}')
        if item_text.text == '' or item_text.text == '???':
            item_price = 0
        else:
            item_price = float(price_check(item_text.text))

        if item_price == 0:
            pass
        elif item_price < amount:
            driver.find_element(By.ID, f'product{i}').click()


# Game
while game_play:
    time.sleep(1)
    print(f'Round {n}')
    n += 1
    button_clik()
    buy_item()
    if n == 100:
        game_play = False


time.sleep(10)
driver.quit()
