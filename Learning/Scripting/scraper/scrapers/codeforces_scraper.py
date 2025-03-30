from scrapers.base_scraper import BaseScraper

class CodeforcesProfileScraper(BaseScraper):
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
                "Total Problem Solved": '//div[contains(text(),"4 problems")]',
                "Contest Rating": '//span[contains(text(),"newbie")]//following::span'
            }

            # Fetch and print the data
            for key, xpath in xpaths.items():
                text = get_element_text(xpath)
                if text:
                    print(f"{key}: {text}")

        except Exception as e:
            print("An unexpected error occurred:", str(e))

        self.close_browser()

# Example usage
driver_path = r"C:\WebDriver\chromedriver.exe"
profile_url = "https://codeforces.com/profile/mohitjais_312"
scraper = CodeforcesProfileScraper(driver_path, profile_url)
scraper.scrape_profile()