import time, os, errno, argparse, sys, random, string
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class WPTest:
    def __init__(self, main_page):
        self.main_page = main_page
        print("[+] Setting up ChromeDriver")
        options = webdriver.chrome.options.Options()
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        self.success = True

    # A virtual method provided by parent, children should override it
    def add_cookies(self):
        pass

    def set_test_name(self, test_name):
        self.driver.delete_cookie('test_name')
        self.driver.add_cookie({'name': 'test_name', 'value': test_name})

    def click_element(self, xpath_selector):
        try:
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            element.click()
        except Exception as e:
            self.success = False
            print('[-] Failed to click on element')
            print(e)

    def fill_textbox(self, xpath_selector, text):
        try:
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            self.success = False
            print('[-] Failed to fill textbox')
            print(e)

    def select_dropdown(self, xpath_selector, text):
        try:
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            Select(element).select_by_visible_text(text)
        except Exception as e:
            self.success = False
            print('[-] Failed to select optin')
            print(e)

    def check_exists_and_visible_by_xpath(self, xpath_selector):
        try:
            return self.driver.find_element_by_xpath(xpath_selector).is_displayed()
        except NoSuchElementException:
            return False
        return True

    def wait_for_element_become_visible(self, xpath_selector):
        timeout = 20
        while not self.check_exists_and_visible_by_xpath(xpath_selector):
            print("[+] Waiting for %s to become visible" % xpath_selector)
            # Wait for login pop up to load via ajax
            time.sleep(1)
            timeout = timeout - 1
            if timeout == 0:
                self.success = False
                print("[-] Timed out %s" % xpath_selector)
                return None

    def wait_for_text_in_page(self, text):
        timeout = 20
        while not text in self.driver.page_source:
            print("[+] Waiting for text: %s to load in page" % text)
            time.sleep(1)
            timeout = timeout - 1
            if timeout == 0:
                self.success = False
                print("[-] Timed out %s" % text)
                return None
        return True

    # This method would provide common login method and write related cookies
    # If detailed login test needed, override it in subclass
    def login(self, username=None, password=None, is_remember=False):
        self.set_test_name('pma_login')
        print("[*] Starting login process...")
        self.driver.get(self.url_with_base('wp-login.php'))
        # Fill form fields
        try:
            # if self.logged_in:
            #     print('[+] Already logged in, skipping.')
            #     return
            # Enter Username
            self.fill_textbox('//*[@id="user_login"]', 'wpuser' if username is None else username)
            # Enter password
            self.fill_textbox('//*[@id="user_pass"]', 'password' if password is None else password)
            # Click remember me
            if is_remember:
                self.click_element('//*[@id="rememberme"]')
            # Click submit
            self.click_element('//*[@id="wp-submit"]')
            time.sleep(3)
            if "login_error" in self.driver.page_source:
                self.success = False
                print('[-] Login failed')
            elif self.wait_for_text_in_page('Log Out') is None:
                self.success = False
                print('[-] Login failed')
            else:
                # self.logged_in = True
                print('[+] Login successful')
        except (NoSuchElementException, ElementNotVisibleException) as ex:
            self.success = False
            print("[-] Elements not found on page")
            print(str(ex))
        except Exception as ex:
            self.success = False
            print("[-] Unhandled error")
            print(str(ex))

    # Concat URL main_page and additional path with '/'
    def url_with_base(self, path):
        if self.main_page.endswith('/'):
            self.main_page = self.main_page[:-1]
        if path.startswith('/'):
            path = path[1:]
        return self.main_page + '/' + path

    def close(self, close_on_suc=False, delay=0):
        if close_on_suc and not self.success:
            pass
        else:
            print('[+] Driver will be closed after', delay, 'seconds')
            time.sleep(delay)
            print('[+] Driver closed')
            self.driver.close()
