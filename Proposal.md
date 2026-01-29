1. Robots.txt Audit I attempted to access the robots exclusion standard at http://quotes.toscrape.com/robots.txt. 
    Result: The server returned a 404 Not Found error. 
    Analysis: The absence of a robots.txt file indicates that the site administrator has not defined any specific crawling restrictions. 
    Ethical Conclusion: In the absence of restrictive directives (like Disallow), standard web etiquette implies that automated access is permitted. Therefore, we are authorized to proceed with scraping.

2. Project Proposal
Target Website: Quotes to Scrape (JavaScript Sandbox) URL: http://quotes.toscrape.com/js/

Data to Extract: I plan to extract the following data points for each quote:

    The Quote: The actual text content.
    The Author: The name of the person who said it.
    The Tags: Keywords associated with the quote (e.g., "inspirational", "life").

Why Selenium is Necessary: I chose the /js/ version of this website. This site uses JavaScript to generate the quotes after the page loads. If I used a basic tool like BeautifulSoup alone, it would only see a blank page. I must use Selenium to open a browser and let the JavaScript run so the quotes become visible for extraction.