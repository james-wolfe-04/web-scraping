from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Import our custom modules (Phase 4 Requirement)
from src.engine import init_driver
from src.parser import parse_html
from src.utils import save_to_csv

def main():
    # 1. Setup
    driver = init_driver()
    url = "http://quotes.toscrape.com/js/"
    driver.get(url)
    
    all_quotes = []
    page_number = 1
    
    # 2. The Logic Loop (Phase 3)
    while True:
        print(f"--- Scraping Page {page_number} ---")
        
        try:
            # Phase 3: Explicit Wait
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "quote"))
            )
            
            # Phase 4: Use the parser module
            new_data = parse_html(driver.page_source)
            all_quotes.extend(new_data)
            print(f"Collected {len(new_data)} quotes from this page.")
            
            # Navigation Logic
            next_button = driver.find_element(By.CSS_SELECTOR, "li.next > a")
            next_button.click()
            page_number += 1
            
            # Small pause to be polite
            time.sleep(1)
            
        except (TimeoutException, NoSuchElementException):
            print("No more pages found. Stopping.")
            break
            
    # 3. Save Data (Phase 4)
    save_to_csv(all_quotes)
    
    # Cleanup
    driver.quit()

if __name__ == "__main__":
    main()