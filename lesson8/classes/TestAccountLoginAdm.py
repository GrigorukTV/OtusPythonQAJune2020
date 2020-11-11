from classes.Browser import Browser
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''
http://localhost/admin/
'''

class TestAccountLoginAdm:

    """
    Проверка, что при отправке пустой формы, появляется предупреждающее собщение
    """

    def test_login_null(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        login = wd.find_element_by_css_selector('button[type="submit"]')
        login.click()
        index = -1
        message = WebDriverWait(wd, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find('alert-danger')
        self.close()
        assert index > -1

    """
    Проверка, что при вводе в форме только логина, появляется предупреждающее собщение
    """

    def test_user_login(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        login = wd.find_element_by_css_selector('#input-username')
        login.send_keys('user')
        button = wd.find_element_by_css_selector('button[type="submit"]')
        button.click()
        index = -1
        message = WebDriverWait(wd, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find('alert-danger')
        self.close()
        assert index > -1

    """
    Проверка, что при вводе в форме только пароля, появляется предупреждающее собщение
    """

    def test_user_pass(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        passw = wd.find_element_by_css_selector('#input-password')
        passw.send_keys('bitnami')
        button = wd.find_element_by_css_selector('button[type="submit"]')
        button.click()
        index = -1
        message = WebDriverWait(wd, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find('alert-danger')
        self.close()
        assert index > -1

    """
    Проверка, что при ошибке в логине, нажав на крестик сообщения, оно закрывается
    """

    def test_message_close(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        login = wd.find_element_by_css_selector('#input-username')
        login.send_keys('user')
        button = wd.find_element_by_css_selector('button[type="submit"]')
        button.click()
        message = WebDriverWait(wd, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert > .close")))
        message.click()
        message1 = wd.find_elements_by_css_selector('.alert')
        self.close()
        assert len(message1) == 0

    """
    Проверка, что пользователь авторизован
    """

    def test_authorization(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        login = wd.find_element_by_css_selector('#input-username')
        login.send_keys('user')
        passw = wd.find_element_by_css_selector('#input-password')
        passw.send_keys('bitnami')
        button = wd.find_element_by_css_selector('button[type="submit"]')
        button.click()
        elements = WebDriverWait(wd, 0.5).until(
            EC.url_changes("http://localhost/admin/")
        )
        self.close()
        assert elements is True

    '''
    Закрытие страницы
    '''

    def close(self):
        self.browser_page.closeBrowser()
