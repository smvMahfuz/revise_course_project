import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class test_auto_suggestion:
    def demo_auto_suggestion_value(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.set_page_load_timeout(10)
        time.sleep(2)
        depart_form = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_form.click()
        time.sleep(2)
        depart_form.send_keys("Dhaka")
        time.sleep(2)
        depart_form.send_keys(Keys.ENTER)
        time.sleep(2)
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        time.sleep(2)
        search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for results in search_result:
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(2)
                break

        driver.find_element(By.ID, "BE_flight_origin_date").click()
        driver.find_element(By.ID, "28/09/2022").click()
        time.sleep(5)


test_auto = test_auto_suggestion()
test_auto.demo_auto_suggestion_value()
