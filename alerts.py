import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestAlerts(unittest.TestCase):
    js_alert_button = (By.XPATH, "//button[@onclick=\"jsAlert()\"]")
    js_confirm_button = (By.XPATH, "//button[@onclick=\"jsConfirm()\"]")
    js_prompt_button = (By.XPATH, "//button[@onclick=\"jsPrompt()\"]")
    result_text = (By.ID, "result")

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.minimize_window()
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")

    def tearDown(self):
        self.chrome.quit()

    def test_jsalert(self):
        self.chrome.find_element(*self.js_alert_button).click()
        self.chrome.switch_to.alert.accept()
        result = self.chrome.find_element(*self.result_text)
        assert result.text == "You successfully clicked an alert"

    def test_jsconfirm_accept(self):
        self.chrome.find_element(*self.js_confirm_button).click()
        self.chrome.switch_to.alert.accept()
        result = self.chrome.find_element(*self.result_text)
        assert result.text == "You clicked: Ok"

    def test_jsconfirm_cancel(self):
        self.chrome.find_element(*self.js_confirm_button).click()
        self.chrome.switch_to.alert.dismiss()
        result = self.chrome.find_element(*self.result_text)
        assert result.text == "You clicked: Cancel"

    def test_jsprompt_accept(self):
        text = "text entered"
        self.chrome.find_element(*self.js_prompt_button).click()
        self.chrome.switch_to.alert.send_keys(text)
        self.chrome.switch_to.alert.accept()
        result = self.chrome.find_element(*self.result_text)
        assert result.text == f"You entered: {text}"

    def test_jsprompt_cancel(self):
        self.chrome.find_element(*self.js_prompt_button).click()
        self.chrome.switch_to.alert.dismiss()
        result = self.chrome.find_element(*self.result_text)
        assert result.text == f"You entered: null"

