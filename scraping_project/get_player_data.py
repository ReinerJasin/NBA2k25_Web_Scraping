from Model.player_model import PlayerModel
from Model.player_model import PlayerKey

import pandas as pd
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

BASE_URL = "https://www.2kratings.com/"

options  = uc.ChromeOptions()
# options.headless = True
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

driver = uc.Chrome(options=options)

# receive list for loop
def getPlayerData(player_urls):

    # Create empty pandas dataframe
    df = pd.DataFrame()

    # create an empy dictionary with keys
    dict_keys = PlayerKey.dict_keys
    player_dict = dict.fromkeys(dict_keys)

    # # loop for every player urls
    for player_url in player_urls:
        
        # Get player data from website
        driver.get(BASE_URL + player_url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        # Initialize default value
        player_name = None
        player_nationality_1 = None
        player_nationality_2 = None
        player_team = None
        player_position_1 = None
        player_position_2 = None

        # Name
        player_h1_tag = soup.find("h1")
        if player_h1_tag:
            player_name = player_h1_tag.text[1:] # Get text and remove leading space


        for p_tag in soup.find_all('p'):

            # Nationality 1 and Nationality 2
            if 'Nationality: ' in p_tag.text:
                nationalities_tag = p_tag
                player_nationalities_a_tag = nationalities_tag.find_all('a')
                if len(player_nationalities_a_tag) > 0:
                    player_nationality_1 = player_nationalities_a_tag[0].text[1:]
                if len(player_nationalities_a_tag) > 1:
                    player_nationality_2 = player_nationalities_a_tag[1].text[1:]
            
            # Team
            if 'Team: ' in p_tag.text:
                team_tag = p_tag
                player_team = team_tag.find('a').text
                # print("found team: ", team_tag.find('a').text.strip())

            # Position 1 and Position 2
            if 'Position: ' in p_tag.text:
                positions_tag = p_tag
                player_positions_a_tag = positions_tag.find_all('a')
                if len(player_positions_a_tag) > 0:
                    player_position_1 = player_positions_a_tag[0].text
                if len(player_positions_a_tag) > 1:
                    player_position_2 = player_positions_a_tag[1].text

        # Compile player in an object model
        print("adding player - name: ", player_name)
        print("adding player - nationality 1: ", player_nationality_1)
        print("adding player - nationality 2: ", player_nationality_2)
        print("adding player - team: ", player_team)
        print("adding player - position 1: ", player_position_1)
        print("adding player - position 2: ", player_position_2)
        print("")
        print("")
        # print("adding player years in the NBA: ", 10)

        # Add to pandas dataframe
        player_dict["name"] = player_name
        player_dict["years_in_the_nba"] = 23
        player_dict[""]= 23

        # print(player_dict)

getPlayerData(["trae-young", "jayson-tatum", "joel-embiid"])