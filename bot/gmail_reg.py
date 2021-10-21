from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class GmailBot:
    def __init__(self,driver,url,number,firstName,lastName,randMail,randPass):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(driver, options = self.options)
        self.driver.get(url)
        self.create_account()
        self.fill_form(firstName,lastName,randMail,randPass)
        time.sleep(5)
        self.phone_num(number)

    def create_account(self):
        create = self.driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button')
        create.click()
        for_me = self.driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/ul/li[1]')
        for_me.click()

    def fill_form(self,firstName,lastName,randMail,randPass):
        f_name = self.driver.find_element_by_xpath('//*[@id="firstName"]')
        f_name.send_keys(firstName)
        l_name = self.driver.find_element_by_xpath('//*[@id="lastName"]')
        l_name.send_keys(lastName)
        user_name = self.driver.find_element_by_xpath('//*[@id="username"]')
        user_name.send_keys(randMail)
        pswd = self.driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input')
        pswd.send_keys(randPass)
        repeat = self.driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
        repeat.send_keys(randPass)
        next = self.driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button')
        next.click()

    def phone_num(self,number):
        num = self.driver.find_element_by_xpath('//*[@id="phoneNumberId"]')
        num.send_keys(number)
        next = self.driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        next.click()




