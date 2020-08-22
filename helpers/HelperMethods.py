import unittest
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, WebDriverException, ElementNotVisibleException, \
    NoAlertPresentException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GeneralMethods(unittest.TestCase):   # this class is inherited from unittest class
    # & all tests will inherit it as well

    def setUp(self):    # mandatory method which is responsible for all start up settings
        options = webdriver.ChromeOptions()  # with the help of this variable we give Chrome appropriate view
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)

    def _test_has_failed(self):  # method which check if test ha failed, will be used in tearDown method
        for method, error in self._outcome.errors:
            if error:
                return True
        return False

    def highlight(self, selector, style):
        original_style = selector.get_attribute('style')
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", selector, style)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                   selector, original_style)

    def click_on_the_element(self, selector, attempts=5):
        count = 0
        while count < attempts:
            try:
                self.highlight(self.driver.find_element_by_css_selector(selector),
                               "background: green; border: 2px solid red;")
                self.driver.find_element_by_css_selector(selector).click()
                return
            except WebDriverException or NoSuchElementException or ElementNotVisibleException or \
                   ElementClickInterceptedException as e:
                if 'element is not attached to the page document' or 'is not clickable at point' in str(e):
                    time.sleep(0.2)
                    count = count + 1
                else:
                    raise e
        raise WebDriverException('Cannot find element:' + selector)

    def click_on_specific_element(self, selector, index, attempts=10):  # overwritten method for
        count = 0
        while count < attempts:
            try:
                self.highlight(self.driver.find_elements_by_css_selector(selector)[index],
                               "background: green; border: 2px solid red;")
                self.driver.find_elements_by_css_selector(selector)[index].click()
                return
            except WebDriverException or NoSuchElementException or ElementNotVisibleException or \
                   ElementClickInterceptedException as e:
                if 'element is not attached to the page document' or 'is not clickable at point' in str(e):
                    time.sleep(0.5)
                    count = count + 1
                else:
                    raise e
        raise WebDriverException('Cannot find element:' + selector)

    def send_keys_to_element(self, selector, keys, attempts=10):  # overwritten method for finding &
        count = 0
        while count < attempts:
            try:
                self.driver.find_element_by_css_selector(selector).send_keys(keys)
                return
            except WebDriverException or NoSuchElementException or ElementNotVisibleException as e:
                if 'element is not attached to the page document' in str(e) or WebDriverException or \
                        NoSuchElementException or ElementNotVisibleException:
                    time.sleep(0.5)

                    count = count + 1
                else:
                    raise e
        raise WebDriverException('Cannot find element:' + selector)

    def send_keys_to_specific_element(self, selector, index, keys, attempts=10):
        count = 0
        while count < attempts:
            try:
                self.driver.find_elements_by_css_selector(selector)[index].send_keys(keys)
                return
            except WebDriverException or NoSuchElementException or ElementNotVisibleException as e:
                if 'element is not attached to the page document' in str(e) or WebDriverException or \
                        NoSuchElementException or ElementNotVisibleException:
                    time.sleep(0.5)
                    count = count + 1
                else:
                    raise e
        raise WebDriverException('Cannot find element:' + selector)

    def get_url(self, url, time_to_load=None):
        if time_to_load:
            self.driver.set_page_load_timeout(time_to_load)
            self.driver.get(url)
        else:
            self.driver.get(url)

    def get_element_text(self, selector, attempts=5):
        count = 0
        while count < attempts:
            try:
                self.highlight(self.driver.find_element_by_css_selector(selector),
                               "background: blue; border: 2px solid red;")
                element = self.driver.find_element_by_css_selector(selector).text
                return element
            except WebDriverException or NoSuchElementException or ElementNotVisibleException as e:
                if 'element is not attached to the page document' in str(e) or WebDriverException or \
                        NoSuchElementException or ElementNotVisibleException:
                    time.sleep(0.3)
                    count = count + 1
                else:
                    raise e
        raise WebDriverException('Cannot find element:' + selector)

    def get_specific_element_text(self, selector, index, attempts=5):
        count = 0
        while count < attempts:
            try:
                self.highlight(self.driver.find_elements_by_css_selector(selector)[index],
                               "background: blue; border: 2px solid red;")
                element = self.driver.find_elements_by_css_selector(selector)[index].text
                return element
            except WebDriverException or NoSuchElementException or ElementNotVisibleException as e:
                if 'element is not attached to the page document' in str(e) or WebDriverException or \
                        NoSuchElementException or ElementNotVisibleException:
                    time.sleep(0.5)
                    count = count + 1
                else:
                    raise e
        raise WebDriverException('Cannot find element:' + selector)

    def clear_field(self, selector, attempts=5):
        count = 0
        while count < attempts:
            try:
                self.driver.find_element_by_css_selector(selector).clear()
                return
            except WebDriverException or NoSuchElementException or ElementNotVisibleException as e:
                if 'element is not attached to the page document' in str(e) or WebDriverException or \
                        NoSuchElementException or ElementNotVisibleException:
                    time.sleep(0.5)
                    count = count + 1
                else:
                    raise e
        raise WebDriverException('Cannot find element:' + selector)

    def clear_specific_field(self, selector, index, attempts=5):
        count = 0
        while count < attempts:
            try:
                self.driver.find_elements_by_css_selector(selector)[index].clear()

                return
            except WebDriverException or NoSuchElementException or ElementNotVisibleException as e:
                if 'element is not attached to the page document' in str(e) or WebDriverException or \
                        NoSuchElementException or ElementNotVisibleException:
                    time.sleep(0.5)
                    count = count + 1
                else:
                    raise e
        raise WebDriverException('Cannot find element:' + selector)

    def check_if_element_is_displayed(self, selector):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
            self.highlight(self.driver.find_element_by_css_selector(selector),
                           "background: yellow; border: 2px solid red;")
        except:
            raise NoSuchElementException

    def accept_and_check_alert(self, alert_text=None, attempts=5):
        count = 0
        while count < attempts:
            try:
                alert = self.driver.switch_to.alert
                alert_text_to_compare = alert.text
                if alert_text:
                    self.assertEqual(alert_text, alert_text_to_compare, 'Incorrect alert appeared')
                else:
                    pass
                alert.accept()
                return
            except NoAlertPresentException as e:
                if 'no such alert' in str(e) or WebDriverException or \
                        NoSuchElementException or ElementNotVisibleException:
                    time.sleep(0.5)
                    count = count + 1
                else:
                    raise e
        alert = self.driver.switch_to.alert
        raise WebDriverException('Cannot find element:' + alert)

    def find_element(self, selector, attempts=5):
        count = 0
        while count < attempts:
            try:
                element = self.driver.find_element_by_css_selector(selector)
                return element
            except WebDriverException or NoSuchElementException or ElementNotVisibleException as e:
                if 'element is not attached to the page document' in str(e) or WebDriverException or \
                        NoSuchElementException or ElementNotVisibleException:
                    time.sleep(0.5)
                    count = count + 1
                else:
                    raise e
        raise WebDriverException('Cannot find element:' + selector)

    def find_elements(self, selector, attempts=5):
        count = 0
        while count < attempts:
            try:
                elements = self.driver.find_elements_by_css_selector(selector)
                return elements
            except Exception as e:
                if 'element is not attached to the page document' in str(e) or WebDriverException or \
                        NoSuchElementException or ElementNotVisibleException:
                    time.sleep(0.5)
                    count = count + 1
                else:
                    raise e
        raise WebDriverException('Cannot find element:' + selector)

    def drag_and_drop(self, selector_to_drag, selector_to_drop):
        source_element = self.find_element(selector_to_drag)
        destination_element = self.find_element(selector_to_drop)
        ActionChains(self.driver).click_and_hold(
            source_element).move_to_element(destination_element).release(source_element).perform()

    def hover(self, selector_to_hover):
        element_to_hover_over = self.find_element(selector_to_hover)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, selector):
        element = self.driver.find_element_by_css_selector(selector)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def text_comparison(self, selector_one=None, selector_two=None, text_to_compare=None):
        if selector_one and selector_two:
            self.assertEqual(self.get_element_text(selector_one), self.get_element_text(selector_two))
        else:
            self.assertEqual(self.get_element_text(selector_one), text_to_compare)

    def draw_colored_circle(self, canvas, x1, y1, x2, y2, x3, y3, color):
        drawing = ActionChains(self.driver) \
            .click_and_hold(canvas) \
            .move_by_offset(x1, y1) \
            .move_by_offset(x2, y2) \
            .move_by_offset(x3, y3) \
            .release()
        drawing.perform()
        canvas.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                             '[value="C4C4C4"]'))).click()
        self.send_keys_to_element('[value="C4C4C4"]', color)
        self.driver.find_element_by_tag_name('body').send_keys('o')

    def drag_action(self, canvas, x1, y1, x2, y2):
        time.sleep(1)
        action = ActionChains(self.driver).move_to_element(canvas).move_by_offset(x1,
                                                                                  y1).click_and_hold().move_by_offset(
            x2, y2).release()
        action.perform()
        time.sleep(1)

    def tearDown(self):
        if self._test_has_failed():
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # get current time
            self.driver.get_screenshot_as_file('helpers/screenshots/' + '%s.png' % now)  # get screen shot of the failre
        self.driver.quit()


