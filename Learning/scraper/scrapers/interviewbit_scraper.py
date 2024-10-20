from scrapers.base_scraper import BaseScraper

class InterviewBitScraper(BaseScraper):
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
                "Problem Solved": '//span[contains(text(),"Total")]//following::span[1]',
                "Easy": '//span[contains(text(),"easy")]//following::span[1]',
                "Medium": '//span[contains(text(),"medium")]//following::span[1]',
                "Hard": '//span[contains(text(),"hard")]//following::span[1]',
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
profile_url = "https://www.interviewbit.com/profile/blackshadows/"
scraper = InterviewBitScraper(driver_path, profile_url)
scraper.scrape_profile()