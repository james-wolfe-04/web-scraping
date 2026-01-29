from bs4 import BeautifulSoup

def parse_html(page_source):
    """Parse the page source and return a list of quote dictionaries."""
    soup = BeautifulSoup(page_source, "html.parser")
    quotes_data = []
    
    quote_elements = soup.find_all("div", class_="quote")
    
    for quote in quote_elements:
        item = {
            "text": quote.find("span", class_="text").text,
            "author": quote.find("small", class_="author").text,
            "tags": [tag.text for tag in quote.find_all("a", class_="tag")]
        }
        quotes_data.append(item)
        
    return quotes_data