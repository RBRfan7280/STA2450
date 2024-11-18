from asyncio import wait_for
from time import sleep

from click import pause
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)
driver.get('https://www.demoblaze.com')
login = driver.find_element(By.ID, 'login2')
login.click()

username = driver.find_element(By.ID, 'loginusername')
username.send_keys('NateF')

password = driver.find_element(By.ID, 'loginpassword')
password.send_keys('5567')

loginClick = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
loginClick.click()

def login(username, password):
    login = driver.find_element(By.ID, 'login2')
    login.click()
    sleep(1)
    un = driver.find_element(By.ID, 'loginusername')
    pw = driver.find_element(By.ID, 'loginpassword')

    un.send_keys(username)
    pw.send_keys(password)
    sleep(1)

    loginClick = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
    loginClick.click()

login('NateF','5567')

def canvas_login():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://canvas.web.baylor.edu/')
    sleep(1)

    loginCLick = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/main/div/div/article/div/div[1]/div/div/div/div[2]/a[1]')
    loginCLick.click()
    sleep(1)

    un = driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[1]/input')
    un.send_keys('Nate_Friedlander1')

    pw = driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[2]/input')
    pw.send_keys('Nathancat1$$7280$')
    sleep(1)

    loginClick2 = driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[5]/button')
    loginClick2.click()

    input("Please complete the 2FA and press Enter to continue...")

    yes_device = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div[2]/div[3]/button')
    yes_device.click()

canvas_login()