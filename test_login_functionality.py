import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By


class Test_Login_Functionalitiy:
    @pytest.fixture()
    def test_setup(self):
        global driver
        # Path to the chromedriver executable
        chromedriver_path = 'C:\\Users\\User\\PycharmProjects\\web_automation\\chromedriver.exe'
        service = Service(executable_path=chromedriver_path)

        # initializing webdriver
        driver = webdriver.Chrome(service=service)
        sleep(3)


        yield
        print("Congratulations! Test is PASSED")

        driver.close()
        driver.quit()


    def test_login_functionality01(self,test_setup):
        driver.get("https://bankofamerica.com/")
        driver.find_element(By.ID, 'onlineId1').send_keys('tanjina@gmail.com')
        driver.find_element(By.XPATH, '//*[@id="passcode1"]').send_keys('me123')
        driver.find_element(By.XPATH, '//*[@id="signIn"]/span[1]').click()


    def test_login_functionality02(self, test_setup):
            driver.get("https://bankofamerica.com/")
            driver.find_element(By.ID, 'onlineId1').send_keys('tanjina@gmail.com')
            driver.find_element(By.XPATH, '//*[@id="passcode1"]').send_keys('me123')
            driver.find_element(By.XPATH, '//*[@id="signIn"]/span[1]').click()


    def test_login_functionality03(self,test_setup):
        driver.get("https://bankofamerica.com/")
        driver.find_element(By.ID, 'onlineId1').send_keys('tanjina@gmail.com')
        driver.find_element(By.XPATH, '//*[@id="passcode1"]').send_keys('me123')
        driver.find_element(By.XPATH, '//*[@id="signIn"]/span[1]').click()
