import datetime

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyocr import  tesseract
import pytesseract
from PIL import Image
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
iplist=[]
def dyname_proxy():
    url="https://www.kuaidaili.com/free/inha"
    response = requests.get(url)
    if(response.status_code==200):
        html = response.text
        soup = BeautifulSoup(html,'lxml')
        tbody = soup.find('tbody')
        tr = tbody.find_all('tr')
        for tds in tr:
            if tds:
                ipport = {}
                ipport['IP']=tds.find('td',attrs={'data-title':'IP'}).text
                ipport['PORT']= tds.find('td', attrs={'data-title': 'PORT'}).text
                iplist.append(ipport)
dyname_proxy()
def buy(go_time, logintimes):
    '''

    :param times:抢购时间
    :param logintimes: 登陆时间
    :return:
    '''
    is_buyed = False
    # 点击购物车里全选按钮

    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print('现在时间：', now)
        # 对比时间，时间到的话就点击结算
        if now > times:
            if choose == 1:
                while True:
                    try:
                        if browser.find_element_by_id("J_SelectAllcbx1"):
                            browser.find_element_by_id("J_SelectAllcbx1").click()
                            print('尝试全选')
                            break
                    except:
                        print("找不到全选按钮")
            # 点击结算按钮
            try:
                if browser.find_element_by_id("J_Go"):
                    browser.find_element_by_id("J_Go").click()
                    print("结算成功")
            except:
                pass
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单') and is_buyed == False:
                        browser.find_element_by_link_text('提交订单').click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("抢购成功时间：%s" % now1)
                except:
                    print("再次尝试提交订单")
            time.sleep(0.005)
def login_taobao(logintime):
    b = False
    # browser.execute_script(url)
    # # 输出当前窗口句柄（百度）
    # handle_taobao = browser.current_window_handle
    # handles = browser.window_handles
    # print(handles)  # 输出句柄集合
    # handle_taobao2 = None   2019-11-23 18:30:00.000000
    # for handle in handles:
    #     if handle != handle_taobao:
    #         'handle_taobao'_b = handle


    go_time = datetime.datetime.strptime(logintime,'%Y-%m-%d %H:%M:%S.%f')+datetime.timedelta(seconds=10)
    mt_time = go_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # print('现在时间：', now)
        if now > logintime and b == False:
            browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)
            browser.get(url)
            wait = WebDriverWait(browser, 10)
            browser.find_element_by_link_text("亲，请登录").click()
            user_account = wait.until(EC.presence_of_element_located((By.ID, 'J_Quick2Static')))
            user_account.click()
            blog_login = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "weibo-login")))
            blog_login.click()
            # browser.find_elements_by_class_name('weibo-login').click()
            # sina operation
            username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            username.send_keys(cf.get("sina.com", "username"))
            password = wait.until(EC.presence_of_element_located((By.NAME,"password")))
            password.send_keys(cf.get("sina.com", "password"))
            bool_login = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "W_btn_g")))
            bool_login.click()
            #淘宝网页操作
            cart = wait.until(EC.presence_of_element_located((By.ID, 'mc-menu-hd')))
            cart.click()
            elements = browser.find_elements_by_class_name('J_CheckBoxItem')
            for element in elements:
                browser.find_element_by_css_selector('input#'+'J_CheckBox_'+element.get_property("value")+'+label').click()
            b = True
        if now > mt_time:
            js = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='btn-area']/a[@class='submit-btn']")))
            js.click()
            commit = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "go-btn")))
            commit.click()
            print('抢购成功时间：', now)
            time.sleep(10)
            browser.close()
            break

if __name__  ==  '__main__':
    # 2019-11-27 21:59:50.001000
    cf = configparser.ConfigParser()
    cf.read("config.ini")
    url = 'https://www.taobao.com'
    # # chrome_option.add_argument('--proxy-server=183.166.96.99:9999')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
    # # options.add_experimental_option('excludeSwitches',["ignore-certificate-errors"])
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"')


    # browser.find_element_by_link_text("亲，请登录").click()
    #
    # user_account = wait.until(EC.presence_of_element_located((By.ID,'J_Quick2Static')))
    # user_account.click()
    # browser.find_element_by_id('J_Quick2Static').click()
    # time.sleep(1)
    '''
    淘宝登陆
    '''

    # tpl_username = wait.until(EC.presence_of_element_located((By.ID,"TPL_username_1")))
    # tpl_username.send_keys(cf.get("taobao.com", "username"))
    # tpl_password = wait.until(EC.presence_of_element_located((By.ID,"TPL_password_1")))
    #
    # tpl_password.send_keys(cf.get("taobao.com", "password"))
    # tpl_login = wait.until(EC.presence_of_element_located((By.ID,"J_SubmitStatic")))
    # tpl_login.click()


    '''
    新浪登陆验证
    '''
    # # browser.find_elements_by_class_name('weibo-login').click()
    # blog_login = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"weibo-login")))
    # blog_login.click()
    # username = wait.until(EC.presence_of_element_located((By.NAME,"username")))
    # username.send_keys(cf.get("sina.com", "username"))
    # password = wait.until(EC.presence_of_element_located((By.NAME,"password")))
    # password.send_keys(cf.get("sina.com", "password"))
    # cookie1 = browser.get_cookies()
    #
    # print('cookie===',cookie1)
    # bool_login = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"W_btn_g")))
    # bool_login.click()
    # # browser.find_element_by_class_name('W_btn_g').click()
    # cart = wait.until(EC.presence_of_element_located((By.ID,'mc-menu-hd')))
    # cart.click()
    # elements=browser.find_elements_by_class_name('J_CheckBoxItem')
    # for element in elements:
    #     print('J_CheckBox_'+element.get_property("value"))
    #     browser.find_element_by_css_selector('input#'+'J_CheckBox_'+element.get_property("value")+'+label').click()
        # change = wait.until(EC.presence_of_element_located((By.XPATH,'J_CheckBox_'+element.get_property("value"))))
        # change.fin
    # js = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='btn-area']/a[@class='submit-btn']")))
    # js.click()
    # commit = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"go-btn")))
    # commit.click()
    # browser.find_element_by_xpath('//div[@class="btn-area"]/a[@class="submit-btn"]').click()
    # browser.close()
    # times = input("请输入抢购时间，格式如(2018-09-06 11:20:00.000000):")
    logintime = input("请输入登陆(login)时间，格式如(2018-09-06 11:20:00.000000):")

    login_taobao(logintime)
    # buy(times, logintime)
































