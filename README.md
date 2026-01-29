# Web Scraper Project: Quotes to Scrape (JS)

## Overview
This project is a resilient data pipeline designed to extract quotes, authors, and tags from the "Quotes to Scrape" JavaScript sandbox. It utilizes a hybrid approach: **Selenium** handles browser automation and JavaScript rendering, while **BeautifulSoup** parses the HTML for efficient data extraction.

## Setup Instructions
1. **Environment:** Ensure Python 3.x is installed.
2. **Installation:** Install dependencies using the requirements file: pip install -r requirements.txt
3. **Execution:** Run the main orchestrator script: python main.py
4. **Output:** The clean dataset will be saved to data/processed/quotes_final.csv

## Ethical Compliance Audit
    Target: http://quotes.toscrape.com/js/
    Robots.txt Analysis:
    Endpoint: http://quotes.toscrape.com/robots.txt

    Result: 404 Not Found.

Conclusion: The server provides no robots.txt file, implying no specific restrictions on automated access. The scraper mimics a standard User-Agent and includes polite delays (1 second) between requests to minimize server load.

## Troubleshooting & Engineering Challenges
Challenge: 
    Dynamic Content Loading The target site renders quotes via JavaScript after the initial page load. A standard HTTP request (like requests.get) returns an empty HTML skeleton.

Solution: 
    Explicit Waits I implemented Selenium.WebDriverWait with expected_conditions. Instead of a hardcoded sleep timer, the script intelligently pauses execution until the specific HTML container (.quote) is present in the DOM. This ensures 100% data capture reliability without wasting time on slow connections.