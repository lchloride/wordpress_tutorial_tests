import time, os, errno, argparse, sys, random, string
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from . import wptest


class WPTest390(wptest.WPTest):
    def __init__(self):
        # UPDATE HERE (1/5)
        self.main_page = 'http://localhost/wordpress3_9/'
        super().__init__(self.main_page)
        self.add_cookies()

    # Override parent's method
    def add_cookies(self):
        self.driver.get(self.main_page)
        # UPDATE HERE (2/5)
        self.driver.add_cookie({'name': 'test_group', 'value': 'wp390_tutorials'})
        # UPDATE HERE (3/5)
        self.driver.add_cookie({'name': 'test_name', 'value': 'wp_login_wp390_tutorials'})
        # UPDATE HERE (4/5)
        self.driver.add_cookie({'name': 'software_id', 'value': '1'})
        # UPDATE HERE (5/5)
        self.driver.add_cookie({'name': 'software_version_id', 'value': '4'})


if __name__ == '__main__':
    # Test chrome driver
    test = WPTest390()
    test.login('admin', 'Admin123456')
    test.close(delay=2)
