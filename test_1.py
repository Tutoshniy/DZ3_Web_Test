import logging
import time

import yaml

from testpage import OperationHelper

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata["username"]
passwd = testdata["password"]


def test_step1(browser):
    logging.info("Test 1 start")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test 2 start")
    testpage = OperationHelper(browser)
    testpage.enter_login(name)
    testpage.enter_pass(passwd)
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {name}"


def test_step3(browser):
    logging.info("Test 3 start")
    testpage = OperationHelper(browser)
    testpage.click_contact_link()
    testpage.enter_contact_name("Tester")
    testpage.enter_contact_mail("Tester@gb.ru")
    testpage.enter_contact_content("Testing contact send")
    testpage.click_contact_send_btn()
    time.sleep(4)
    print(testpage.switch_to_contact_alert())
    assert testpage.switch_to_contact_alert() == "Form successfully submitted"
