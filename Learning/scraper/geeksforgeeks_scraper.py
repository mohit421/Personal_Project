from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome WebDriver
service = Service(executable_path=r"C:\WebDriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Set implicit wait
driver.implicitly_wait(10)

# Open GeeksforGeeks profile
driver.get("https://www.geeksforgeeks.org/user/mohitjaiswal1/")

# Define a function to extract the text of elements based on their XPath
def get_element_text(xpath):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return element.text
    except TimeoutException:
        return "TimeoutException: Element not found"
    except NoSuchElementException:
        return "NoSuchElementException: Element not found"


try:
    # Retrieve tags statistics
    tags_xpaths = {
        "TotalProblemSolved": '//div[contains(text(),"Total Problem Solved")]//following::div[1]',
        "Easy": '//div[contains(text(),"EASY")]',
        "Medium": '//div[contains(text(),"MEDIUM")]',
        "Hard": '//div[contains(text(),"HARD")]',
    }

    # Loop through the tags to print their counts
    for tag, xpath in tags_xpaths.items():
        print(f"{tag}: {get_element_text(xpath)}")

except Exception as e:
    print("An unexpected error occurred:", str(e))

finally:
    time.sleep(10)  # Allow time to view results
    driver.quit()  # Ensure the browser is closed properly
