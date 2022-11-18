import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

def edge():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'
    EdgeDriverPath = r"database\webdriver\msedgedriver.exe"
    edge_service = Service(EdgeDriverPath)
    edge_option = Options()
    edge_option.add_argument(f'user-agent={user_agent}')
    browser = webdriver.Edge(service=edge_service, options=edge_option)