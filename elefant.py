import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class TestElefant(unittest.TestCase):
    #method to set conditions for each tests
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://www.elefant.ro/")

    def tearDown(self):
        self.chrome.quit() #Close browser and shut down the ChromiumDriver exe.


    def test_search_products(self):
        time.sleep(4)
        self.chrome.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
        #self.chrome.find_element(By.XPATH, "//a[contains(text(), \"inapoi in site\")]").click()
        self.chrome.find_element(By.XPATH, "//input[@name=\"SearchTerm\"]").send_keys("jovan")
        self.chrome.find_element(By.XPATH, "//button[contains(@class, \"btn-search\")]").click()
        time.sleep(3)
        produse = self.chrome.find_elements(By.CLASS_NAME, "product-title")
        assert len(produse) == 6

    def test_search_products_with_waits(self):
        WebDriverWait(self.chrome, 6).until(EC.presence_of_element_located((By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')))
        self.chrome.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
        #self.chrome.find_element(By.XPATH, "//a[contains(text(), \"inapoi in site\")]").click()
        self.chrome.find_element(By.XPATH, "//input[@name=\"SearchTerm\"]").send_keys("jovan")
        self.chrome.find_element(By.XPATH, "//button[contains(@class, \"btn-search\")]").click()
        self.chrome.implicitly_wait(6)  # awaits for products to load on page
        produse = self.chrome.find_elements(By.CLASS_NAME, "product-title")
        assert len(produse) == 6

    def test_search_products_with_keys_library(self):
        WebDriverWait(self.chrome, 8).until(EC.presence_of_element_located((By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')))
        self.chrome.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
        #self.chrome.find_element(By.XPATH, "//a[contains(text(), \"inapoi in site\")]").click()
        self.chrome.find_element(By.XPATH, "//input[@name=\"SearchTerm\"]").send_keys("jovann")
        self.chrome.find_element(By.XPATH, "//input[@name=\"SearchTerm\"]").send_keys(Keys.BACKSPACE)
        self.chrome.find_element(By.XPATH, "//input[@name=\"SearchTerm\"]").send_keys(Keys.ENTER)
        self.chrome.implicitly_wait(8)
        produse = self.chrome.find_elements(By.CLASS_NAME, "product-title")
        assert len(produse) == 6

