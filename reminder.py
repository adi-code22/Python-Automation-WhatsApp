from typing import Text
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

from reminder_short import message0
from reminder_short import message1

from reminder_short import message7
from reminder_short import message8
from reminder_short import message9
from reminder_short import message10
from reminder_short import message11
from reminder_short import message12
from reminder_short import message13


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://web.whatsapp.com")
input("Press any key to continue")


# def send(msg,phonen):
#     driver.get(f"https://web.whatsapp.com/send?phone=91{phonen}")
#     time.sleep(5)


def text(message0,message7, message8, message10,message11, message12, message13, phoneno):

    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message0)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message7)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message8)
    # Basics of Programming
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message10)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message11)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message12)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message13)

    # Joining Info

    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()


def send(message0,message7, message8, message10,message11, message12, message13, phoneno):
    try:
        driver.get(f"https://web.whatsapp.com/send?phone=91{phoneno}")
    except:
        print(".")

    time.sleep(5)

    try:
        text(message0,message7, message8, message10,message11, message12, message13, phoneno)
    except:
        try:
            time.sleep(8)
            text(message0,message7, message8, message10,message11, message12, message13, phoneno)
        except:
            print({phoneno})

    time.sleep(3)


count = 2
with open('./phoneno.csv', 'r')as myfile:
    while myfile:
        phoneno = myfile.readline()
        if phoneno == "":
            print("All Messages Sent")
            break
        count = count + 1
        send(message0,message7, message8, message10,message11, message12, message13, phoneno)
        print(count)
