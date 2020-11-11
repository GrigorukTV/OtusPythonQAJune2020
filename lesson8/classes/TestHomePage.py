import time
from classes.Browser import Browser
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''
http://localhost/
'''
class TestHomePage:

    '''
    Проверка того, что мы на главной по title страницы
    '''

    def test_title(self, browser, url):
        self.browser_page = Browser(browser, url)
        title = self.browser_page.get_wd().title
        self.close()
        assert title == 'Your Store'

    '''
    Проверка номера телефона
    '''
    def test_phone(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        topLinks = wd.find_element_by_id('top-links')
        print(topLinks)
        listInline = topLinks.find_elements_by_class_name('list-inline')
        print(listInline)
        li = listInline[0].find_elements_by_tag_name('li')
        print(li)
        span = li[0].find_element_by_tag_name('span')
        phone = span.get_attribute('innerHTML')
        self.close()
        assert phone == '123456789'

    '''
    Проверка на то, что в Рекомендуемых товарах 4 карточки
    '''
    def test_cards(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        product_layouts = self.browser_page.get_wd().find_elements_by_css_selector('.product-layout')
        self.close()
        assert len(product_layouts) == 4

    '''
    Проверка, что ссылка Yor Store переходит на домашнюю страницу
    '''

    def test_href(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        logo = self.browser_page.get_wd().find_element_by_css_selector('#logo a')
        logo.click()
        url = wd.current_url
        self.close()
        assert url.find('?route=common/home') > -1

    '''
    Проверка, что ссылка Поиска переходит на страницу поиска
    '''

    def test_search(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        search = self.browser_page.get_wd().find_element_by_css_selector('#search > .form-control')
        search.send_keys('iphone')
        button = self.browser_page.get_wd().find_element_by_css_selector('#search > .input-group-btn')
        button.click()
        elements = WebDriverWait(wd, 0.5).until(EC.url_to_be("http://localhost/index.php?route=product/search&search=iphone"))
        self.close()
        assert elements is True


    '''
    Проверка, что вторая карточка iphone переходит на страницу товара
    '''

    def test_iphone(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        iphone = wd.find_elements_by_css_selector('.product-layout h4 > a')
        iphone[1].click()
        elements = WebDriverWait(wd, 0.5).until(EC.url_to_be("http://localhost/iphone"))
        self.close()
        assert elements is True

    '''
    Закрытие страницы
    '''

    def close(self):
        self.browser_page.closeBrowser()
