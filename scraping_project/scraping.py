import requests
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

BASE_URL = "https://www.2kratings.com/"

options  = uc.ChromeOptions()
# options.headless = True
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

driver = uc.Chrome(options=options)
driver.get(BASE_URL + "current-teams/")

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
team_name_list = sorted(list(team_name_url))

for team_name_url in team_name_list:
    driver.get(BASE_URL + '/teams/' + team_name_url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    print(soup.title)