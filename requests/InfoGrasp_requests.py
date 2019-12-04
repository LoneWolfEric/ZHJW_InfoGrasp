import requests
from bs4 import BeautifulSoup
import hashlib
import time

class Spider(object):

    def __init__(self):
        self.s = requests.session()

    # 访问登陆页面，获取下载验证码
    def get_CAPTCHA(self):

        header = {
            'Cookie': 'JSESSIONID=dbcoVU7uOTD0ccCPIKj7w',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
        }
        url = 'http://zhjw.scu.edu.cn/login'
        response = self.s.get(url,headers=header)

        url = 'http://zhjw.scu.edu.cn/assets/js/jquery/jquery-2.1.1.min.js'
        response = self.s.get(url,headers=header)

        url = 'http://zhjw.scu.edu.cn/assets/layer/layer.js'
        response = self.s.get(url,headers=header)

        url = 'http://zhjw.scu.edu.cn/js/md5/md5.js'
        response = self.s.get(url,headers=header)

        url = 'http://zhjw.scu.edu.cn/js/jQuery/jquery.js'
        response = self.s.get(url,headers=header)
        
        url = 'http://zhjw.scu.edu.cn/css/login/login.css'
        response = self.s.get(url,headers=header)

        url = 'http://zhjw.scu.edu.cn/img/captcha.jpg'
        response = self.s.get(url,headers=header)
        with open('captcha.jpg', 'wb') as f:
            f.write(response.content)
        # response = self.s.get(url,headers=header)
        # with open('captcha2.jpg', 'wb') as f:
        #     f.write(response.content)

        url = 'http://zhjw.scu.edu.cn/assets/layer/skin/layer.css'
        response = self.s.get(url,headers=header)

        url = 'http://zhjw.scu.edu.cn/img/icon/favicon.ico'
        response = self.s.get(url,headers=header)


    # 输入学号密码验证码，登陆
    def login(self):
        url = 'http://zhjw.scu.edu.cn/j_spring_security_check'
        header = { 
            'Connection': 'keep-alive',
            'Content-Length': '83',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'JSESSIONID=dbcoVU7uOTD0ccCPIKj7w',
            'Host': 'zhjw.scu.edu.cn',
            'Origin': 'http://zhjw.scu.edu.cn',
            'Referer':'http://zhjw.scu.edu.cn/login',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
        }
        captcha = str(input('CAPTCHA?'))
        password = 'lyx-19980708'
        print(hashlib.md5(password.encode('utf-8')).hexdigest())
        data = {
            'j_username': '2016141442100',
            'j_password': hashlib.md5(password.encode('utf-8')).hexdigest(),
            'j_captcha': captcha,
        }
        self.s.post(url,headers=header,data=data)


        # url = 'http://zhjw.scu.edu.cn/login?errorCode=badCaptcha'
        # header = {
        #     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
        # }
        # response = self.s.get(url,headers=header)
        # print(response.url)
        # print(response.content.decode('utf-8'))

    # 进入登陆页面，获取个人信息
    def get_personl_info(self):
        header = { 
            'Connection': 'keep-alive',
            # 'Cookie': 'JSESSIONID=dbcoVU7uOTD0ccCPIKj7w',
            'Host': 'zhjw.scu.edu.cn',
            'Origin': 'http://zhjw.scu.edu.cn',
            'Referer':'http://zhjw.scu.edu.cn/login',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
        }
        response = self.s.get('http://zhjw.scu.edu.cn/',headers=header)
        print(response.headers)
        print(response.status_code)
        print(response.history)
        print(response.links)
        print(response.content.decode('utf-8'))
        



    # 断开连接
    def logout(self):
        pass

    def run(self):
        self.get_CAPTCHA()
        time.sleep(2)
        self.login()
        time.sleep(2)
        self.get_personl_info()
        self.logout()


spider = Spider()
spider.run()
