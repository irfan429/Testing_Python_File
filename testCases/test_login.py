import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_001_Login():
    baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()

        if act_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_Username(self.username)
        self.lp.set_Password(self.password)
        self.lp.click_Login()
        title = self.driver.title
        print(title)
        self.driver.close()
        if title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False

