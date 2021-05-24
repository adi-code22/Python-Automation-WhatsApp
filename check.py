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


def text(message0, message1, message2, message3, message4, message5, message6, message7, message8, message9, message10,
         message11, message12, message13, message14, message15, message16, message17, message18, message19, message20,
         message21, message22, message23, message24, message25, message26, message27, message28, message29, message30,
         message31, message32, message33, message34, message35, message36, message37, message38, phoneno):
    print("Hi")


def send(phoneno):
    try:
        # driver.get(f"https://web.whatsapp.com/send?phone=91{phoneno}")
        driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').click()
        driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(phoneno)
        check = input("Enter Y/N")
        if check == "N":
            print(phoneno)
        driver.find_element_by_xpath('// *[ @ id = "side"] / div[1] / div / button').click()


    except:
        print(phoneno + "Error Occurred in driver")




with open('./phoneno.csv', 'r')as myfile:
    count = 1
    driver.get(f"https://web.whatsapp.com/send?phone=917034480492")
    time.sleep(10)
    while myfile:
        phoneno = myfile.readline()

        if phoneno == "":
            print("All Messages Sent")
            break

        send(phoneno)

#INPUT : //*[@id="side"]/div[1]/div/label/div/div[2]
#bACK : //*[@id="side"]/div[1]/div/button