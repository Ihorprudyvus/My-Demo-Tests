from helpers import elements, HelperMethods, TestData, creds
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FigmaTestOlympicsSymbol(HelperMethods.GeneralMethods):

    def test_olympics_symbol(self):
        self.get_url(elements.URL.mainURL)
        self.click_on_the_element(elements.HomePage.login_button)
        frame = self.find_element(elements.LoginPopup.iframe)
        self.driver.switch_to.frame(frame)
        self.send_keys_to_element(elements.LoginPopup.email_field, creds.email)
        self.send_keys_to_element(elements.LoginPopup.password_field, creds.password)
        self.click_on_the_element(elements.LoginPopup.login_button)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                               elements.HomePage.search_label)))
        self.click_on_the_element(elements.HomePage.search_label)
        self.send_keys_to_specific_element(elements.HomePage.search_field, 1, TestData.project_name)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                               elements.HomePage.project_link))).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                              elements.HomePage.drawing_area))).click()
        self.send_keys_to_element('body', 'o')
        canvas = self.find_element(elements.HomePage.drawing_area)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'a')
        self.driver.find_element_by_tag_name('body').send_keys(Keys.BACK_SPACE)
        drawing = ActionChains(self.driver) \
            .click_and_hold(canvas) \
            .move_by_offset(30, 15) \
            .move_by_offset(20, 32) \
            .move_by_offset(50, 50) \
            .release()
        drawing.perform()
        self.click_on_the_element(elements.HomePage.drawing_area)
        self.click_on_the_element(elements.LeftOptionsBar.color_field)
        self.send_keys_to_element(elements.LeftOptionsBar.color_field, TestData.blue_color)
        self.driver.find_element_by_tag_name('body').send_keys('o')
        drawing.perform()
        self.click_on_the_element(elements.HomePage.drawing_area)
        self.click_on_the_element(elements.LeftOptionsBar.color_field)
        self.send_keys_to_element(elements.LeftOptionsBar.color_field, TestData.green_color)
        self.driver.find_element_by_tag_name('body').send_keys('o')
        drawing.perform()
        self.click_on_the_element(elements.HomePage.drawing_area)
        self.click_on_the_element(elements.LeftOptionsBar.color_field)
        self.send_keys_to_element(elements.LeftOptionsBar.color_field, TestData.yellow_color)
        self.driver.find_element_by_tag_name('body').send_keys('o')
        drawing.perform()
        self.click_on_the_element(elements.HomePage.drawing_area)
        self.click_on_the_element(elements.LeftOptionsBar.color_field)
        self.send_keys_to_element(elements.LeftOptionsBar.color_field, TestData.red_color)
        self.driver.find_element_by_tag_name('body').send_keys('o')
        drawing.perform()
        self.click_on_the_element(elements.HomePage.drawing_area)
        self.click_on_the_element(elements.LeftOptionsBar.color_field)
        self.send_keys_to_element(elements.LeftOptionsBar.color_field, TestData.black_color)
        time.sleep(1)

        action = ActionChains(self.driver).move_to_element(canvas).move_by_offset(80,
                                                                                  80).click_and_hold().move_by_offset(
            80, 0).release()
        action.perform()
        time.sleep(1)
        action = ActionChains(self.driver).move_to_element(canvas).move_by_offset(70,
                                                                                  80).click_and_hold().move_by_offset(
            160, 0).release()
        action.perform()
        time.sleep(1)
        action = ActionChains(self.driver).move_to_element(canvas).move_by_offset(10,
                                                                                  20).click_and_hold().move_by_offset(
            40, 50).release()
        action.perform()
        time.sleep(1)
        action = ActionChains(self.driver).move_to_element(canvas).move_by_offset(10,
                                                                                  20).click_and_hold().move_by_offset(
            120, 50).release()
        action.perform()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'a')
        self.driver.find_elements_by_css_selector(elements.LeftOptionsBar.opacity_options)[0].click()
        self.driver.find_elements_by_css_selector(elements.LeftOptionsBar.opacity_options)[0].send_keys(TestData.
                                                                                                        opacity_level)
        self.driver.find_elements_by_css_selector(elements.LeftOptionsBar.opacity_options)[0].send_keys(Keys.ENTER)
        self.driver.find_element_by_tag_name('body').send_keys('t')

        action = ActionChains(self.driver).move_to_element(canvas).move_by_offset(60, 150).click()\
            .send_keys('My Olympics Prototype')
        action.perform()
        circles_list = self.find_elements(elements.RightMenu.right_options_list)
        if len(circles_list) == 5:
            pass
        else:
            self.fail('Incorrect circles count')
        time.sleep(5)

