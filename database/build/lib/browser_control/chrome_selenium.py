import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def chrome():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'
    driver_path = r"database\webdriver\chromedriver.exe"
    chrome_service = Service(driver_path)
    chrome_options = Options()
    chrome_options.add_argument(f'user-agent={user_agent}')
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)