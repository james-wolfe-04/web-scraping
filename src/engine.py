from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def init_driver():
    """Initialize and return the Selenium driver with Phase 3 configurations."""
    options = Options()
    # Phase 3 Requirement: User-Agent Mocking
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_experimental_option("detach", True)
    
    print("Step 1: Launching Browser (Engine)...")
    driver = webdriver.Chrome(options=options)
    return driver