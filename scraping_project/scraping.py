import requests
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

URL = "https://www.2kratings.com/"

driver = uc.Chrome()
driver.get(URL)

# page = requests.get(URL)

page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

print(soup)