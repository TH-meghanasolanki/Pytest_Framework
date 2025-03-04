
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class SignupPage:
    def __init__(self, driver):
        # Define locators
        self.driver = driver
        self.signup_link = (By.ID, "signin2")
        self.username_field = (By.ID, "sign-username")
        self.password_field = (By.ID, "sign-password")
        self.signup_button = (By.XPATH, "//button[normalize-space()='Sign up']")

    def sign_up(self,username,password):
        self.driver.find_element(*self.signup_link).click()  # Click on Sign up button
        self.driver.find_element(*self.username_field).send_keys(username)  # Enter username
        self.driver.find_element(*self.password_field).send_keys(password)  # Enter password
        self.driver.find_element(*self.signup_button).click()  # Click Sign up button
