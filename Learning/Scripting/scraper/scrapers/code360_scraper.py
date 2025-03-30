from scrapers.base_scraper import BaseScraper

class NaukriProfileScraper(BaseScraper):
    def scrape_profile(self):
        self.open_profile(profile_url)

        try:
            # Function to get the text of an element based on its XPath
            def get_element_text(xpath):
                try:
                    element = WebDriverWait(self.driver, 10).until(
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

        except Exception as e:
            print("An unexpected error occurred:", str(e))

        self.close_browser()

    def close_browser(self):
        pass


# Example usage
driver_path = r"C:\WebDriver\chromedriver.exe"
profile_url = "https://www.naukri.com/code360/profile/Epic"
scraper = NaukriProfileScraper(driver_path, profile_url)
scraper.scrape_profile()