from purbeurreconfig.settings import BASE_DIR
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')


class TestProductSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(
            executable_path=str(BASE_DIR / 'webdrivers' / 'chromedriver'),
            options=chrome_options,
            )
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()        

    def test_results_page_shows(self):
        browser = self.driver.get("https://nunopurbeurre.herokuapp.com/")
        product_form = browser.find_element(By.ID("searchForm"))
        product_form.send_keys('maison')
        product_form.click()


        page_url = browser.current_url

        self.assertEqual(page_url, 'https://nunopurbeurre.herokuapp.com/products/3265261606676/')
        self.assertEqual(page_title, u'Page Products')


if __name__ == '__main__':
    unittest.main()