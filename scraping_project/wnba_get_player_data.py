# from Model.player_model import PlayerModel
from Model.wnba_player_model import PlayerKey

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

    # create an empty dictionary with keys
    dict_keys = PlayerKey.dict_keys
    # player_dict = dict.fromkeys(dict_keys)

    # loop for every player urls
    for player_url in player_urls:
        
        print("Accessing data for player: ", player_url)

        # Get player data from website
        driver.get(BASE_URL + player_url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        player_dict = dict.fromkeys(dict_keys)
    
        # Step 1 - Get Player Bio
        player_dict = getPlayerBio(soup, player_dict)

        # Step 2 - Get Player Attributes
        player_dict = getPlayerAttributes(soup, player_dict)

        # Step 2 - Get Player Badges
        player_dict = getPlayerBadges(soup, player_dict)

        # print(player_dict)
        # print("")

        current_player_df = pd.DataFrame([player_dict])
        result_df = pd.concat([result_df, current_player_df], ignore_index=True)

        result_df.to_csv(os.path.abspath(os.curdir) + '\output\current_wnba_players.csv')
        # # FOR DEBUG
        # player_dict = dict.fromkeys(dict_keys)
        # current_player_df = pd.DataFrame([player_dict])
        # result_df = pd.concat([result_df, current_player_df], ignore_index=True)

    # ALSO DEBUG
    # player_urls = ["trae-young", "alex-caruso", "luka-doncic", "alex-caruso", "joel-embiid", "alex-caruso", "stephen-curry", "alex-caruso", "giannis-antetokounmpo", "alex-caruso", "anthony-edwards", "alex-caruso"]

    # # print(result_df)
    # none_list = checkEmptyPlayerData(result_df)
    
    # print("HEYY  ", [player_urls[i] for i in none_list])
    # print("HEYY  2 ", map(player_urls.__getitem__, none_list))
    # missing_player_urls = [player_urls[i] for i in none_list]


    while True:

        none_list = checkEmptyPlayerData(result_df)
        missing_player_urls = [player_urls[i] for i in none_list]

        # print("")
        # print("Missing player index on the df : ", none_list)
        # print("Missing player url : ", missing_player_urls)
        # print("")

        # if checkEmptyPlayerData(result_df) == []:
        if none_list == []:
            print("================== ALERT  =======================")
            print("No more empty data, breaking the infinite loop")
            print("=================================================")
            print("")
            break
        else:
            print("================== ALERT  =======================")
            print("found empty data")
            print(missing_player_urls)
            print("=================================================")
            print("")
            
            # print("RESULT OF EMPTY CHECKING IS : ")
            # print(checkEmptyPlayerData(result_df))
            # print(none_list)

            # print("Missing player url : ", missing_player_urls)
            for i in range(len(missing_player_urls)):
                print(f"========== FIXING THE VALUE OF {missing_player_urls[i]} ===============")
                driver.get(BASE_URL + missing_player_urls[i])
                page_source = driver.page_source
                soup = BeautifulSoup(page_source, "html.parser")

                player_dict = dict.fromkeys(dict_keys)
    
                # Step 1 - Get Player Bio
                player_dict = getPlayerBio(soup, player_dict)
    
                # Step 2 - Get Player Attributes
                player_dict = getPlayerAttributes(soup, player_dict)
    
                # Step 2 - Get Player Badges
                player_dict = getPlayerBadges(soup, player_dict)
                # print("RESULT PLAYER DICT: ", player_dict)
                # print("RESULT REASULT DF [i]: ", result_df.iloc[none_list[i]])
                # print("")
                # print("RESULT RESULT DF 1: ", result_df)
                # print("")
                # print("RESULT RESULT DF 2: ", result_df.loc[none_list[i]])
                
                # current_player_df = pd.DataFrame([player_dict])
                result_df.loc[none_list[i]] = pd.Series(player_dict)
                # print("RESULT RESULT DF 1 1: ", result_df)
                print("RESULT RESULT DF 2 2: ", result_df.loc[none_list[i]])
                # result_df = pd.concat([result_df, current_player_df], ignore_index=True)

                result_df.to_csv(os.path.abspath(os.curdir) + '\output\current_wnba_players.csv')
                print("========== FIXING PROCESS DONE ===============")


        # Saving dataframe result as a csv file
    #     # print("Saving")
    # result_df.to_csv(os.path.abspath(os.curdir) + '\output\current_nba_players_debug.csv')


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
    # player_season_salary = None
    player_years_in_the_wnba = None
    player_birthdate = None
    player_hometown = None
    player_prior_to_wnba = None

    # Name
    player_h1_tag = soup.find("h1")
    if player_h1_tag:
        player_name = player_h1_tag.text.strip() # Get text and remove leading space

    for p_tag in soup.find_all('p'):

        # Nationality 1 and Nationality 2
        if 'Nationality: ' in p_tag.text:
            nationalities_tag = p_tag
            player_nationalities_a_tag = nationalities_tag.find_all('span')
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
        # if 'Season Salary: ' in p_tag.text:
        #     season_salary_tag = p_tag
        #     player_season_salary = season_salary_tag.text.replace("Season Salary: ", "").replace("$", "").replace(",", "")
            
        # Year(s) in the NBA
        if 'Year(s) in the WNBA: ' in p_tag.text:
            years_in_the_wnba_tag = p_tag
            player_years_in_the_wnba = years_in_the_wnba_tag.text.replace(" Year(s) in the WNBA: ", "")
            
        # Birthdate
        if 'Birthdate: ' in p_tag.text:
            birthdate_tag = p_tag
            player_birthdate = birthdate_tag.text.replace("Birthdate: ", "")
            
        # Hometown
        if 'Hometown: ' in p_tag.text:
            hometown_tag = p_tag
            player_hometown = hometown_tag.text.replace("Hometown: ", "")
            
        # Prior to NBA
        if ' Prior to  WNBA:' in p_tag.text:
            prior_to_wnba_tag = p_tag
            player_prior_to_wnba = prior_to_wnba_tag.text.replace("Prior to  WNBA:", "").strip()

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
    # player_dict["season_salary"]= player_season_salary
    player_dict["years_in_the_wnba"]= player_years_in_the_wnba
    player_dict["birthdate"]= player_birthdate
    player_dict["hometown"]= player_hometown
    player_dict["prior_to_wnba"]= player_prior_to_wnba

    return player_dict

def getPlayerAttributes(soup, player_dict):
    
    # print(soup)

    # Key value pair for attributes
    attribute_dict = {
        'group_outside_scoring': ' Outside Scoring',
        'close_shot': ' Close Shot ',
        'mid_range_shot': ' Mid-Range Shot ',
        'three_point_shot': ' Three-Point Shot ',
        'free_throw': ' Free Throw ',
        'shot_iq': ' Shot IQ ',
        'offensive_consistency': ' Offensive Consistency ',
        'group_athleticism': ' Athleticism',
        'speed': ' Speed ',
        'agility': ' Agility ',
        'strength': ' Strength ',
        'vertical': ' Vertical ',
        'stamina': ' Stamina ',
        'hustle': ' Hustle ',
        'overall_durability': ' Overall Durability ',
        'group_inside_scoring': ' Inside Scoring',
        'layup': ' Layup ',
        'standing_dunk': ' Standing Dunk ',
        'driving_dunk': ' Driving Dunk ',
        'post_hook': ' Post Hook ',
        'post_fade': ' Post Fade ',
        'post_control': ' Post Control ',
        'draw_foul': ' Draw Foul ',
        'hands': ' Hands ',
        'group_playmaking': ' Playmaking',
        'pass_accuracy': ' Pass Accuracy ',
        'ball_handle': ' Ball Handle ',
        'speed_with_ball': ' Speed with Ball ',
        'pass_iq': ' Pass IQ ',
        'pass_vision': ' Pass Vision ',
        'group_defense': ' Defense',
        'interior_defense': ' Interior Defense ',
        'perimeter_defense': ' Perimeter Defense ',
        'steal': ' Steal ',
        'block': ' Block ',
        'help_defense_iq': ' Help Defense IQ ',
        'pass_perception': ' Pass Perception ',
        'defensive_consistency': ' Defensive Consistency ',
        'group_rebounding': ' Rebounding',
        'offensive_rebound': ' Offensive Rebound ',
        'defensive_rebound': ' Defensive Rebound ',
        'intangibles': ' Intangibles ',
        'potential': ' Potential ',
        'total_attributes': ' Total Attributes',
        }

    # Attribute
    attribute_tag = soup.find("span", class_='attribute-box-player')
    
    player_dict["overall"] = None

    if attribute_tag:
        player_overall = attribute_tag.text
        # print('overall : ', player_overall)

        player_dict["overall"] = player_overall

    for p_tag in soup.find_all(['h4', 'li'], class_=['card-title', 'mb-1']):
        # print(p_tag)
        # print("")

        for key, value in attribute_dict.items():

            if value in p_tag:
                
                player_dict[key] = None

                # print(p_tag.find('span').text)

                player_dict[key] = p_tag.find('span').text.replace(",", "")
                # print("successfully adding: ", key)
                # print("value: ", player_dict[key])
                # print("")

    # print(player_dict)

    return player_dict

def getPlayerBadges(soup, player_dict):

    for p_tag in soup.find_all('div', class_='badge-card'):
        
        img_tag = p_tag.find('img')

        badge_name = img_tag.get('title').lower().replace(" ","_").replace("-", "_")
        badge_level = img_tag.get('data-src').replace("https://www.2kratings.com/wp-content/uploads/", "").replace("-badge.png","").replace("-", "_").replace(badge_name + "_", "")
        player_dict["badge_" + badge_name] = badge_level
        
        # print("attempting to add: badge_" + badge_name)
        # print("value: ", badge_level)
        # print("")

    # print(player_dict)

    return player_dict

def checkEmptyPlayerData(result_df):
    print("================== ALERT  =======================")
    print("checking empty player data")
    print("=================================================")
    print("")
    none_list = result_df[result_df['name'].isnull()].index.tolist()
    # print("Index with None data: ", none_list)
    
    return none_list

# Test case 1
# getPlayerData(["trae-young", "luka-doncic", "joel-embiid", "stephen-curry", "giannis-antetokounmpo", "anthony-edwards"])