import requests
from bs4 import BeautifulSoup
import csv
import time

class WebScraper:
    def __init__(self, base_url):
        # Initialize with a base URL and headers to mimic a real browser
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def get_page(self, url):
        """Download a webpage safely"""
        try:
            # Add a delay to be respectful to the server
            time.sleep(1)
            
            # Make the request
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad status codes
            
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Error downloading page: {e}")
            return None
    
    def find_element_text(self, element, selector, default=""):
        """Safely extract text from an element"""
        found = element.select_one(selector)
        return found.text.strip() if found else default
    
    def scrape_quotes(self, num_pages=3):
        """Scrape multiple pages of quotes"""
        all_quotes = []
        
        for page in range(1, num_pages + 1):
            print(f"Scraping page {page}...")
            
            # Construct the URL for each page
            url = f"{self.base_url}/page/{page}/"
            soup = self.get_page(url)
            
            if not soup:
                continue
            
            # Find all quote containers
            quote_elements = soup.select('.quote')
            
            for quote in quote_elements:
                quote_data = {
                    'text': self.find_element_text(quote, '.text'),
                    'author': self.find_element_text(quote, '.author'),
                    'tags': [tag.text for tag in quote.select('.tags .tag')]
                }
                all_quotes.append(quote_data)
        
        return all_quotes
    
    def save_to_csv(self, data, filename):
        """Save the scraped data to a CSV file"""
        if not data:
            print("No data to save!")
            return
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"Successfully saved data to {filename}")
        except Exception as e:
            print(f"Error saving to CSV: {e}")

def main():
    # Create a scraper instance
    scraper = WebScraper('http://quotes.toscrape.com')
    
    # Scrape quotes from multiple pages
    quotes = scraper.scrape_quotes(num_pages=3)
    
    # Save the results
    scraper.save_to_csv(quotes, 'quotes.csv')
    
    # Print some results
    print("\nSample of scraped quotes:")
    for quote in quotes[:3]:
        print(f"\nQuote: {quote['text']}")
        print(f"Author: {quote['author']}")
        print(f"Tags: {', '.join(quote['tags'])}")

if __name__ == "__main__":
    main()