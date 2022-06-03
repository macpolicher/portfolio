from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service('D:/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=s)


def test_login_with_correct_credentials():
    driver.get('https://www.saucedemo.com/')
    # maximize window
    driver.maximize_window()

    # input username
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys('standard_user')
    # input password
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    # click login button
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    # get current url
    current_url = driver.current_url
    # assert if user was able to log in
    assert current_url == "https://www.saucedemo.com/inventory.html"


def test_login_with_locked_out_user():
    driver.get('https://www.saucedemo.com/')
    # maximize window
    driver.maximize_window()

    # input username
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys('locked_out_user')
    # input password
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    # click login button
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    # assert error message for locked_out_user
    error_msg = driver.find_element(By.XPATH, '//*[@data-test="error"]').text

    assert error_msg == "Epic sadface: Sorry, this user has been locked out."


def test_problem_user():
    driver.get('https://www.saucedemo.com/')
    # maximize window
    driver.maximize_window()

    # input username
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys('locked_out_user')
    # input password
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    # click login button
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    # assert error message for problem user
    error_msg = driver.find_element(By.XPATH, '//*[@data-test="error"]').text

    assert error_msg == "Epic sadface: Sorry, this user has been locked out."
