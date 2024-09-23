import requests
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

URL = "https://www.2kratings.com/current-teams"

driver = uc.Chrome()
driver.get(URL)

# page = requests.get(URL)

page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

# Create empty set to store all nba team names
team_name_url = set()

# Find all table row
current_teams = soup.find_all("tr")

# Extract the img tag and get the title of each team name
for current_team in current_teams:
    img_tag = current_team.find("img", class_="mr-2")
    if img_tag:
        team_name = img_tag['title']
        team_name_url.add(team_name.lower().replace(" ", "-"))

# Print list of nba team names
print(sorted(list(team_name_url)))
