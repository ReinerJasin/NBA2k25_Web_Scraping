from Model.player_model import PlayerModel
from Model.player_model import PlayerKey

import os
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
    result_df = pd.DataFrame()

    # create an empy dictionary with keys
    dict_keys = PlayerKey.dict_keys
    player_dict = dict.fromkeys(dict_keys)

    # loop for every player urls
    for player_url in player_urls:
        
        # Get player data from website
        driver.get(BASE_URL + player_url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        # Step 1 - Get Player Bio
        # player_dict = getPlayerBio(soup, player_dict)

        # Step 2 - Get Player Attributes
        player_dict = getPlayerAttributes(soup, player_dict)

        # print(player_dict)
        print("")

        current_player_df = pd.DataFrame([player_dict])
        result_df = pd.concat([result_df, current_player_df], ignore_index=True)

        # print(result_df)

        # print("Saving")
        result_df.to_csv(os.path.abspath(os.curdir) + '\output\current_nba_players_test.csv')


def getPlayerBio(soup, player_dict):

    # Initialize default value
    player_name = None
    player_nationality_1 = None
    player_nationality_2 = None
    player_team = None
    player_jersey = None
    player_position_1 = None
    player_position_2 = None
    player_archetype = None
    player_height_feet = None
    player_height_cm = None
    player_weight_lbs = None
    player_weight_kg = None
    player_wingspan_feet = None
    player_wingspan_cm = None
    player_season_salary = None
    player_years_in_the_nba = None
    player_birthdate = None
    player_hometown = None
    player_prior_to_nba = None

    # Name
    player_h1_tag = soup.find("h1")
    if player_h1_tag:
        player_name = player_h1_tag.text.strip() # Get text and remove leading space

    for p_tag in soup.find_all('p'):

        # Nationality 1 and Nationality 2
        if 'Nationality: ' in p_tag.text:
            nationalities_tag = p_tag
            player_nationalities_a_tag = nationalities_tag.find_all('a')
            if len(player_nationalities_a_tag) > 0:
                player_nationality_1 = player_nationalities_a_tag[0].text.strip()
            if len(player_nationalities_a_tag) > 1:
                player_nationality_2 = player_nationalities_a_tag[1].text.strip()
        
        # Team
        if 'Team: ' in p_tag.text:
            team_tag = p_tag
            player_team = team_tag.find('a').text

        # Jersey
        if 'Jersey: ' in p_tag.text:
            jersey_tag = p_tag
            player_jersey = jersey_tag.text.replace("Jersey: #", "")

        # Position 1 and Position 2
        if 'Position: ' in p_tag.text:
            positions_tag = p_tag
            player_positions_a_tag = positions_tag.find_all('a')
            if len(player_positions_a_tag) > 0:
                player_position_1 = player_positions_a_tag[0].text
            if len(player_positions_a_tag) > 1:
                player_position_2 = player_positions_a_tag[1].text

        # Archetype
        if 'Archetype: ' in p_tag.text:
            archetype_tag = p_tag
            player_archetype = archetype_tag.find("span").text
            
        # Height
        if 'Height: ' in p_tag.text:
            height_tag = p_tag
            player_height = height_tag.find("span").text.split(" ")
            player_height_feet = player_height[0]
            player_height_cm = player_height[1].replace("(", "").replace("cm)", "")
            
        # Weight
        if 'Weight: ' in p_tag.text:
            weight_tag = p_tag
            player_weight = weight_tag.find("span").text.split(" ")
            player_weight_lbs = player_weight[0].replace("lbs", "")
            player_weight_kg = player_weight[1].replace("(", "").replace("kg)", "")

        # Wingspan
        if 'Wingspan: ' in p_tag.text:
            wingspan_tag = p_tag
            player_wingspan = wingspan_tag.find("span").text.split(" ")
            player_wingspan_feet = player_wingspan[0]
            player_wingspan_cm = player_wingspan[1].replace("(", "").replace("cm)", "")

        # Season salary
        if 'Season Salary: ' in p_tag.text:
            season_salary_tag = p_tag
            player_season_salary = season_salary_tag.text.replace("Season Salary: ", "").replace("$", "").replace(",", "")
            
        # Year(s) in the NBA
        if 'Year(s) in the NBA: ' in p_tag.text:
            years_in_the_nba_tag = p_tag
            player_years_in_the_nba = years_in_the_nba_tag.text.replace(" Year(s) in the NBA: ", "")
            
        # Birthdate
        if 'Birthdate: ' in p_tag.text:
            birthdate_tag = p_tag
            player_birthdate = birthdate_tag.text.replace("Birthdate: ", "")
            
        # Hometown
        if 'Hometown: ' in p_tag.text:
            hometown_tag = p_tag
            player_hometown = hometown_tag.text.replace("Hometown: ", "")
            
        # Prior to NBA
        if ' Prior to  NBA:' in p_tag.text:
            prior_to_nba_tag = p_tag
            player_prior_to_nba = prior_to_nba_tag.text.replace("Prior to  NBA:", "").strip()

    # Compile player in an object model for DEBUG
    # print("adding player - name: ", player_name)
    # print("adding player - nationality 1: ", player_nationality_1)
    # print("adding player - nationality 2: ", player_nationality_2)
    # print("adding player - team: ", player_team)
    # print("adding player - jersey: ", player_jersey)
    # print("adding player - position 1: ", player_position_1)
    # print("adding player - position 2: ", player_position_2)
    # print("adding player - archetype: ", player_archetype)
    # print("adding player - height (feet): ", player_height_feet)
    # print("adding player - height (cm): ", player_height_cm)
    # print("adding player - weight (lbs): ", player_weight_lbs)
    # print("adding player - weight (kg): ", player_weight_kg)
    # print("adding player - wingspan (feet): ", player_wingspan_feet)
    # print("adding player - wingspan (cm): ", player_wingspan_cm)
    # print("adding player - season salary: ", player_season_salary)
    # print("adding player - year(s) in the NBA: ", player_years_in_the_nba)
    # print("adding player - birthdate: ", player_birthdate)
    # print("adding player - hometown: ", player_hometown)
    # print("adding player - prior to NBA: ", player_prior_to_nba)
    # print("")
    # print("")

    # Add to pandas dataframe
    player_dict["name"] = player_name
    player_dict["nationality_1"] = player_nationality_1
    player_dict["nationality_2"] = player_nationality_2
    player_dict["team"] = player_team
    player_dict["jersey"] = player_jersey
    player_dict["position_1"]= player_position_1
    player_dict["position_2"]= player_position_2
    player_dict["archetype"]= player_archetype
    player_dict["height_feet"]= player_height_feet
    player_dict["height_cm"]= player_height_cm
    player_dict["weight_lbs"]= player_weight_lbs
    player_dict["weight_kg"]= player_weight_kg
    player_dict["wingspan_feet"]= player_wingspan_feet
    player_dict["wingspan_cm"]= player_wingspan_cm
    player_dict["season_salary"]= player_season_salary
    player_dict["years_in_the_nba"]= player_years_in_the_nba
    player_dict["birthdate"]= player_birthdate
    player_dict["hometown"]= player_hometown
    player_dict["prior_to_nba"]= player_prior_to_nba

    return player_dict

def getPlayerAttributes(soup, player_dict):
    
    # print(soup)

    # Key value pair for attributes
    attribute_dict = {
        'group_outside_scoring': ' Outside Scoring',
        'close_shot': ' Close Shot '
        }

    # Attribute
    attribute_tag = soup.find("span", class_='attribute-box-player')
    if attribute_tag:
        player_overall = attribute_tag.text
        # print('overall : ', player_overall)

        player_dict["overall"] = player_overall

    for p_tag in soup.find_all(['h4', 'li'], class_=['card-title', 'mb-1']):
        # print(p_tag)
        # print("")

        for key, value in attribute_dict.items():
            if value in p_tag:
                # print(p_tag.find('span').text)

                player_dict[key] = p_tag.find('span').text
                # print("successfully adding: ", key)
                # print("value: ", player_dict[key])
                # print("")


    print(player_dict)

    return player_dict


# Test case 1
getPlayerData(["trae-young", "luka-doncic", "joel-embiid"])