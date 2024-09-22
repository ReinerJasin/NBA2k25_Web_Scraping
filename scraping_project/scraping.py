import requests
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

URL = "https://www.2kratings.com/current-teams"

driver = uc.Chrome()
driver.get(URL)

# page = requests.get(URL)

page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

# Get current teams and put in an array
current_teams = soup.find_all("tr")

for current_team in current_teams:
    team_name = current_team.find("img", class_="mr-2")
    print("=====DEBUG START=====")
    print(type(team_name))
    print("=====DEBUG END=====")
    print(type(team_name))
    # print(current_team, end="\n"*2)