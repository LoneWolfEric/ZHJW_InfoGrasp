import requests
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO



class Spider(object):

    def __init__(self):
        self.s = requests.session()

    # 访问登陆页面，获取下载验证码
    def get_CAPTCHA(self):
        url = 'http://zhjw.scu.edu.cn/img/captcha.jpg'
        response = self.s.get(url)
        with open('captcha.jpg', 'wb') as f:
            f.write(response.content)

    # 输入学号密码验证码，登陆
    def login(self):
        url = 'http://zhjw.scu.edu.cn/j_spring_security_check'
        


        
    # 进入登陆页面，获取个人信息
    def get_personl_info(self):
        pass
    # 断开连接
    def logout(self):
        pass

    def run(self):
        self.get_CAPTCHA()
        self.login()
        self.get_personl_info()
        self.logout()


spider = Spider()
spider.run()
