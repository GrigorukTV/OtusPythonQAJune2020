import time
from classes.Browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''
http://localhost/index.php?route=account/login
'''

class TestAccountLogin:

    '''
    New Customer при клике на Continue меняется ссылка
    '''

    def test_new_customer(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        continue_bt= wd.find_element_by_css_selector('.well:first-child a')
        continue_bt.click()
        elements = WebDriverWait(wd, 0.5).until(
            EC.url_to_be("http://localhost/index.php?route=account/register")
        )
        self.close()
        assert elements is True


    '''
    При отправке пустой формы в Returning Customer, появляется сообщение об ошибке
    '''

    def test_returning_customer(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        login_bt = wd.find_element_by_css_selector('input[type="submit"]')
        login_bt.click()
        index = -1
        message = WebDriverWait(wd, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find('alert-danger')
        self.close()
        assert index > -1

    '''
    Проверка, что при нажатии Forgotten Password меняется url
    '''

    def test_forgotten_password(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        link = wd.find_element_by_css_selector('.form-group a')
        link.click()
        elements = WebDriverWait(wd, 0.5).until(
            EC.url_to_be("http://localhost/index.php?route=account/forgotten")
        )
        self.close()
        assert elements is True

    '''
    Проверка, что при вводе не существующего email и пароля, появляется сообщение, что пользователь не найден
    '''

    def test_user_not_found(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        email = wd.find_element_by_css_selector('#input-email')
        email.send_keys('12@tests.ru')
        password = wd.find_element_by_css_selector('#input-password')
        password.send_keys('123')
        login_bt = wd.find_element_by_css_selector('input[type="submit"]')
        login_bt.click()
        time.sleep(0.5)
        message = wd.find_element_by_css_selector('.alert')
        user_none = message.get_attribute('innerHTML')
        index = user_none.find('E-Mail Address and/or Password')
        self.close()
        assert index != -1

    '''
    Проверка, что при вводе существующего email и пароля, пользователь авторизован
    '''

    def test_account(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        email = wd.find_element_by_css_selector('#input-email')
        email.send_keys('tests@tests.ru')
        password = wd.find_element_by_css_selector('#input-password')
        password.send_keys('1234')
        login_bt = wd.find_element_by_css_selector('input[type="submit"]')
        login_bt.click()
        account = WebDriverWait(wd, 2).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#content > h2")))
        my_account = account[0].get_attribute('innerHTML')
        index = my_account.find('My Account')
        self.close()
        assert index != -1


    '''
    Закрытие страницы
    '''
    def close(self):
        self.browser_page.closeBrowser()