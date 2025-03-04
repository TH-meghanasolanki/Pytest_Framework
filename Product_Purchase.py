import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Purchase_mobile():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.device1 = (By.LINK_TEXT, "Samsung galaxy s6")
        self.Addtocart = (By.XPATH, "//*[@id='tbodyid']/div[2]/div/a")

    def mobiledevice(self):
        self.wait.until(EC.element_to_be_clickable)(self.device1).click()
        self.wait.until(EC.element_to_be_clickable)(self.Addtocart).click()
