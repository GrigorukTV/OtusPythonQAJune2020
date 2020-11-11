from classes.Browser import Browser
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

text = 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

'''
http://localhost/index.php?route=product/product&path=57&product_id=49
'''

class TestCatalogId:

    '''
    На странице есть превьюшки
    '''
    def test_img(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        count_elements = wd.find_elements_by_class_name('image-additional')
        print(len(count_elements))
        # self.close()
        assert len(count_elements) > 0

    '''
    Проверка, что цена товара > 0
    '''

    def test_price(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        element = wd.find_element_by_css_selector('.list-unstyled h2')
        price = element.get_attribute('innerHTML')
        price = float(price.replace('$',''))
        self.close()
        assert price > 0

    '''
    Проверка, что при добавлении товара в корзину, счетчик корзины изменился с 0 на 1
    # '''

    def test_count(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        element_product = wd.find_element_by_css_selector('#button-cart')
        element_product.click()
        WebDriverWait(wd, 2).until(
            EC.text_to_be_present_in_element((By.ID, 'cart-total'), '0 item(s) - $0.00')
        )
        el = wd.find_element_by_css_selector('#cart-total')
        cart = el.get_attribute('innerHTML')
        print(cart)
        index = cart.find('1 item')
        print(index)
        self.close()
        assert index != -1

    '''
    Проверка, что url превью совпадает с url открытой картинкой в галерее
    '''

    def test_gallery(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        element = wd.find_element_by_css_selector('.thumbnails .thumbnail')
        href = element.get_attribute('href')
        element.click()
        element_gallery = WebDriverWait(wd, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, "mfp-img")))
        print(element_gallery)
        href_gallery = element_gallery.get_attribute('src')
        print(href_gallery)
        self.close()
        assert href == href_gallery


    '''
    Проверка, что при отправке отзыва появляется сообщение
    '''

    def test_reviews(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        element = wd.find_element_by_css_selector('a[href="#tab-review"]')
        element.click()
        name = wd.find_element_by_id('input-name')
        name.send_keys('Oleg')
        review = wd.find_element_by_id('input-review')
        review.send_keys(text)
        rating = wd.find_elements_by_css_selector('input[name="rating"]')
        rating[4].click()
        button_review = wd.find_element_by_id('button-review')
        button_review.click()
        index = -1
        message = WebDriverWait(wd, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find('alert-success')
        self.close()
        assert index > -1

    '''
    Закрытие страницы
    '''
    def close(self):
        self.browser_page.closeBrowser()

