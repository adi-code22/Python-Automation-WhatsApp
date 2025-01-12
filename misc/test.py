# from typing import Text
# from selenium import webdriver
# import time
# from message import message
#
# driver = webdriver.Chrome(executable_path='chromedriver.exe')
# driver.get("http://darkprotocol.rf.gd/?i=1")
# input("Press any key to continue")
#
#
# def send(msg, phonen):
#     driver.get("http://darkprotocol.rf.gd/?i=1")
#     time.sleep(10)
#     while(True):
#         for i in range(10):
#             for i in range(10):
#                 for i in range(10):
#
#                     driver.find_element_by_xpath("(//button[@class='flickity-prev-next-button next'])[4]").click()
#
#
#                 for i in range(1):
#                     driver.find_element_by_xpath("(//button[@class='flickity-prev-next-button next'])[3]").click()
#             driver.find_element_by_xpath("(//button[@class='flickity-prev-next-button next'])[2]").click()
#         driver.find_element_by_xpath("(//button[@class='flickity-prev-next-button next'])[1]").click()
#
#
#
#
#
#
#
# # def text(msg):
#
#     #driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
#
#
# # def send(msg, phonen):
# #     driver.get(f"https://web.whatsapp.com/send?phone=91{phonen}")
# #     time.sleep(7)
#
#
# with open('./phoneno.csv', 'r')as myfile:
#     while myfile:
#         phoneno = myfile.readline()
#         if phoneno == "":
#             print("All Messages Sent")
#             break
#         send(message, phoneno)
#         print(phoneno)
#
#
#
