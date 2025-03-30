from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (ensure the path to your ChromeDriver is correct)
service = Service(executable_path=r"C:\WebDriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the LeetCode profile page
driver.get("https://www.naukri.com/code360/profile/Epic")

# Function to get the text of an element
def get_element_text(xpath):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return element.text
    except Exception as e:
        print(f"Error fetching element: {xpath} - {str(e)}")
        return None

# XPaths of the elements
xpaths = {
    "Problem Solved": '//div[contains(text(),"Data Structures & Algorithms")]//following::div[contains(@class, "total")]',
    "Easy": '//div[contains(text(),"Data Structures & Algorithms")]//following::div[contains(@class, "total")]//following::div[1]//div[1]//div[@class="value"]',
    "Medium": '//div[contains(text(),"Data Structures & Algorithms")]//following::div[contains(@class, "total")]//following::div[1]//div[1]//div[@class="value"]',
    "Hard": '//div[contains(text(),"Data Structures & Algorithms")]//following::div[contains(@class, "total")]//following::div[1]//div[3]//div[@class="value"] ',
    "Ninja": '//div[contains(text(),"Data Structures & Algorithms")]//following::div[contains(@class, "total")]//following::div[1]//div[4]//div[@class="value"]'
}

# Fetch and print the data
for key, xpath in xpaths.items():
    text = get_element_text(xpath)
    if text:
        print(f"{key}: {text}")

# Optional sleep before quitting (can be removed)
time.sleep(10)

# Close the WebDriver
driver.quit()
