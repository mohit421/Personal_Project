from scrapers.base_scraper import BaseScraper

# class LeetCodeScraper(BaseScraper):
#     def scrape_profile(self):
#         self.open_profile()
#         # Implement scraping logic for LeetCode
#         # e.g., find elements, extract data, etc.
#         username = self.driver.find_element_by_xpath("//h1[@class='username']").text
#         problems_solved = self.driver.find_element_by_xpath("//span[@class='problems-solved']").text
#         print(f"Username: {username}, Problems Solved: {problems_solved}")
#         self.close_browser()


class LeetCodeScraper(BaseScraper):
    def scrape_profile(self):
        self.open_profile(profile_url)

        # Click "Show more" buttons to load additional data
        xpaths_show_more = [
            '//span[contains(text(),"Show more")]',
            '//span[contains(text(),"Show more")]',
            '//span[contains(text(),"Show more")]',
        ]

        for xpath in xpaths_show_more:
            try:
                element = self.driver.find_element(By.XPATH, xpath)
                element.click()
            except Exception as e:
                print(f"Error clicking 'Show more' button: {str(e)}")

        try:
            # Function to extract the text of elements based on their XPath
            def get_element_text(xpath):
                element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, xpath))
                )
                return element.text

            # Retrieve various statistics
            problem_solved = get_element_text(
                '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[3]/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/span[1]'
            )
            easy = get_element_text(
                '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div[2]'
            )
            medium = get_element_text(
                '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]'
            )
            hard = get_element_text(
                '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[3]/div[1]/div/div/div[2]/div[3]/div[2]'
            )

            # Retrieve tags statistics
            tags_xpaths = {
                "Easy": '//div[contains(text(),"Easy")]//following::div[1]',
                "Medium": '//div[contains(text(),"Med.")]//following::div[1]',
                "Hard": '//div[contains(text(),"Hard")]//following::div[1]',
                "Dynamic Programming": '//a[@href="/tag/dynamic-programming/"]//following::span[1]',
                "Divide and Conquer": '//a[@href="/tag/divide-and-conquer/"]//following::span[1]',
                "Shortest Path": '//a[@href="/tag/shortest-path/"]//following::span[1]',
                "Game Theory": '//a[@href="/tag/game-theory/"]//following::span[1]',
                "Backtracking": '//a[@href="/tag/backtracking/"]//following::span[1]',
                "Union Find": '//a[@href="/tag/union-find/"]//following::span[1]',
                "Segment Tree": '//a[@href="/tag/segment-tree/"]//following::span[1]',
                "Monotonic Stack": '//a[@href="/tag/monotonic-stack/"]//following::span[1]',
                "Hash Table": '//a[@href="/tag/hash-table/"]//following::span[1]',
                "Math": '//a[@href="/tag/math/"]//following::span[1]',
                "Tree": '//a[@href="/tag/tree/"]//following::span[1]',
                "Binary Tree": '//a[@href="/tag/binary-tree/"]//following::span[1]',
                "Database": '//a[@href="/tag/database/"]//following::span[1]',
                "DFS": '//a[@href="/tag/depth-first-search/"]//following::span[1]',
                "Greedy": '//a[@href="/tag/greedy/"]//following::span[1]',
                "Binary Search": '//a[@href="/tag/binary-search/"]//following::span[1]',
                "Array": '//a[@href="/tag/array/"]//following::span[1]',
                "String": '//a[@href="/tag/string/"]//following::span[1]',
                "Sorting": '//a[@href="/tag/sorting/"]//following::span[1]',
                "Two Pointer": '//a[@href="/tag/two-pointers/"]//following::span[1]',
                "Simulation": '//a[@href="/tag/simulation/"]//following::span[1]',
                "Matrix": '//a[@href="/tag/matrix/"]//following::span[1]',
                "Stack": '//a[@href="/tag/stack/"]//following::span[1]',
                "Linked List": '//a[@href="/tag/linked-list/"]//following::span[1]'
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

        self.close_browser()

driver_path = r"C:\WebDriver\chromedriver.exe"
profile_url = "https://leetcode.com/u/Epicureanism/"
scraper = LeetCodeScraper(driver_path, profile_url)
scraper.scrape_profile()