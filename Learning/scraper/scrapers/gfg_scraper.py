from selenium.common import TimeoutException, NoSuchElementException

from scrapers.base_scraper import BaseScraper


class GeeksforGeeksScraper(BaseScraper):
    def scrape_profile(self):
        self.open_profile(profile_url)

        try:
            # Function to extract the text of elements based on their XPath
            def get_element_text(xpath):
                try:
                    element = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, xpath))
                    )
                    return element.text
                except TimeoutException:
                    return "TimeoutException: Element not found"
                except NoSuchElementException:
                    return "NoSuchElementException: Element not found"

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

        self.close_browser()

# Example usage
driver_path = r"C:\WebDriver\chromedriver.exe"
profile_url = "https://www.geeksforgeeks.org/user/mohitjaiswal1/"
scraper = GeeksforGeeksScraper(driver_path, profile_url)
scraper.scrape_profile()