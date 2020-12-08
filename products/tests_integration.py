from purbeurreconfig.settings import BASE_DIR
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import logout, login
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import RequestFactory

from django.urls import reverse
from django.shortcuts import render, redirect

from .models import Products
from accounts.models import CustomUser


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:90014")

class TestIntegrations(StaticLiveServerTestCase):
    """Functional tests using the Chrome web browser in headless mode."""
    

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(
            executable_path=str(BASE_DIR / 'webdrivers' / 'chromedriver'),
            options=chrome_options,
            )
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()        

    def test_results_page_shows(self):

        self.driver.get(self.live_server_url)
        self.driver.find_element_by_id("searchForm").send_keys('maison')
        self.driver.find_element_by_id("searchForm").submit()

        page_url = self.driver.current_url

        server = self.live_server_url
        url_test = reverse('search_product')
        url = ''.join((server,url_test))
        args = "query=maison"
        final_url = '?'.join((url,args))

        self.assertEqual(page_url, final_url)

    def test_create_account(self):

        url = reverse("create_account")
        self.driver.get(self.live_server_url + url)
        self.driver.find_element_by_name('email').send_keys(
            "email@email.com"
        )
        self.driver.find_element_by_name('first_name').send_keys(
            "first_name"
        )
        self.driver.find_element_by_name('second_name').send_keys(
            "second_name"
        )
        self.driver.find_element_by_name('password1').send_keys(
            "12345678"
        )
        self.driver.find_element_by_name('password2').send_keys(
            "12345678"
        )
        self.driver.find_element_by_tag_name('input').submit()

        url = reverse("logout")
        self.driver.get(self.live_server_url + url)

        page_url = self.driver.current_url
        url2 = reverse('home')
        
        self.assertEqual(page_url, self.live_server_url + url2)


    def test_user_can_connect_and_disconnect(self):
        url = reverse("login")
        self.driver.get(self.live_server_url + url)

        self.driver.find_element_by_id('id_username').send_keys(
            "email@email.com"
        )
        self.driver.find_element_by_id('id_password').send_keys(
            "12345678"
        )
        self.driver.find_element_by_id("login-form").submit()

        url = reverse("logout")
        self.driver.get(self.live_server_url + url)

        page_url = self.driver.current_url
        url2 = reverse('home')
        
        self.assertEqual(page_url, self.live_server_url + url2)


