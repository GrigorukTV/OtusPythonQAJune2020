from classes.Browser import Browser

'''
http://localhost/admin/
'''

class TestAdmin:

    """
    авторизация
    """

    def login(self, browser, url):
        self.browser_page = Browser(browser, url)
        wd = self.browser_page.get_wd()
        login = wd.find_element_by_css_selector('#input-username')
        login.send_keys('user')
        passw = wd.find_element_by_css_selector('#input-password')
        passw.send_keys('bitnami')
        button = wd.find_element_by_css_selector('button[type="submit"]')
        button.click()
        return wd

    '''
    Проверка, что заголовок = 'Orders'
    '''
    def test_total_orders(self,browser, url):
        wd = self.login(browser, url)
        tile_footer = wd.find_elements_by_css_selector('.tile-footer')
        view_more = tile_footer[0].find_element_by_tag_name('a')
        view_more.click()
        orders = wd.find_element_by_css_selector('h1')
        h1 = orders.get_attribute('innerHTML')
        result = h1.find('Orders')
        self.close()
        assert result != -1

    '''
    Проверка, перехода Systems -> Settings
    '''

    def test_settings(self, browser, url):
        wd = self.login(browser, url)
        menu_system = wd.find_element_by_css_selector('#menu-system a')
        menu_system.click()
        settings = wd.find_element_by_css_selector('#collapse7 > li:first-child a')
        settings.click()
        index = -1
        table = wd.find_element_by_css_selector('.table')
        if table is not None:
            cl_table = table.get_attribute('class')
            index = cl_table.find('table table-bordered table-hover')
        self.close()
        assert index > -1

    '''
    Проверка перехода к разделу с товарами, что появляется таблица с товарами
    '''
    def test_table(self, browser, url):
        wd = self.login(browser, url)
        menu_catalog = wd.find_element_by_css_selector('#menu-catalog a')
        menu_catalog.click()
        product = wd.find_element_by_css_selector('#collapse1 > li:nth-child(2) a')
        product.click()
        index = -1
        table = wd.find_element_by_css_selector('.table')
        if table is not None:
            cl_table = table.get_attribute('class')
            index = cl_table.find('table-bordered table-hover')
        self.close()
        assert index > -1

    '''
    Проверка логина
    '''

    def test_login(self, browser, url):
        wd = self.login(browser, url)
        logout = wd.find_element_by_css_selector('.navbar-right > li:last-child span')
        user_login = logout.get_attribute('innerHTML')
        index = user_login.find('Logout')
        self.close()
        assert index != -1

    '''
    Проверка разлогина
    '''
    def test_logout(self, browser, url):
        wd = self.login(browser, url)
        logout = wd.find_element_by_css_selector('.navbar-right > li:last-child span')
        logout.click()
        url = wd.current_url
        self.close()
        assert url.find('?route=common/login') > -1

    '''
    Закрытие страницы
    '''
    def close(self):
        self.browser_page.closeBrowser()
