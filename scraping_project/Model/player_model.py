class PlayerModel:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PlayerKey:
    dict_keys = [
        # General Bio
        'name',
        'nationality_1',
        'nationality_2',
        'team',
        'jersey',
        'position_1',
        'position_2',
        'archetype',
        'height_feet',
        'height_cm',
        'weight_lbs',
        'weight_kg',
        'wingspan_feet',
        'wingspan_cm',
        'season_salary',
        'years_in_the_nba',
        'birthdate',
        'hometown',
        'prior_to_nba',

        # Attributes
        'overall',

        'group_outside_scoring',
        'close_shot',
        'mid_range_shot',
        'three_point_shot',
        'free_throw',
        'shot_iq',
        'offensive_consistency',

        'group_athleticism',
        'speed',
        'agility',
        'strength',
        'vertical',
        'stamina',
        'overall_durability',

        'group_inside_scoring',
        'layup',
        'standing_dunk',
        'driving_dunk',
        'post_hook',
        'post_fade',
        'post_control',
        'draw_foul',
        'hands',
        
        'group_playmaking',
        'pass_accuracy',
        'ball_handle',
        'speed_with_ball',
        'pass_iq',
        'pass_vision',
        
        'group_defense',
        'interior_defense',
        'perimeter_defense',
        'steal',
        'block',
        'help_defense_iq',
        'pass_perception',
        'defensive_consistency',
        
        'group_rebounding',
        'offensive_rebound',
        'defensive_rebound',
        
        'intangibles',
        'potential',
        'total_attributes',

        # Badges
        # 'badge_outside_scoring_deadeye',
        # 'badge_outside_scoring_limitless_range',
        # 'badge_outside_scoring_mini_marksman',
        # 'badge_outside_scoring_set_shot_specialist',
        # 'badge_outside_scoring_shifty_shooter',

        # 'badge_inside_scoring_aerial_wizard',
        # 'badge_inside_scoring_float_game',
        # 'badge_inside_scoring_hook_specialist',
        # 'badge_inside_scoring_layup_mixmaster',
        # 'badge_inside_scoring_paint_prodigy',
        # 'badge_inside_scoring_physical_finisher',
        # 'badge_inside_scoring_post_fade_phenom',
        # 'badge_inside_scoring_post_powerhouse',
        # 'badge_inside_scoring_post_up_poet',
        # 'badge_inside_scoring_posterizer',
        # 'badge_inside_scoring_rise_up',

        # 'badge_playmaking_ankle_assassin',
        # 'badge_playmaking_bail_out',
        # 'badge_playmaking_break_starter',
        # 'badge_playmaking_dimer',
        # 'badge_playmaking_handles_for_days',
        # 'badge_playmaking_lightning_launch',
        # 'badge_playmaking_strong_handle',
        # 'badge_playmaking_unpluckable',
        # 'badge_playmaking_versatile_visionary',
        
        # 'badge_defense_challenger',
        # 'badge_defense_glove',
        # 'badge_defense_high_flying_denier',
        # 'badge_defense_immovable_enforcer',
        # 'badge_defense_interceptor',
        # 'badge_defense_off_ball_pest',
        # 'badge_defense_on_ball_menace',
        # 'badge_defense_paint_patroller',
        # 'badge_defense_pick_dodger',
        # 'badge_defense_post_lockdown',
        
        # 'badge_rebounding_boxout_beast',
        # 'badge_rebounding_rebound_chaser',
        
        # 'badge_general_offense_brick_wall',
        # 'badge_general_offense_slippery_off_ball',
        
        # 'badge_all_around_pogo_stick',
        
        # Badges (with no grouping)
        # 'badge_deadeye',
        # 'badge_limitless_range',
        # 'badge_mini_marksman',
        # 'badge_set_shot_specialist',
        # 'badge_shifty_shooter',

        # 'badge_aerial_wizard',
        # 'badge_float_game',
        # 'badge_hook_specialist',
        # 'badge_layup_mixmaster',
        # 'badge_paint_prodigy',
        # 'badge_physical_finisher',
        # 'badge_post_fade_phenom',
        # 'badge_post_powerhouse',
        # 'badge_post_up_poet',
        # 'badge_posterizer',
        # 'badge_rise_up',

        # 'badge_ankle_assassin',
        # 'badge_bail_out',
        # 'badge_break_starter',
        # 'badge_dimer',
        # 'badge_handles_for_days',
        # 'badge_lightning_launch',
        # 'badge_strong_handle',
        # 'badge_unpluckable',
        # 'badge_versatile_visionary',
        
        # 'badge_challenger',
        # 'badge_glove',
        # 'badge_high_flying_denier',
        # 'badge_immovable_enforcer',
        # 'badge_interceptor',
        # 'badge_off_ball_pest',
        # 'badge_on_ball_menace',
        # 'badge_paint_patroller',
        # 'badge_pick_dodger',
        # 'badge_post_lockdown',
        
        # 'badge_boxout_beast',
        # 'badge_rebound_chaser',
        
        # 'badge_brick_wall',
        # 'badge_slippery_off_ball',
        
        # 'badge_pogo_stick',

        # Hot Zones
        # 'hot_zones_paint',
        # 'hot_zones_close_range_left',
        # 'hot_zones_close_range_center',
        # 'hot_zones_close_range_right',
        # 'hot_zones_mid_range_left',
        # 'hot_zones_mid_range_left_center',
        # 'hot_zones_mid_range_center',
        # 'hot_zones_mid_range_right_center',
        # 'hot_zones_mid_range_right',
        # 'hot_zones_3pt_left',
        # 'hot_zones_3pt_left_center',
        # 'hot_zones_3pt_center',
        # 'hot_zones_3pt_right_center',
        # 'hot_zones_3pt_right',
        ]