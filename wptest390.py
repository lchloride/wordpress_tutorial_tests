import time, os, errno, argparse, sys, random, string
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from wptest import WPTest
from styleparser import StyleParser


class WPTest390(WPTest):
    def __init__(self):
        # UPDATE HERE (1/5)
        self.main_page = 'http://localhost/wordpress3_9/'
        super().__init__(self.main_page)
        self.driver.get(self.main_page)
        self.driver.delete_all_cookies()
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

    def init_new_post(self):
        print('[*] Starting new post test...')
        self.driver.get(self.url_with_base('wp-admin/post-new.php'))
        # Must logged in to post new article
        assert self.driver.get_cookie('wp_login') != 'success', '[-] Cannot initialize new post page: login failed'
        self.click_element('//*[@id="show-settings-link"]')
        time.sleep(2)
        print(self.driver.find_element_by_xpath('//*[@id="postexcerpt"]').is_displayed())
        if self.driver.find_element_by_xpath('//*[@id="postexcerpt-hide"]').get_attribute('checked') is None:
            self.click_element('//*[@id="postexcerpt-hide"]')
        if self.driver.find_element_by_xpath('//*[@id="trackbacksdiv-hide"]').get_attribute('checked') is None:
            self.click_element('//*[@id="trackbacksdiv-hide"]')
        if self.driver.find_element_by_xpath('//*[@id="postcustom-hide"]').get_attribute('checked') is None:
            self.click_element('//*[@id="postcustom-hide"]')
        if self.driver.find_element_by_xpath('//*[@id="commentstatusdiv-hide"]').get_attribute('checked') is None:
            self.click_element('//*[@id="commentstatusdiv-hide"]')
        if self.driver.find_element_by_xpath('//*[@id="slugdiv-hide"]').get_attribute('checked') is None:
            self.click_element('//*[@id="slugdiv-hide"]')
        if self.driver.find_element_by_xpath('//*[@id="authordiv-hide"]').get_attribute('checked') is None:
            self.click_element('//*[@id="authordiv-hide"]')
        if self.driver.find_element_by_xpath('//*[@id="show-settings-link"]').get_attribute('checked') is None:
            self.click_element('//*[@id="show-settings-link"]')
        if self.success:
            self.driver.add_cookie({'name': 'wp_new_post_init', 'value': 'success'})
            print('[+] Test initialization successful')

    def add_title_text(self, text):
        print('[+] Adding title...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.fill_textbox('//*[@id="title"]', text)

    def add_body_text(self, text):
        print('[+] Adding body...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.click_element('//*[@id="content-html"]')
        self.fill_textbox('//*[@id="content"]', text)

    def preview_post(self):
        print('[+] Preview post...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.click_element('//*[@id="post-preview"]')

    def save_post(self):
        print('[+] Saving post...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.driver.execute_script("window.scrollTo(0, 0)");
        self.click_element('//*[@id="save-post"]')

    def publish_post(self):
        print('[+] Publishing post...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.click_element('//*[@id="publish"]')
        if self.wait_for_text_in_page('Post published.') is None:
            print('[-] Publishing failed')

    def select_category(self, idx):
        print('[+] Select category...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        categories = self.driver.find_elements_by_xpath('//*[@id="categorychecklist"]/li')
        if 1 <= idx <= len(categories):
            self.click_element('//*[@id="in-category-' + str(idx) + '"]')
        else:
            print('[!] Invalid category index, using 1 instead')
            self.click_element('//*[@id="in-category-1"]')

    def add_excerpt(self, text):
        print('[+] Adding excerpt...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        styles = StyleParser(self.driver.find_element_by_xpath('//*[@id="postexcerpt"]').get_attribute('style'))
        # print(styles)
        if styles.get_style_value('display') != 'none' or styles.get_style_value('display') is None:
            self.fill_textbox('//*[@id="excerpt"]', text)
        else:
            print('[-] Cannot find excerpt textarea')

    # status_text should be Draft(default) or Pending Review
    def change_status(self, status_text='Draft'):
        print('[+] Changing status')
        # self.driver.execute_script("window.scrollTo(0, 0)");
        self.click_element('//*[@id="misc-publishing-actions"]/div[1]/a')
        styles = StyleParser(self.driver.find_element_by_xpath('//*[@id="post-status-select"]')
                            .get_attribute('style'))
        if styles.get_style_value('display') == 'none':
            self.success = False
            print('[-] Status panel not displayed')
            return
        self.select_dropdown('//*[@id="post_status"]', status_text)
        self.click_element('//*[@id="post-status-select"]/a[1]')
        if self.wait_for_text_in_page(status_text) is None:
            self.success = False
            print('[-] Changing status failed')

    # # TODO:
    def change_visibility(self, visibility):
        print('[+] Changing visibility')


    def new_post_tests(self):
        self.init_new_post() if self.success else None
        # self.select_category(2) if self.success else None
        # self.add_title_text('Test') if self.success else None
        # self.add_body_text('<h2>This is a test article.</h2>\n<p>This is a paragraph. 12345</p>') if self.success else None
        # self.add_excerpt('This is a test') if self.success else None
        # self.change_status('Pending Review')
        # self.save_post() if self.success else None
        # self.preview_post() if self.success else None
        # self.publish_post() if self.success else None


if __name__ == '__main__':
    # Test chrome driver
    test = WPTest390()
    test.login('admin', 'Admin123456')

    test.new_post_tests()

    # test.close_all(delay=3)
