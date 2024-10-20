from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BaseScraper(ABC):
    def __init__(self, driver_path):
        self.service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(10)

    def open_profile(self, url):
        self.driver.get(url)

    @abstractmethod
    def scrape_profile(self):
        pass

    def get_element_text(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return element.text
        except Exception as e:
            print(f"Error fetching element: {xpath} - {str(e)}")
            return None

    def close(self):
        time.sleep(10)
        self.driver.quit()
