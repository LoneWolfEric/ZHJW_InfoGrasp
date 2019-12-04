from selenium import webdriver
from bs4 import BeautifulSoup
import hashlib
import time

class Spider(object):

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=chrome_options)

    # 访问登陆页面，获取下载验证码
    def get_CAPTCHA(self):
        pass

    # 输入学号密码验证码，登陆
    def login(self):
        pass

    # 进入登陆页面，获取个人信息
    def get_personl_info(self):
        pass

    # 断开连接
    def logout(self):



        client.quit()
        pass

    def run(self):
        self.get_CAPTCHA()
        self.login()
        self.get_personl_info()
        self.logout()


spider = Spider()
spider.run()



