from typing import Text
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://web.whatsapp.com")
input("Press any key to continue")


def forward(phoneno, count):
    if(count % 5 == 0 and count!=0 ):
        input("Forward to 5 People?")
        driver.find_element_by_xpath(
            '// *[ @ id = "app"] / div[1] / span[2] / div[1] / span / div[1] / div / div / div / div / div / span / div / div / div / span').click()

        print("5 Participant limit reached, please select the messages to forward")
        input("Forwarding Set??? Press any key to start")


    try:
        driver.find_element_by_xpath(
             '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div/div[1]/div/label').click()
        time.sleep(1)
        print("1")
        time.sleep(5)
        driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div/div[1]/div/label/div/div[2]').send_keys(phoneno)
        time.sleep(5)
        print("2")
        driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div/div[2]/div[1]/div/div/div[6]/div/div[2]/div/div[2]/div[1]/div/span/span').click()

    except Exception as e:

        time.sleep(1)
        print("3")
        driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div/div[1]/div/label/div/div[2]').clear()
        time.sleep(1)
        print("4")
        print(e)
        print(f"''''''''''''Number-missing {phoneno + str(count)}'''''''''''''")

count = -1
with open('./phoneno.csv', 'r')as myfile:


    while myfile:

        phoneno = myfile.readline()
        if phoneno == "":
            print("All Messages Sent")
            break
        count = count + 1
        forward(phoneno, count)

# CloseButton ------>   //*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div/div[1]/div/span/button
# SentButton ------>   //*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div/span/div/div/div/span
# ArrowDown ------>   //*[@id="main"]/div[3]/div/div/div[3]/div[5]/div[1]/div/span/div/div
# FwdButton ----->   //*[@id="app"]/div[1]/span[4]/div/ul/div/li[3]/div[1]

