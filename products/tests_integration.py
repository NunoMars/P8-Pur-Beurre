import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestProductSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:/OPENCLASSROOMS/Projet8/webdrivers/geckodriver.exe')

    def test_results_page_shows(self):
        browser = self.driver.get("https://nunopurbeurre.herokuapp.com/")
        product_form = browser.find_element(By.ID("searchForm"))
        product_form.send_keys('maison')
        product_form.click()


        page_url = browser.current_url

        self.assertEqual(page_url, 'https://nunopurbeurre.herokuapp.com/products/3265261606676/')
        self.assertEqual(page_title, u'Page Products')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()