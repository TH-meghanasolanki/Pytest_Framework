import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.Product_Purchase import Purchase_mobile

def test_addtocart(userlogin):
    
    mobiledevice = Purchase_mobile(userlogin)

    
   