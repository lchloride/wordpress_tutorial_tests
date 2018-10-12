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

        if not self.checkbox_is_checked('//*[@id="postexcerpt-hide"]'):
            self.click_element('//*[@id="postexcerpt-hide"]')
        if not self.checkbox_is_checked('//*[@id="trackbacksdiv-hide"]'):
            self.click_element('//*[@id="trackbacksdiv-hide"]')
        if not self.checkbox_is_checked('//*[@id="postcustom-hide"]'):
            self.click_element('//*[@id="postcustom-hide"]')
        if not self.checkbox_is_checked('//*[@id="commentstatusdiv-hide"]'):
            self.click_element('//*[@id="commentstatusdiv-hide"]')
        if not self.checkbox_is_checked('//*[@id="slugdiv-hide"]'):
            self.click_element('//*[@id="slugdiv-hide"]')
        if not self.checkbox_is_checked('//*[@id="authordiv-hide"]'):
            self.click_element('//*[@id="authordiv-hide"]')

        self.click_element('//*[@id="show-settings-link"]')
        time.sleep(2)
        if self.success:
            self.driver.add_cookie({'name': 'wp_new_post_init', 'value': 'success'})
            print('[+] Test initialization finished')

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
        self.driver.execute_script("window.scrollTo(0, 0)")
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
        # styles = StyleParser(self.driver.find_element_by_xpath('//*[@id="postexcerpt"]').get_attribute('style'))
        # # print(styles)
        # if styles.get_style_value('display') != 'none' or styles.get_style_value('display') is None:
        if self.driver.find_element_by_xpath('//*[@id="postexcerpt"]').is_displayed():
            self.fill_textbox('//*[@id="excerpt"]', text)
        else:
            print('[-] Cannot find excerpt textarea')

    # status_text should be one of Published, Draft(default) or Pending Review
    def change_status(self, status_text='Published'):
        print('[+] Changing status')
        # self.driver.execute_script("window.scrollTo(0, 0)");

        # If article is private, we cannot change its status
        if self.driver.find_element_by_xpath('//*[@id="post-status-display"]').text == 'Privately Published':
            print('[!] Cannot set status since this article is private')
            return
        self.click_element('//*[@id="misc-publishing-actions"]/div[1]/a')
        # styles = StyleParser(self.driver.find_element_by_xpath('//*[@id="post-status-select"]')
        #                     .get_attribute('style'))
        # if styles.get_style_value('display') == 'none':
        if self.driver.find_element_by_xpath('//*[@id="post-status-select"]').is_displayed():
            self.success = False
            print('[-] Status panel not displayed')
            return
        self.select_dropdown('//*[@id="post_status"]', status_text)
        self.click_element('//*[@id="post-status-select"]/a[1]')
        if self.wait_for_text_in_page(status_text) is None:
            self.success = False
            print('[-] Changing status failed')

    # Change visibility of article
    def change_visibility(self, visibility="public", password=None):
        print('[+] Changing visibility')
        self.click_element('//*[@id="visibility"]/a')
        if visibility == 'public':
            self.click_element('//*[@id="visibility-radio-public"]')
        elif visibility == 'public_sticky':
            self.click_element('//*[@id="visibility-radio-public"]')
            if not self.checkbox_is_checked('//*[@id="sticky"]'):
                self.click_element('//*[@id="sticky"]')
        elif visibility == 'protected':
            self.click_element('//*[@id="visibility-radio-password"]')
            if password is None:
                self.success = False
                print('[-] Password needed')
            elif len(password) > 20:
                print('[-] Password too long')
            else:
                self.fill_textbox('//*[@id="post_password"]', password)
        elif visibility == 'private':
            self.click_element('//*[@id="visibility-radio-private"]')
        else:
            self.success = False
            print('[-] Invalid visibility level. It should be one of public, public_sticky, protected and private.')
            return

        self.click_element('//*[@id="post-visibility-select"]/p/a[1]')

        updated_state = self.driver.find_element_by_xpath('//*[@id="post-visibility-display"]').text

        if (visibility == 'public' and updated_state == 'Public') or \
                (visibility == 'public_sticky' and updated_state == 'Public, Sticky') or \
                (visibility == 'protected' and updated_state == 'Password Protected') or \
                (visibility == 'private' and updated_state == 'Private'):
            print('[+] Changing visibility successfully')
        else:
            self.success = False
            print('[-] Failed to change visibility, current visibility does not match')

    def change_publish_datetime(self, year=None, month=None, day=None, hour=None, minute=None):
        print('[+] Changing publishing datetime')
        trans_mon_str = ['', '01-Jan', '02-Feb', '03-Mar', '04-Apr', '05-May', '06-Jun', '07-Jul', '08-Aug', '09-Sep',
                         '10-Oct', '11-Nov', '12-Dec']
        self.click_element('//*[@id="misc-publishing-actions"]/div[3]/a')

        if year is not None:
            self.fill_textbox('//*[@id="aa"]', str(year))
        if month is not None:
            self.select_dropdown('//*[@id="mm"]', trans_mon_str[month])
        if day is not None:
            self.fill_textbox('//*[@id="jj"]', str(day))
        if hour is not None:
            self.fill_textbox('//*[@id="hh"]', str(hour))
        if minute is not None:
            self.fill_textbox('//*[@id="mn"]', str(minute))

        self.click_element('//*[@id="timestampdiv"]/p/a[1]')

        # Check datetime in format like 09-Sep 04, 2018 @ 14 : 47
        publishing_datetime = '%s %d, %d @ %d : %d' % (trans_mon_str[month], day, year, hour, minute)
        if publishing_datetime == self.driver.find_element_by_xpath('//*[@id="timestamp"]/b').text:
            print('[+] Changing publishing datetime successfully')
        else:
            self.success = False
            print('[-] Current publishing datetime does not match')


    def add_tags(self, tag_list):
        print('[+] Adding tags')
        if len(tag_list) == 0:
            print('[!] No tag provided')
            return
        tag_str = ''
        for tag in tag_list:
            tag_str += tag + ','
        tag_str = tag_str[:-1]

        self.fill_textbox('//*[@id="new-tag-post_tag"]', tag_str)
        self.click_element('//*[@id="new-tag-post_tag"]/../input[2]')

        ele = self.driver.find_elements_by_xpath('//*[@id="post_tag"]/div[2]/span')
        updated_tag_list = []
        for e in ele:
            updated_tag_list.append(e.text[e.text.rfind(' ')+1:])
        for tag in tag_list:
            if tag not in updated_tag_list:
                self.success = False
                print('[-] Adding tag %s failed' % tag)
                return
        print('[+] Adding tag finished')

    def new_post_tests(self):
        self.init_new_post() if self.success else None
        # self.select_category(2) if self.success else None
        # self.add_title_text('Test') if self.success else None
        # self.add_body_text('<h2>This is a test article.</h2>\n<p>This is a paragraph. 12345</p>') if self.success else None
        # self.add_excerpt('This is a test') if self.success else None
        # self.change_status('Pending Review')
        # self.change_visibility('private')
        # self.change_publish_datetime(2017,8,9,1,2)
        self.add_tags(['test', 'example'])
        # self.save_post() if self.success else None
        # self.preview_post() if self.success else None
        # self.publish_post() if self.success else None
        if self.success:
            print('[+] New post test finished')


if __name__ == '__main__':
    # Test chrome driver
    test = WPTest390()
    test.login('admin', 'Admin123456')

    test.new_post_tests()

    # test.close_all(delay=3)
