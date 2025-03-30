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
driver.get("https://www.codechef.com/users/mohitjais312")

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
    "Problem Solved": '//h3[contains(text(),"Total Problems Solved")]',
    "CurrentRating":'//div[@class="rating-number"]',
    "Highest Rating": '//small[contains(text(),"Highest Rating")]',
    "Global Rank": '//div[@class="rating-star"]//span',
    "Country Rank": '//div[@class="rating-ranks"]//li[2]//strong',
    "Div": '//div[contains(text(),"Div")]',
    # "Easy": '',
    # "Medium": '',
    # "Hard": '',

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
