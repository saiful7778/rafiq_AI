import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def firefox(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
    FireFoxDriverPath = r"database\webdriver\geckodriver.exe"
    firefox_service = Service(FireFoxDriverPath)
    firefox_option = Options()
    firefox_option.set_preference("general.useragent.override", user_agent)
    browser = webdriver.Firefox(service=firefox_service, options=firefox_option)
    browser.implicitly_wait(7)
    browser.get(url)