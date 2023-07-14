from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_NEW_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_RES_LBL = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_MAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_SEND = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.info(f"Send '{word}' to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operate with {locator}")
            return False
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.info(f"We found text {text} in field {element_name}")
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception while click")
            return False
        logging.info(f"Clicked {element_name} button")
        return True

    # ENTER_TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_LOGIN_FIELD, word, description="Enter Login")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_PASS_FIELD, word, description="Enter password")

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_DESCRIPTION, word, description="Enter Description")

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTENT, word, description="Enter Content")

    def enter_contact_name(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTACT_NAME, word, description="Enter Contact Name")

    def enter_contact_mail(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTACT_MAIL, word, description="Enter Mail")

    def enter_contact_content(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTACT_CONTENT, word,
                                   description="Enter contact content")

    # GET_TEXT
    def get_res_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_RES_LBL, description="Get result text")

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_ERROR_FIELD, description="Get error text")

    def get_user_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_HELLO, description="Get user text")

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text

    # CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.LOCATOR_LOGIN_BTN, description="Login button")

    def click_contact_send_btn(self):
        self.click_button(TestSearchLocators.LOCATOR_CONTACT_SEND, description="Locator send button")

    def click_contact_link(self):
        self.click_button(TestSearchLocators.LOCATOR_CONTACT_BTN, description="contact link button")

    def click_save_btn(self):
        self.click_button(TestSearchLocators.LOCATOR_SAVE_BTN, description="save")
