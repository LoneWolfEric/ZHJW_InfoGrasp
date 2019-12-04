from selenium import webdriver
from PIL import Image
from bs4 import BeautifulSoup
import hashlib
import time


# 创建一个类用于存储学生信息
class StudentInfo(object):
    name = ''
    student_id = ''
    major = ''
    college = ''
    degree = ''
    grade = ''
    gender = ''
    native_place = ''
    email = ''
    phone = ''

class Spider(object):

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=chrome_options)

    # 访问登陆页面，获取下载验证码
    def get_CAPTCHA(self):
        self.driver.get('http://zhjw.scu.edu.cn/login')
        time.sleep(2)
        self.driver.maximize_window()
        self.driver.save_screenshot('screenshot.png')
        captcha = self.driver.find_element_by_id('captchaImg')
        location = captcha.location
        size = captcha.size
        print(captcha.location)
        print(captcha.size)
        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = top + size['height']

        img=Image.open('screenshot.png')
        img = img.crop((left,top,right,bottom))
        img.save('captch.png')
        # print(self.driver.page_source) 

    # 输入学号密码验证码，登陆
    def login(self):
        username_box = self.driver.find_element_by_id('input_username')
        password_box = self.driver.find_element_by_id('input_password')
        captch_box = self.driver.find_element_by_id('input_checkcode')

        username_box.send_keys('2016141442100')
        password_box.send_keys('lyx-19980708')
        captch = str(input('captch?'))
        captch_box.send_keys(captch)
        self.driver.save_screenshot('filltheform.png')

        submit_bottom = self.driver.find_element_by_id('loginButton')
        submit_bottom.click()
        time.sleep(1)
        self.driver.save_screenshot('login.png')
        pass

    # 进入登陆页面，获取个人信息
    def get_personl_info(self):
        # 进入个人信息界面
        # menu-text = self.driver.find_element_by_id('1181690')
        time.sleep(3)
        self.driver.get('http://zhjw.scu.edu.cn/student/rollManagement/rollInfo/index')
        self.driver.save_screenshot('personalinfo.png')

        with open('prsonalinfo.html', 'wb') as f:
            f.write(self.driver.page_source.encode('utf-8'))

        # print(self.driver.page_source)
        student = StudentInfo()

        student.name = ''
        student.student_id = ''
        student.major = ''
        student.college = ''
        student.degree = ''
        student.grade = ''
        student.gender = ''
        student.native_place = ''
        student.email = ''
        student.phone = ''

    # 断开连接
    def logout(self):
        self.driver.delete_all_cookies()
        self.driver.quit()

    def run(self):
        self.get_CAPTCHA()
        self.login()
        self.get_personl_info()
        self.logout()


spider = Spider()
spider.run()



