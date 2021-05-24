from typing import Text
from selenium import webdriver
import time


from selenium.webdriver.common.keys import Keys

from message import message0
from message import message1
from message import message2
from message import message3
from message import message4
from message import message5
from message import message6
from message import message7
from message import message8
from message import message9
from message import message10
from message import message11
from message import message12
from message import message13
from message import message14
from message import message15
from message import message16
from message import message17
from message import message18
from message import message19
from message import message20
from message import message21
from message import message22
from message import message23

from message import message24
from message import message25
from message import message26
from message import message27
from message import message28
from message import message29
from message import message30
from message import message31
from message import message32
from message import message33
from message import message34
from message import message35
from message import message36
from message import message37
from message import message38


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://web.whatsapp.com")
input("Press any key to continue")


# def send(msg,phonen):
#     driver.get(f"https://web.whatsapp.com/send?phone=91{phonen}")
#     time.sleep(5)

def image():
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div').click()
    driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input').send_keys(
        r"C:\Users\91703\Desktop\whatsappbot\image.jpeg")
    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div').click()


def text(message0, message1, message2, message3, message4, message5, message6, message7, message8, message9, message10,
         message11, message12, message13, message14, message15, message16, message17, message18, message19, message20,
         message21, message22, message23, message24, message25, message26, message27, message28, message29, message30,
         message31, message32, message33, message34, message35, message36, message37, message38, phoneno):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message0)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message2)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message4)
    # Basics of Programming
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message6)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message7)
    # Session on working of home appliances and energy meter
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message9)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message10)
    # Session on digital electronics
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message12)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message13)
    # Session on dynamic architecture
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message15)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message16)
    # Introduction to App development
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message18)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message19)
    # Introduction to Web development
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message21)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message22)
    # Session on machine learning
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message24)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message25)
    # Introduction to ethical hacking
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message27)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message28)
    # Register and link
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message30)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message31)
    # Kindly Share
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message33)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    # Thanks and Regards
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message35)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message36)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message37)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message38)




    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()


def send(message0, message1, message2, message3, message4, message5, message6, message7, message8, message9, message10,
         message11, message12, message13, message14, message15, message16, message17, message18, message19, message20,
         message21, message22, message23, message24, message25, message26, message27, message28, message29, message30,
         message31, message32, message33, message34, message35, message36, message37, message38, phoneno):
    try:
        driver.get(f"https://web.whatsapp.com/send?phone=91{phoneno}")
    except:
        print(phoneno + "Error Occured in driver")

    time.sleep(15)

    try:
        image()
    except:
        print(phoneno + "Error Occured in uploading image")


    try:
        text(message0, message1, message2, message3, message4, message5, message6, message7, message8, message9,
             message10,
             message11, message12, message13, message14, message15, message16, message17, message18, message19,
             message20,
             message21, message22, message23, message24, message25, message26, message27, message28, message29,
             message30,
             message31, message32, message33, message34, message35, message36, message37, message38, phoneno)
    except:
        print(phoneno + "Error Occured in adding Text")

    time.sleep(5)


with open('./phoneno.csv', 'r')as myfile:
    count = 1
    while myfile:
        phoneno = myfile.readline()
        if phoneno == "":
            print("All Messages Sent")
            break

        send(message0, message1, message2, message3, message4, message5, message6, message7, message8, message9,
             message10, message11, message12, message13, message14, message15, message16, message17, message18,
             message19, message20, message21, message22, message23, message24, message25, message26, message27,
             message28, message29, message30, message31, message32, message33, message34, message35, message36,
             message37, message38, phoneno)

