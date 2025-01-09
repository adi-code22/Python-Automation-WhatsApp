import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyperclip
from dataclasses import dataclass
from typing import List

@dataclass
class Message:
    content: str
    add_newline: bool = True

class WhatsAppAutomation:
    def __init__(self, image_path: str, messages: List[Message]):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.image_path = os.path.abspath(image_path)
        self.messages = messages

    def start(self):
        self.driver.get("https://web.whatsapp.com")
        input("Scan QR code and press Enter to continue...")

    def send_image(self):
        try:
            pyperclip.copy(self.image_path)

            attachment_btn = self.wait.until(EC.element_to_be_clickable(
                 (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div/button')))
            attachment_btn.click()

            attachment_btn2 = self.wait.until(EC.presence_of_element_located(
                 (By.XPATH, '//*[@id="app"]/div/span[5]/div/ul/div/div/div[2]/li/div/input')))
            attachment_btn2.send_keys(r"/Users/adityakrishnan/Documents/Git/Python-Automation-WhatsApp/image.jpeg")
            
        
            time.sleep(1)  # Wait for paste
            
        except Exception as e:
            raise Exception(f"Failed to send image: {str(e)}")
        

    def send_message(self, message: Message):
        try:
            # //*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p
            msg_box = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#app > div > div.x78zum5.xdt5ytf.x5yr21d > div > div.x10l6tqk.x13vifvy.x17qophe.x78zum5.xh8yej3.x5yr21d.x6ikm8r.x10wlt62.x47corl > div.x9f619.x1n2onr6.x5yr21d.x6ikm8r.x10wlt62.x17dzmu4.x1i1dayz.x2ipvbc.x1w8yi2h.xyyilfv.x1iyjqo2.xa1v5g2 > span > div > div > div > div.x1n2onr6.xyw6214.x78zum5.x1r8uery.x1iyjqo2.xdt5ytf.x1hc1fzr.x6ikm8r.x10wlt62.x1tkvqr7 > div > div.x78zum5.x1iyjqo2.xs83m0k.x1r8uery.xdt5ytf.x1qughib.x6ikm8r.x10wlt62 > div.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.x78zum5.xozqiw3.x1oa3qoh.x12fk4p8.xeuugli.x2lwn1j.xl56j7k.x1q0g3np.x6s0dn4.x1n2onr6.xo8q3i6.x1y1aw1k.xwib8y2.xkhd6sd.x4uap5 > div > div > div.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.x78zum5.xozqiw3.x1oa3qoh.x12fk4p8.xeuugli.x2lwn1j.x1nhvcw1.x1q0g3np.x1cy8zhl.x9f619.xh8yej3.x1ba4aug.x1iorvi4.x1pi30zi.xjkvuk6.x1swvt13.x7nbn6e.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c > div.x1n2onr6.xh8yej3.x1k70j0n.x11i5rnm.xzueoph.x1mh8g0r.xisnujt.xzwifym.x1vvkbs.x126k92a.x1hx0egp.lexical-rich-text-input > div.x1hx0egp.x6ikm8r.x1odjw0f.x1k6rcq7.x1lkfr7t > p')))
            msg_box.send_keys(message.content)
            
            if message.add_newline:
                msg_box.send_keys(Keys.SHIFT, Keys.ENTER, Keys.SHIFT, Keys.ENTER)
            
            return True
        except Exception as e:
            print(f"Failed to send message: {e}")
            return False

    def send_to_number(self, phone_number: str):
        try:
            self.driver.get(f"https://web.whatsapp.com/send?phone=91{phone_number}")
            time.sleep(10)
            
            self.send_image()
            for message in self.messages:
                if not self.send_message(message):
                    raise Exception("Message sending failed")
                    
            # send_btn = self.wait.until(EC.element_to_be_clickable(
            #     (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div')))
            # send_btn.click()
            
            time.sleep(3)
            return True
        except Exception as e:
            print(f"Failed to send to {phone_number}: {str(e)}")
            return False

    def process_numbers(self, csv_path: str):
        success_count = 0
        fail_count = 0
        
        with open(csv_path, 'r') as file:
            phone_numbers = [line.strip() for line in file if line.strip()]
            
        total = len(phone_numbers)
        for i, number in enumerate(phone_numbers, 1):
            print(f"Processing {i}/{total}: {number}")
            if self.send_to_number(number):
                success_count += 1
            else:
                fail_count += 1
                
        print(f"\nSummary:\nSuccessful: {success_count}\nFailed: {fail_count}")

    def close(self):
        self.driver.quit()

def main():
    messages = [
        Message("Hello!"),
        Message("This is a test message"),
        # Add more messages
    ]
    
    automation = WhatsAppAutomation(
        image_path="/Users/adityakrishnan/Documents/Git/Python-Automation-WhatsApp/image.jpeg",
        messages=messages
    )
    
    try:
        automation.start()
        automation.process_numbers("./phoneno.csv")
    finally:
        automation.close()

if __name__ == "__main__":
    main()