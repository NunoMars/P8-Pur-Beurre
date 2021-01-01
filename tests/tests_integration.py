from purbeurreconfig.settings import BASE_DIR, FIXTURE_DIRS
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from django.urls import reverse

from products.models import Products, Categorys
from accounts.models import CustomUser


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('-headless')
chrome_options.add_argument('window-size=1920x1080')


class TestIntegrations(StaticLiveServerTestCase):
    """Functional tests using the Chrome web browser in headless mode."""
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(
            options=chrome_options,
            )
        cls.driver.maximize_window()    

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()        

    def test_results_page_shows(self):
        '''
        Tests the search page, and the products page.
        '''
        i = 1
        while i <= 20:
            
            c = Categorys(
                category="category",
            )
            c.save()
            if 1 <= 10:
                p = Products(
                    product="123456"+str(i),
                    nutrition_grade_fr= 1,
                    product_name_fr="Product"+str(i),
                    ingredients_text_fr="Ingredients"+str(i),
                    product_image_large="Product_img_l"+str(i),
                    product_image_small="Product_img_s"+str(i),
                    product_image_nutrition_large="Product_img_n_l"+str(i),
                    product_image_nutrition_small="Product_img_n_s"+str(i),
                    stores="Stores"+str(i),
                    url="Url"+str(i),
                    )
                
                cat = Categorys.objects.get(category="category")
                p.category = cat
                p.save()
            else:
                p = Products(
                    product="123456"+str(i),
                    nutrition_grade_fr= 2,
                    product_name_fr="Product"+str(i),
                    ingredients_text_fr="Ingredients"+str(i),
                    product_image_large="Product_img_l"+str(i),
                    product_image_small="Product_img_s"+str(i),
                    product_image_nutrition_large="Product_img_n_l"+str(i),
                    product_image_nutrition_small="Product_img_n_s"+str(i),
                    stores="Stores"+str(i),
                    url="Url"+str(i),
                    )
                
                cat = Categorys.objects.get(category="category")
                p.category = cat
                p.save()
            i += 1

        self.driver.get(self.live_server_url)
        self.driver.find_element_by_id("searchForm").send_keys('Product')
        self.driver.find_element_by_id("searchForm").submit()

        

        self.assertTrue(self.driver.title == 'Page Products')


    def test_create_account(self):
        '''
        Tests the account creation page an verify that the account icon change.
        '''

        url = reverse("create_account")
        self.driver.get(self.live_server_url + url)

        username_input = self.driver.find_element_by_name("email")
        username_input.send_keys('remi@purbeurre.com')

        first_name_input = self.driver.find_element_by_name("first_name")
        first_name_input.send_keys('remi')

        second_name_input = self.driver.find_element_by_name("second_name")
        second_name_input.send_keys('petitchef')

        password1_input = self.driver.find_element_by_name("password1")
        password1_input.send_keys('a.345679')

        password2_input = self.driver.find_element_by_name("password2")
        password2_input.send_keys('a.345679')

        self.driver.find_element_by_xpath('//input[@value="Submit"]').click()


        element = self.driver.find_element_by_id("auth_icon")
        self.assertTrue(element.is_displayed())


    def test_user_can_connect_and_disconnect(self):
        '''
        Tests the login and logout pages.
        '''
       
        user = CustomUser.objects.create_user(
            email="souris@purbeurre.com",
            first_name="souris",
            second_name="petite",
            password="a.1234S1"
            )

        url = reverse("login")
        self.driver.get(self.live_server_url + url)


        username = self.driver.find_element_by_id('id_username')
        username.send_keys("souris@purbeurre.com")

        password = self.driver.find_element_by_id('id_password')
        password.send_keys("a.1234S1")

        self.driver.find_element_by_xpath('//input[@value="Login"]').click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "auth_icon"))
        )
        
        self.assertTrue(element.is_displayed())

        url = reverse("logout")
        self.driver.get(self.live_server_url + url)
        
        element = self.driver.find_element_by_id("account_icon")
        self.assertTrue(element.is_displayed())




        