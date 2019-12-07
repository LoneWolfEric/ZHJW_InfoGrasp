from selenium import webdriver
from PIL import Image
from bs4 import BeautifulSoup
import time
import re

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
        self.student_info = StudentInfo()
        self.message = ''


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

    # 输入学号密码验证码，登陆
    def login(self, student_id, password, captch):
        username_box = self.driver.find_element_by_id('input_username')
        password_box = self.driver.find_element_by_id('input_password')
        captch_box = self.driver.find_element_by_id('input_checkcode')

        username_box.send_keys(student_id)
        password_box.send_keys(password)
        # captch = str(input('captch?'))
        captch_box.send_keys(captch)
        self.driver.save_screenshot('filltheform.png')

        submit_bottom = self.driver.find_element_by_id('loginButton')
        submit_bottom.click()
        time.sleep(1)

        if self.driver.current_url == 'http://zhjw.scu.edu.cn/index.jsp':
            self.message = '成功登陆'
        elif self.driver.current_url == 'http://zhjw.scu.edu.cn/login?errorCode=badCaptcha':
            self.message = '验证码错误！'
        else:
            self.message = '用户名或密码错误！'
        

        self.driver.save_screenshot('login.png')

    # 进入登陆页面，获取个人信息
    def personl_info_process(self):
        self.driver.get('http://zhjw.scu.edu.cn/student/rollManagement/rollInfo/index')
        html = self.driver.page_source
        soup = BeautifulSoup(html,features='html.parser')
        info = soup.find_all('div', class_='profile-info-value')
        usrful_info = info[2:74]
        for i in range(len(usrful_info)):
            res = re.findall(r'>(.*?)<',str(usrful_info[i]),re.DOTALL)
            res = str(res[0]).strip()
            usrful_info[i] = res

        self.student_info.name = usrful_info[16]
        self.student_info.student_id = usrful_info[15]
        self.student_info.major = usrful_info[23]
        self.student_info.college = usrful_info[22]
        self.student_info.degree = usrful_info[31]
        self.student_info.grade = usrful_info[21]
        self.student_info.gender = usrful_info[49]
        self.student_info.native_place = usrful_info[55]
        self.student_info.email = usrful_info[0]
        self.student_info.phone = usrful_info[5]

    # 断开连接
    def logout(self):
        self.driver.delete_all_cookies()
        self.driver.quit()

    def get_personal_info(self, student_id, password, captch):
        self.login(student_id, password, captch)
        if self.message == '成功登陆':
            self.personl_info_process()
            self.logout()

        


spider = Spider()
spider.get_CAPTCHA()
captch = str(input('captch?'))
spider.get_personal_info('2016141442100', 'lyx-19980708', captch)

print(spider.message)
print(spider.student_info.student_id)
print(spider.student_info.name)
print(spider.student_info.major)
print(spider.student_info.college)
print(spider.student_info.degree)
print(spider.student_info.grade)
print(spider.student_info.gender)
print(spider.student_info.native_place)
print(spider.student_info.email)
print(spider.student_info.phone)