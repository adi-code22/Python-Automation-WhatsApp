from typing import Text
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

from cprogmessage import message0
from cprogmessage import message1

from cprogmessage import message6
from cprogmessage import message7
from cprogmessage import message8
from cprogmessage import message9
from cprogmessage import message10
from cprogmessage import message11
from cprogmessage import message12
from cprogmessage import message13
from cprogmessage import message14
from cprogmessage import message15

from cprogmessage import message35
from cprogmessage import message36

from cprogmessage import message38

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://web.whatsapp.com")
input("Press any key to continue")


# def send(msg,phonen):
#     driver.get(f"https://web.whatsapp.com/send?phone=91{phonen}")
#     time.sleep(5)


def text(message0, message6, message7, message8, message10,
         message11, message12, message13, message14, message35, message36, message38, phoneno):
    # Greetings

    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message0)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message1)

    # Session on digital electronics
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message7)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message6)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message8)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message9)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)

    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message10)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)

    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message11)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message12)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message13)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message14)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    # Thanks and Regards
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message35)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message36)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message38)

    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()


def send(message0, message6, message7, message8, message10,
         message11, message12, message13, message14, message35, message36, message38, phoneno):
    try:
        driver.get(f"https://web.whatsapp.com/send?phone=91{phoneno}")
    except:
        print(".")

    time.sleep(5)

    try:
        text(message0, message6, message7, message8, message10,
             message11, message12, message13, message14, message35, message36, message38, phoneno)
    except:
        try:
            time.sleep(8)
            text(message0, message6, message7, message8, message10,
                 message11, message12, message13, message14, message35, message36, message38, phoneno)
        except:
            print(phoneno)

    time.sleep(3)


count = 0
with open('./phoneno.csv', 'r')as myfile:
    while myfile:
        phoneno = myfile.readline()
        if phoneno == "":
            print("All Messages Sent")
            break
        count = count + 1
        send(message0, message6, message7, message8, message10,
             message11, message12, message13, message14, message35, message36, message38, phoneno)
        print(count)
