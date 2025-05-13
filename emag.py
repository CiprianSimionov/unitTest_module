import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class TestEmag(unittest.TestCase):
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://www.emag.ro/")

    def tearDown(self):
        self.chrome.quit() #Close browser and shut down the ChromiumDriver exe.

    def test_search_products(self):
        self.chrome.implicitly_wait(3)
        self.chrome.find_element(By.CSS_SELECTOR, "input[id=\"searchboxTrigger\"]").send_keys("Iphone 15 pro max")
        self.chrome.find_element(By.CSS_SELECTOR, "button[class*=\"searchbox-submit\"]").click()
        self.chrome.find_element(By.CSS_SELECTOR, "div[class*=\"card-item\"]:nth-of-type(4)").click()
        self.chrome.find_element(By.CSS_SELECTOR, "a[title=\"512 GB\"]").click()
        self.chrome.find_element(By.CSS_SELECTOR, "div[class=\"product-buy-area-wrapper\"] > div > button[type=\"submit\"]").click()
        self.chrome.implicitly_wait(3)
        self.chrome.find_element(By.XPATH, "//a[contains(text(), \"Vezi detalii cos\")]").click()
        self.chrome.implicitly_wait(3)
        container = self.chrome.find_element(By.CLASS_NAME, "cart-line")
        self.assertTrue(container, "Container is not empty")
        # pret = self.chrome.find_element(By.XPATH, "//div[@class=\"order-summary-total\"] / div / p[contains(text(), \"7.699\")]")
        # assert pret, "7.699"


