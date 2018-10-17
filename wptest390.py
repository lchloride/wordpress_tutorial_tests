import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from wptest import WPTest


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
        self.get_by_relative_url('wp-admin/post-new.php')
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
        self.to_page_top()
        self.fill_textbox('//*[@id="title"]', text)

    def add_body_text(self, text):
        print('[+] Adding body...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()
        self.click_element('//*[@id="content-html"]')
        self.fill_textbox('//*[@id="content"]', text)

    def preview_post(self):
        print('[+] Preview post...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()
        self.click_element('//*[@id="post-preview"]')

    def save_post(self):
        print('[+] Saving post...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()
        self.click_element('//*[@id="save-post"]')

    def publish_post(self):
        print('[+] Publishing post...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()
        self.click_element('//*[@id="publish"]')
        if self.wait_for_text_in_page('Post published.') is None:
            print('[-] Publishing failed')

    def select_category(self, idx):
        print('[+] Select category...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

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
        self.to_page_top()

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
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        # If article is private, we cannot change its status
        if self.driver.find_element_by_xpath('//*[@id="post-status-display"]').text == 'Privately Published':
            print('[!] Cannot set status since this article is private')
            return
        self.click_element('//*[@id="misc-publishing-actions"]/div[1]/a')
        # styles = StyleParser(self.driver.find_element_by_xpath('//*[@id="post-status-select"]')
        #                     .get_attribute('style'))
        # if styles.get_style_value('display') == 'none':
        time.sleep(1)
        self.select_dropdown('//*[@id="post_status"]', status_text)
        self.click_element('//*[@id="post-status-select"]/a[1]')
        if self.wait_for_text_in_page(status_text) is None:
            self.success = False
            print('[-] Changing status failed')

    # Change visibility of article
    def change_visibility(self, visibility="public", password=None):
        print('[+] Changing visibility')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

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

        time.sleep(1)

    def change_publish_datetime(self, year=None, month=None, day=None, hour=None, minute=None):
        print('[+] Changing publishing datetime')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

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
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

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
            updated_tag_list.append(e.text[e.text.rfind(' ') + 1:])
        for tag in tag_list:
            if tag not in updated_tag_list:
                self.success = False
                print('[-] Adding tag %s failed' % tag)
                return
        print('[+] Adding tag finished')

    def set_feature_image_by_uploading(self, image_path):
        print('[+] Selecting feature image...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        self.click_element('//*[@id="set-post-thumbnail"]')

        self.click_element('//*[@id="__wp-uploader-id-0"]/div[3]/div/a[1]')

        self.upload_file_input('//*[@id="__wp-uploader-id-0"]/div[@class="moxie-shim moxie-shim-html5"]/input',
                               image_path)

        if self.wait_for_text_in_page("Edit Image"):
            time.sleep(1)
            self.click_element('//*[@id="__wp-uploader-id-0"]/div[5]/div/div[2]/a')  # Can be improved by class name
            if self.wait_for_text_in_page('Remove featured image'):
                print('[+] Setting feature image finished')
            else:
                self.success = False
                print('[-] Failed to set uploaded image')
        else:
            self.success = False
            print('[-] Failed to set uploaded image')

    def set_traceback(self, link):
        print('[+] Setting traceback link')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        if self.driver.find_element_by_xpath('//*[@id="trackback_url"]').is_displayed():
            self.fill_textbox('//*[@id="trackback_url"]', link)
            print('[+] Setting traceback link finished')
        else:
            self.success = False
            print('[-] Traceback textbox not found')

    def add_custom_fields(self, fields):
        print('[*] Adding custom fields...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        for name in fields.key():
            value = fields[name]
            if self.driver.find_element_by_xpath('//*[@id="newmetaleft"]/a').is_displayed():
                # There exists a field, click "Enter new" first
                self.click_element('//*[@id="newmetaleft"]/a')

            # Fill in field
            self.fill_textbox('//*[@id="metakeyinput"]', name)
            self.fill_textbox('//*[@id="metavalue"]', value)
            self.click_element('//*[@id="newmeta-submit"]')

        if self.success:
            print('[+] Adding custom fields finished')
        else:
            print('[+] Failed to addi custom fields')

    def change_slug(self, name):
        print('[+] Changing slug')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        self.fill_textbox('//*[@id="post_name"]', name)
        print('[+] Changing slug finished')

    def change_discussion_state(self, comments=False, ping_status=False):
        print('[+] Changing discussion state')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        current_comment_state = self.checkbox_is_checked('//*[@id="comment_status"]')
        if current_comment_state != comments:
            self.click_element('//*[@id="comment_status"]')
        current_ping_status = self.checkbox_is_checked('//*[@id="ping_status"]')
        if current_ping_status != ping_status:
            self.click_element('//*[@id="ping_status"]')
        if self.success:
            print('[+] Changing discussion state finished')
        else:
            print('[-] Failed to change discussion state')

    # format_name should be one of the standard, aside, image, video, audio, quote, link, gallery
    def change_format(self, format_name='standard'):
        print('[+] Changing format')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        format_name = format_name.lower()
        if format_name not in ['standard', 'aside', 'image', 'video', 'audio', 'quote', 'link', 'gallery']:
            print('[!] Invalid format name %s, using standard instead' % format_name)
        self.click_element('//*[@id="post-format-' + format_name + '"]')
        if self.success:
            print('[+] Changing format finished')
        else:
            print('[-] Failed to change format')

    def move_to_trash_post_page(self):
        print('[+] Moving post to trash')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'

        self.click_element('//*[@id="delete-action"]/a')
        if self.wait_for_text_in_page('1 post moved to the Trash.'):
            print('[+] Moving post to trash finished')
        else:
            self.success = False
            print('[-] Failed to move post to trash')

    def new_post_tests(self):
        self.init_new_post() if self.success else None
        self.select_category(2) if self.success else None
        self.add_title_text('Test') if self.success else None
        self.add_body_text(
            '<h2>This is a test article.</h2>\n<p>This is a paragraph. 12345</p>') if self.success else None
        self.add_excerpt('This is a test') if self.success else None
        self.change_status('Pending Review') if self.success else None
        self.change_visibility('private') if self.success else None
        self.change_publish_datetime(2017, 8, 9, 1, 2) if self.success else None
        self.add_tags(['test', 'example']) if self.success else None
        self.set_feature_image_by_uploading(os.path.abspath('./leaf.png')) if self.success else None
        self.set_traceback('http://localhost/wordpress3_9/?p=1') if self.success else None
        self.change_format('image') if self.success else None
        self.change_slug('another-title') if self.success else None
        self.change_discussion_state(comments=True, ping_status=False) if self.success else None
        # self.save_post() if self.success else None if self.success else None
        self.preview_post() if self.success else None if self.success else None
        # self.publish_post() if self.success else None if self.success else None
        # self.move_to_trash_post_page()
        if self.success:
            print('[+] New post test finished')

    def init_theme_tests(self):
        print('[*] Starting theme tests...')
        self.get_by_relative_url('wp-admin/themes.php')
        # Must logged in to post new article
        assert self.driver.get_cookie('wp_login') != 'success', \
            '[-] Cannot initialize theme page: login failed'
        if self.success:
            self.driver.add_cookie({'name': 'wp_theme_init', 'value': 'success'})
            print('[+] Test initialization finished')

    def upload_theme(self, theme_path):
        print('[+] Uploading theme')
        self.get_by_relative_url('wp-admin/theme-install.php')
        if not self.wait_for_text_in_page('Upload Theme'):
            self.success = False
            print('[-] Cannot open theme installation page')
            return

        self.click_element('//*[@class="upload add-new-h2"]')

        self.upload_file_input('//*[@name="themezip"]', theme_path)

        timeout = 10
        while self.driver.find_element_by_xpath('//*[@id="install-theme-submit"]').get_attribute('disabled'):
            if timeout <= 0:
                self.success = False
                print('[-] Failed to specify file to be upload')
                return
            timeout -= 1
            time.sleep(1)

        self.click_element('//*[@id="install-theme-submit"]')

        if self.wait_for_text_in_page('Theme installed successfully.'):
            print('[+] Uploading theme finished')
        else:
            self.success = False
            print('[-] Failed to upload theme, provided information:\n %s'
                  % self.driver.find_element_by_xpath('//*[@id="wpbody-content"]/div[3]'))

    def activate_theme(self, theme_name):
        print('[+] Activating theme')
        ele = self.driver.find_element_by_xpath('//*[@aria-describedby="%s-action %s-name"]' % (theme_name, theme_name))
        if ele is None:
            self.success = False
            print('[-] Theme with name %s not found' % theme_name)
            return

        ele.find_element_by_xpath('//*/a[@class="button button-primary activate"]').click()

        if self.wait_for_text_in_page('New theme activated'):
            print('[+] Activating theme finished')
        else:
            self.success = False
            print('[-] Failed to activate theme')

    def change_background_color_theme_twentyten(self, color_code):
        print('[+] Changing background color')
        self.get_by_relative_url('wp-admin/customize.php')

        if not self.wait_for_text_in_page('You are previewing'):
            self.success = False
            print('[-] Failed to load customization page')
            return

        self.click_element('//*[@id="accordion-section-colors"]')

        if not self.wait_for_text_in_page('Background Color'):
            self.success = False
            print('[-] Failed to show control panel of color')
            return

        ele = self.driver.find_element_by_xpath(
            '//*[@id="customize-control-background_color"]/label/div/div/a')
        # //*[@id="customize-control-background_color"]/label/div/div/a
        # //*[@id="customize-control-background_color"]/*/[@title="Select Color"]

        if ele is None:
            self.success = False
            print('[-] Failed to find color picker')
            return

        ele.click()

        timeout = 10
        while 'wp-picker-open' not in ele.get_attribute('class'):
            if timeout <= 0:
                self.success = False
                print('[-] Failed to load color picker')
                return
            timeout -= 1

        self.fill_textbox('//*[@id="customize-control-background_color"]/label/div/div/span/input[1]',
                          color_code)

        time.sleep(1)

        if 'iris-error' in self.driver.find_element_by_xpath(
                '//*[@id="customize-control-background_color"]/label/div/div/span/input[1]').get_attribute('class'):
            self.success = False
            print('[-] Invalid color code format')
            return

        self.click_element('//*[@id="save"]')

        timeout = 10
        while self.driver.find_element_by_xpath('//*[@id="save"]').get_attribute('value') != 'Saved':
            if timeout <= 10:
                self.success = False
                print('[-] Failed to save changes')
                return
            timeout -= 1

        print('[+] Changing background color finished')

    def theme_tests(self):
        self.init_theme_tests()
        # self.upload_theme(os.path.abspath('./twentyten.2.5.zip'))
        # self.activate_theme('twentyten')
        self.change_background_color_theme_twentyten('#d8d8d8')

    def change_site_title(self, title):
        print('[+} Changing site title')
        self.get_by_relative_url('wp-admin/options-general.php')
        self.fill_textbox('//*[@id="blogname"]', title)
        self.click_element('//*[@id="submit"]')
        if self.wait_for_text_in_page('Settings saved.'):
            print('[+] Site title changed')
        else:
            self.success = False
            print('[-] Failed to change site title')

    def change_default_post_format(self, new_format='Standard'):
        print('[+] Changing default post format')
        self.get_by_relative_url('wp-admin/options-writing.php')
        self.select_dropdown('//*[@id="default_post_format"]', new_format)
        self.click_element('//*[@id="submit"]')
        if self.wait_for_text_in_page('Settings saved.'):
            print('[+] Default post format changed')
        else:
            self.success = False
            print('[-] Failed to change default post format')

    def change_posts_per_page(self, count):
        print('[+] Changing posts per page')
        self.get_by_relative_url('wp-admin/options-reading.php')
        self.fill_textbox('//*[@id="posts_per_page"]', count)
        self.click_element('//*[@id="submit"]')
        if self.wait_for_text_in_page('Settings saved.'):
            print('[+] Posts per page changed')
        else:
            self.success = False
            print('[-] Failed to change posts per page')

    # Level is an integer from 2 to 10
    def change_nested_comment_level(self, level):
        print('[+] Changing nested comment level')
        self.get_by_relative_url('wp-admin/options-discussion.php')
        if not self.checkbox_is_checked('//*[@id="thread_comments"]'):
            self.click_element('//*[@id="thread_comments"]')
        if not 2 <= level <= 10 or type(level) != int:
            self.success = False
            print('[-] Level should be an integer from 2 to 10')
            return

        self.select_dropdown('//*[@id="thread_comments_depth"]', str(level))
        self.click_element('//*[@id="submit"]')
        if self.wait_for_text_in_page('Settings saved.'):
            print('[+] Nested comment level changed')
        else:
            self.success = False
            print('[-] Failed to change nested comment level')

    def change_media_medium_size(self, max_width, max_height):
        print('[+] Changing media medium size')
        self.get_by_relative_url('wp-admin/options-media.php')
        self.fill_textbox('//*[@id="medium_size_w"]', max_width)
        self.fill_textbox('//*[@id="medium_size_h"]', max_height)
        self.click_element('//*[@id="submit"]')
        if self.wait_for_text_in_page('Settings saved.'):
            print('[+] Nested comment level changed')
        else:
            self.success = False
            print('[-] Failed to change nested comment level')

    def change_permalink_category_base(self, base):
        print('[+] Changing permalink category base')
        self.get_by_relative_url('wp-admin/options-permalink.php')
        self.fill_textbox('//*[@id="category_base"]', base)
        self.click_element('//*[@id="submit"]')
        if self.wait_for_text_in_page('Permalink structure updated.'):
            print('[+] Category base of permalink changed')
        else:
            self.success = False
            print('[-] Failed to change category base of permalink')

    def setting_tests(self):
        print('[*] Starting setting tests...')
        assert self.driver.get_cookie('wp_login') != 'success', '[-] Cannot initialize setting page: login failed'

        self.change_site_title('wp3_9_test') if self.success else None
        self.change_default_post_format('Image') if self.success else None
        self.change_posts_per_page(15) if self.success else None
        self.change_nested_comment_level(6) if self.success else None
        self.change_media_medium_size(400, 400) if self.success else None
        self.change_permalink_category_base('category') if self.success else None
        if self.success:
            print('[+] Setting tests finished')

    # Category & Tag tests

    def add_category(self, name, slug, description, parent="None", is_tag=False):
        print('[+] Adding category/tag')
        if not is_tag:
            self.get_by_relative_url('wp-admin/edit-tags.php?taxonomy=category')
        else:
            self.get_by_relative_url('wp-admin/edit-tags.php?taxonomy=post_tag')

        self.fill_textbox('//*[@id="tag-name"]', name)
        self.fill_textbox('//*[@id="tag-slug"]', slug)
        if not is_tag:
            self.select_dropdown('//*[@id="parent"]', str(parent))
        self.fill_textbox('//*[@id="tag-description"]', description)
        self.click_element('//*[@id="submit"]')

        if self.wait_for_text_in_page('A term with the name and slug provided already exists.'):
            self.success = False
            print('[-] Cannot create category/tag since a term with the name and slug provided already exists')
            return
        else:
            print('[+] Category/Tag added')

    def quick_edit_category(self, id, new_name, new_slug, is_tag=False):
        print('[+] Quick Editing category/tag')
        if not is_tag:
            self.get_by_relative_url('wp-admin/edit-tags.php?taxonomy=category')
        else:
            self.get_by_relative_url('wp-admin/edit-tags.php?taxonomy=post_tag')

        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath('//*[@id="tag-%d"]/td[1]' % id))
        hover.perform()

        self.click_element('//*[@id="tag-%d"]/td[1]/div[1]/span[2]/a' % id)
        self.fill_textbox('//*[@name="name"]', new_name)
        self.fill_textbox('//*[@name="slug"]', new_slug)
        self.click_element('//*[@class="inline-edit-save submit"]/a[2]')
        error = self.driver.find_element_by_xpath('//*[@class="inline-edit-save submit"]/span[@class="error"]')
        if not error.is_displayed():
            self.success = False
            print('[-] Failed to update category/tag: %s', error.text)
        else:
            print('[+] Category/Tag updated')

    def category_tag_tests(self):
        print('[*] Starting category/tag tests')
        # self.add_category('test_name', 'test-slug', 'This is a test category', parent='Test')
        # self.add_category('test_tag', 'test-tag-slug', 'This is a test tag', is_tag=True)
        self.quick_edit_category(id=5, new_name='new_name', new_slug='new-slug', is_tag=True)
        if self.success:
            print('[+] Category/Tag tests finished')


if __name__ == '__main__':
    # Test chrome driver
    test = WPTest390()
    test.login('admin', 'Admin123456')

    # test.new_post_tests()

    # test.theme_tests()

    # test.setting_tests()

    test.category_tag_tests()

    test.close_all(delay=3)
