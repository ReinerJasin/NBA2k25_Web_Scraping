from all_nba_get_player_data import getPlayerData

import requests
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

BASE_URL = "https://www.2kratings.com/"

options  = uc.ChromeOptions()
# options.headless = True
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

driver = uc.Chrome(options=options)
driver.get(BASE_URL + "all-time-teams/")

# page = requests.get(URL)

page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

# Create empty set to store all nba team names
team_name_url = set()
player_name_url = set()

# Find all table row
current_teams = soup.find_all("tr")

# Extract the img tag and get the title of each team name
for current_team in current_teams:
    # img_tag = current_team.find("img", class_="mr-2")
    team_a_tag = current_team.find("a", href=True)
    if team_a_tag:
        team_name = team_a_tag.get('href')
        team_name_url.add(team_name.replace("https://www.2kratings.com/teams/", ""))
        # print(team_a_tag)

# Print list of nba team names
team_name_list = sorted(list(team_name_url))

# Print all team_name_list that will be used as a url endpoint
print(team_name_list)

for team_name_url in team_name_list:
# for team_name_url in ('atlanta-hawks', 'boston-celtics'):
    driver.get(BASE_URL + '/all-nba-teams/' + team_name_url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    
    current_players = soup.find("tbody")
    # print(current_players)
    for current_player in current_players:
        player_a_tag = current_player.find("a", href=True)
        if player_a_tag:
            player_name = player_a_tag.get('href')
            player_name_url.add(player_name.replace("https://www.2kratings.com/", ""))
            print(player_name)

player_name_list = sorted(list(player_name_url))

# Print all player_name_url that will be used as a url endpoint
print(player_name_list)

getPlayerData(player_name_list)