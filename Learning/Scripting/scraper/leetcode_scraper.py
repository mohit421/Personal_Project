from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome WebDriver
service = Service(executable_path=r"C:\WebDriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Set implicit wait
driver.implicitly_wait(10)

# Open LeetCode profile
driver.get("https://leetcode.com/u/Epicureanism/")



xpaths1 = [
    '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[1]/div[3]/span[text()="Show more"]',
    '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[2]/div[3]/span[text()="Show more"]',
    '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[3]/div[3]/span[text()="Show more"]'
]

# Iterate over the list and click each "Show more" button
for xpath in xpaths1:
    element = driver.find_element(By.XPATH, xpath)
    element.click()

try:
    # Define a function to extract the text of elements based on their XPath
    def get_element_text(xpath):
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return element.text


    # Retrieve various statistics
    problem_solved = get_element_text(
        '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[3]/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/span[1]')
    easy = get_element_text('//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div[2]')
    medium = get_element_text('//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]')
    hard = get_element_text('//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[3]/div[1]/div/div/div[2]/div[3]/div[2]')

    # Retrieve tags statistics
    tags_xpaths = {
        "DynamicProgramming": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[1]/span',
        "DivideAndConquer": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[2]/span',
        "ShortestPath": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[3]/span',
        "GameTheory": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[4]/span',
        "Backtracking": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[5]/span',
        "UnionFind": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[6]/span',
        "SegmentTree": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[7]/span',
        "MonotonicStack": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[8]/span',
        "HashTable": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[1]/span',
        "Math": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[2]/span',
        "Tree": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[3]/span',
        "BinaryTree": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[4]/span',
        "Database": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[5]/span',
        "DFS": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[6]/span',
        "Greedy": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[7]/span',
        "BinarySearch": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[8]/span',
        "Array": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[1]/span',
        "String": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[2]/span',
        "Sorting": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[2]/span',
        "TwoPointer": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[4]/span',
        "Simulation": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[5]/span',
        "Matrix": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[6]/span',
        "Stack": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[7]/span',
        "LinkedList": '//*[@id="__next"]/div[1]/div[4]/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[8]/span',
    }

    # Print retrieved statistics
    print("Problem Solved:", problem_solved)
    print("Easy:", easy)
    print("Medium:", medium)
    print("Hard:", hard)

    # Loop through the tags to print their counts
    for tag, xpath in tags_xpaths.items():
        print(f"{tag}: {get_element_text(xpath)}")

except TimeoutException as e:
    print("An element could not be found:", str(e))

finally:
    time.sleep(10)
    driver.quit()
