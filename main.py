import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="./chromedriver.exe")

driver.get("https://www.google.com/")

try:
    search_field = driver.find_element(By.NAME, "q")
    search_field.send_keys("Калькулятор")

    search_button = driver.find_elements(By.CLASS_NAME, "gNO89b")[1]
    search_button.click()

    num_1 = driver.find_element(By.XPATH, "//div[text()='1']")
    num_2 = driver.find_element(By.XPATH, "//div[text()='2']")
    num_3 = driver.find_element(By.XPATH, "//div[text()='3']")

    minus = driver.find_element(By.XPATH, "//div[text()='−']")
    plus = driver.find_element(By.XPATH, "//div[text()='+']")
    mul = driver.find_element(By.XPATH, "//div[text()='×']")
    equal = driver.find_element(By.XPATH, "//div[text()='=']")

    num_1.click()
    mul.click()
    num_2.click()
    minus.click()
    num_3.click()
    plus.click()
    num_1.click()
    equal.click()

    condition = driver.find_element(By.XPATH, "//span[@class='vUGUtc']")
    result = driver.find_element(By.ID, "cwos")

    assert condition.text.strip() == "1 × 2 - 3 + 1 =", "Incorrect condition"
    assert result.text == "0", "Incorrect result"

    time.sleep(5)
except Exception as e:
    driver.quit()
    print(e)