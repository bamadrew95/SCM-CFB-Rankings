# Import required modules
import pandas as pd
import cfbd
import time

# Import files
import write_to_db

##########################################
year = 2009
##########################################


#  Configure API key for College Football Data API
cfbd_config = cfbd.Configuration()
cfbd_config.api_key[
    "Authorization"
] = "kf4KXdtp2JFvq+7wy4yipT75+3mcVzeTl56SvjdONO3cdEksOHxWuZdPf2fB92hl"
cfbd_config.api_key_prefix["Authorization"] = "Bearer"

teams_api = cfbd.TeamsApi(cfbd.ApiClient(cfbd_config))
games_api = cfbd.GamesApi(cfbd.ApiClient(cfbd_config))

# Build out DataFrame with basic team info
teams = teams_api.get_fbs_teams()

# teams_df = pd.DataFrame.from_records(
#     [
#         dict(
#             id=t.id,
#             team=t.school,
#             conference=t.conference,
#             division=t.division,
#             city=t.location["city"],
#             state=t.location["state"],
#         )
#         for t in teams
#     ]
# )

test_df = pd.DataFrame.from_dict({"team": ["Alabama"]})

game_info = {}
game_stats = {}
game_opp_stats = {}
team_sched = {}

# Gather weekly stats for each team
for t in test_df["team"]:
    week = 1
    regular_season_games = games_api.get_team_game_stats(
        year, team=t, season_type="regular"
    )

    for game in regular_season_games:
        # Build out game_stats dict
        if game.teams[0]["school"] == t:
            for s in game.teams[0]["stats"]:
                game_stats[s["category"]] = s["stat"]

        if game.teams[1]["school"] == t:
            for s in game.teams[1]["stats"]:
                game_stats[s["category"]] = s["stat"]

        # Build out game_stats dict
        if game.teams[0]["school"] != t:
            for s in game.teams[0]["stats"]:
                game_opp_stats[s["category"]] = s["stat"]

        if game.teams[1]["school"] != t:
            for s in game.teams[1]["stats"]:
                game_opp_stats[s["category"]] = s["stat"]

        # Build out game_info dict
        game_info["gameid"] = game.id

        if game.teams[0]["school"] == t:
            game_info["opponent"] = game.teams[1]["school"]
            game_info["homeAway"] = "home"
            game_info["pointsFor"] = game.teams[0]["points"]
            game_info["pointsAgainst"] = game.teams[1]["points"]

        if game.teams[1]["school"] == t:
            game_info["opponent"] = game.teams[0]["school"]
            game_info["homeAway"] = "away"
            game_info["pointsFor"] = game.teams[1]["points"]
            game_info["pointsAgainst"] = game.teams[0]["points"]

        game_info["stats"] = game_stats
        game_info["oppStats"] = game_opp_stats

        # Add to team_sched dict
        key = "week" + str(week)

        team_sched[key] = game_info

        week += 1

        ############################## REMEMBER TO ADD RESULTS LATER WHEN DATA IS CONVERTED SO SCORE CAN BE COMPARED

    time.sleep(0.5)

    # print(game_stats)
    # print(game_opp_stats)
    # print(game_info)
    print(team_sched)

# team_game_stats = games_api.get_team_game_stats(2009, team="Alabama", week=1)

# for g in team_game_stats:
#     print(g.teams[0]["stats"][0]["category"])
#     print(g.teams[0]["stats"][0]["category"])