from scrapers.leetcode_scraper import LeetCodeScraper
from scrapers.gfg_scraper import GeeksforGeeksScraper
from scrapers.codeforces_scraper import CodeforcesProfileScraper  # Import Codeforces scraper
from scrapers.codechef_scraper import CodeChefProfileScraper  # Import Codeforces scraper
from scrapers.interviewbit_scraper import InterviewBitScraper  # Import Codeforces scraper
from scrapers.code360_scraper import NaukriProfileScraper  # Import Codeforces scraper
# from scrapers.hackerrank_scraper import hackerrankProfileScraper  # Import Codeforces scraper


# Add imports for other scrapers

def main():
    # global scraper
    profile_url = input("Enter profile URL: ")
    driver_path = r"C:\WebDriver\chromedriver.exe"  # Ensure this path is correct

    if "leetcode.com" in profile_url:
        scraper = LeetCodeScraper(driver_path, profile_url)
    elif "geeksforgeeks.org" in profile_url:
        scraper = GeeksforGeeksScraper(driver_path, profile_url)
    elif "codeforces.com" in profile_url:
        scraper = CodeforcesProfileScraper(driver_path, profile_url)
    elif "codechef.com" in profile_url:
        scraper = CodeChefProfileScraper(driver_path, profile_url)
    # elif "hackerrank.com" in profile_url:
    #     scraper = CodeforcesProfileScraper(driver_path, profile_url)
    elif "interviewbit.com" in profile_url:
        scraper = InterviewBitScraper(driver_path, profile_url)
    elif "Naukri.com" in profile_url:
        scraper = NaukriProfileScraper(driver_path, profile_url)

    # Add more conditions for other platforms

    scraper.scrape_profile()


if __name__ == "__main__":
    main()
