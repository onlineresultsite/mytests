# tests/test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed and in PATH
    
    # Open the login page
    driver.get("http://127.0.0.1:8000/login/")  # Update with your login URL
    
    # Find the username and password input elements
    username_input = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div/div/div[1]/div/form/div[1]/input")  # Update if different
    password_input = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div/div/div[1]/div/form/div[2]/input")  # Update if different
    
    # Enter the username and password
    username_input.send_keys("akshay")  # Update with a valid username
    password_input.send_keys("akTR@300")  # Update with a valid password
    
    # Submit the form
    password_input.send_keys(Keys.RETURN)
    
    # Wait for the page to load
    time.sleep(2)  # Adjust if needed
    
    # Check if login was successful
    assert "Logout" in driver.page_source  # Update with a string that indicates successful login

    # Close the browser
    driver.quit()
