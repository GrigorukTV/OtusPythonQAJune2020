from classes.Browser import Browser
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''
http://localhost/index.php?route=product/category&path=20
'''

class TestCatalog:

    '''
    Проверка, что при отображении карточек на странице списком или в гриде, колличество элементов на странице равно
    '''
    def test_count_elements(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        list_view = wd.find_element_by_id('list-view')
        list_view.click()
        count_elements = wd.find_elements_by_class_name('product-layout')
        print(len(count_elements))
        grid_view = wd.find_element_by_id('grid-view')
        grid_view.click()
        count_elements1 = wd.find_elements_by_class_name('product-layout')
        print(len(count_elements1))
        self.close()
        assert count_elements == count_elements1

    '''
    Проверка, что при отображении карточек на странице списком или в гриде, колличество элементов на странице равно
    '''

    def test_sorted(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        input_sort = Select(wd.find_element_by_id('input-sort'))
        input_sort.select_by_index(2)
        card = wd.find_elements_by_css_selector('.caption h4 > a')
        first_letter = card[0].get_attribute('innerHTML')
        self.close()
        assert first_letter[0] == 'S'

    '''
    Проверка, что при нажатии на баннер открывается другая страница
    '''

    def test_banner(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        banner = wd.find_element_by_id('banner0')
        banner.click()
        url = wd.current_url
        self.close()
        assert url != 'http://localhost/index.php?route=product/category&path=20'

    '''
    Проверка, что при нажатии в боковом меню Tablets открывается страница Tablets и на ней есть товар
    '''

    def test_menu(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        list_group = wd.find_elements_by_css_selector('.list-group-item')
        list_group[5].click()
        card = wd.find_elements_by_css_selector('.caption  h4 > a')
        card1 = card[0].get_attribute('innerHTML')
        self.close()
        assert card1 == 'Samsung Galaxy Tab 10.1'

    '''
    Проверка, что при выборе товара в избранное, в сплывающем сообщении присутствует название товара
    '''

    def test_message(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        like = wd.find_elements_by_css_selector('.button-group button')
        like[1].click()
        message = WebDriverWait(wd, 2).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, ".alert a")))
        name_card = message[2].get_attribute('innerHTML')
        self.close()
        assert name_card == 'Apple Cinema 30"'



    '''
    Закрытие страницы
    '''

    def close(self):
        self.browser_page.closeBrowser()