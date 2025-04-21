import requests
from bs4 import BeautifulSoup
import sys

def fetch_problem_names(url):
    problem_names = []
    try:
        print(f"Fetching URL: {url}...")
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        print("Successfully fetched HTML content.")

        soup = BeautifulSoup(response.text, 'html.parser')
        print("Parsing HTML...")

        # Use partial class match for Tailwind-style classes
        td_tags = soup.find_all('td', class_=lambda c: c and 'text-left' in c)

        print(f"Found {len(td_tags)} matching <td> tags.")

        for td in td_tags:
            div = td.find('div', class_='font-medium cursor-pointer text-gray-800 dark:text-zinc-200')
            if div:
                a_tag = div.find('a', href=True)
                if a_tag and a_tag.text.strip():
                    name = a_tag.text.strip()
                    href = a_tag['href']
                    problem_names.append((name, href))

        print(f"Successfully extracted {len(problem_names)} problem names.")
        return problem_names

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An error occurred during parsing: {e}", file=sys.stderr)
        return None

# --- Main Execution ---
if __name__ == "__main__":
    target_url = "https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/"
    extracted_problems = fetch_problem_names(target_url)

    if extracted_problems:
        print("\n--- Extracted Problem Names ---")
        for i, (name, link) in enumerate(extracted_problems):
            print(f"{i + 1}. {name} - {link}")
        print(f"\nTotal problems found: {len(extracted_problems)}")
    else:
        print("\nCould not extract problem names. Please check the URL and the script's selectors.", file=sys.stderr)
