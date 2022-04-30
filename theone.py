from requests import get
from pprint import PrettyPrinter
# from datetime import datetime

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links

links = [title for title, link in get_links().items()]

def get_data(category):
    data = get_links()[category]
    returner = get(BASE_URL + data).json()
    return returner

def get_teams():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']
    teams = list(filter(lambda x: x['name'] != 'Team', teams))
    return teams

teams = get_teams()
team_id_name = dict(zip([int(team['teamId']) for team in get_teams()], [team['nickname'] for team in get_teams()]))

def get_ppg_ranking():
    teams.sort(key=lambda x: int(x['ppg']['rank']))
    print('The ranking of teams by points per game:' + '\n')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']
        print(f"{i+1}. {name} {nickname} - {ppg}")

def get_apg_ranking(): 
    teams.sort(key=lambda x: int(x['apg']['rank']))
    print('The ranking of teams by assists per game:' + '\n')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        apg = team['apg']['avg']
        print(f"{i+1}. {name} {nickname} - {apg}")

def get_bpg_ranking():
    teams.sort(key=lambda x: int(x['bpg']['rank']))
    print('The ranking of teams by blocks per game:' + '\n')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        bpg =  team['bpg']['avg']
        print(f"{i+1}. {name} {nickname} - {bpg}")

def get_drpg_ranking():
    teams.sort(key=lambda x: int(x['drpg']['rank']))
    print('The ranking of teams by defensive rebounds per game:' + '\n')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        drpg =  team['drpg']['avg']
        print(f"{i+1}. {name} {nickname} - {drpg}")

def get_fgp_ranking():
    teams.sort(key=lambda x: int(x['fgp']['rank']))
    print('The ranking of teams by field-goal percentage:' + '\n')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        fgp =  str(team['fgp']['avg'] + '%').replace('0.', '')
        print(f"{i+1}. {name} {nickname} - {fgp}")

def get_ftp_ranking():
    teams.sort(key=lambda x: int(x['ftp']['rank']))
    print('The ranking of teams by field-goal percentage:' + '\n')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ftp =  str(team['ftp']['avg'] + '%').replace('0.', '')
        print(f"{i+1}. {name} {nickname} - {ftp}")

def get_oppg_ranking():
    teams.sort(key=lambda x: int(x['oppg']['rank']))
    print('The ranking of teams by field-goal percentage:' + '\n')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        oppg =  team['oppg']['avg']
        print(f"{i+1}. {name} {nickname} - {oppg}")

def get_tpg_ranking():
    teams.sort(key=lambda x: int(x['tpg']['rank']))
    print('The ranking of teams by field-goal percentage:' + '\n')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        tpg = team['fgp']['avg']
        print(f"{i+1}. {name} {nickname} - {tpg}")

def get_orpg_ranking():
    teams.sort(key=lambda x: int(x['orpg']['rank']))
    print('The ranking of teams by efficiency:' + '\n')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        orpg =  team['orpg']['avg']
        print(f"{i+1}. {name} {nickname} - {orpg}")

def get_spg_ranking():
    teams.sort(key=lambda x: int(x['spg']['rank']))
    print('The ranking of teams by efficiency:' + '\n')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        spg =  team['spg']['avg']
        print(f"{i+1}. {name} {nickname} - {spg}")

def get_eff_ranking():
    teams.sort(key=lambda x: int(x['eff']['rank']))
    print('The ranking of teams by efficiency rating:' + '\n')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        eff =  team['eff']['avg']
        print(f"{i+1}. {name} {nickname} - {eff}")

def get_trpg_ranking():
    teams.sort(key=lambda x: int(x['trpg']['rank']))
    print('The ranking of teams by field-goal percentage:' + '\n')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        trpg =  team['trpg']['avg']
        print(f"{i+1}. {name} {nickname} - {trpg}")

def get_today_game():
    positions = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
    data = get_data(links[3])['games']
    returner = []
    for i in list(range(len(data))):
        arenaName = data[i]['arena']['name']
        cityName = data[i]['arena']['city']
        stateAbbr = data[i]['arena']['stateAbbr']
        hTeam = team_id_name[int(data[i]['hTeam']['teamId'])]
        vTeam = team_id_name[int(data[i]['vTeam']['teamId'])]
        
        if len(data) == 1:
            returner.append(f"Today's game faces {vTeam} and {hTeam}, being played at the {arenaName} arena, {cityName}, {stateAbbr}.")
        elif i == list(range(len(data)))[-1]:
            returner.append(f"And finally another game faces {vTeam} and {hTeam}, being played at the {arenaName} arena, {cityName}, {stateAbbr}.")
        else:
            returner.append(f"Today {positions[0]} game faces {vTeam} and {hTeam}, being played at the {arenaName} arena, {cityName}, {stateAbbr}.")
    
    return returner


def main():

    print("Welcome to the NBA data collector!")
    print("Rankings?        - Press 'R'")
    print("Today's games?   - Press 'G'")
    print("Want to quit?    - Press 'Q'")
    print()

    while True:
        command = input(">>> ").lower()

        if command == "q":
            break
       
        elif command == "r":
            print("If you want to check the ranking of teams by: ")
            print("By points per game - Enter 'ppg'")
            print("By assists per game - Enter 'apg'")
            print("By blocks per game - Enter 'bpg'")
            print("By steals per game - Enter 'spg'")
            print("By field goal percentage - Enter 'fgp'")
            print("By turnovers per game - Enter 'tpg'")
            print("By total rebounds per game - Enter 'trpg'")
            print("By efficienfy rating - Enter 'eff'")
            print("By offensive rebounds per game - Enter 'orpg'")
            print("By deffensive rebounds per game - Enter 'drpg'")
            print("By free throw percentage - Enter 'ftp'")
            print("By opponent points allowed per game - Enter 'oppg'")

            command2 = input (">>> ").lower()

            if command2 == 'ppg': printer.pprint(get_ppg_ranking())
            elif command2 == 'apg': printer.pprint(get_apg_ranking())
            elif command2 == 'bpg': printer.pprint(get_bpg_ranking())
            elif command2 == 'spg': printer.pprint(get_spg_ranking())
            elif command2 == 'fgp': printer.pprint(get_fgp_ranking())
            elif command2 == 'trpg': printer.pprint(get_trpg_ranking())
            elif command2 == 'eff': printer.pprint(get_eff_ranking())
            elif command2 == 'orpg': printer.pprint(get_orpg_ranking())
            elif command2 == 'drpg': printer.pprint(get_drpg_ranking())
            elif command2 == 'ftp': printer.pprint(get_ftp_ranking())
            elif command2 == 'tpg': printer.pprint(get_tpg_ranking())
            elif command2 == 'oppg': printer.pprint(get_oppg_ranking())
            else: print('Unrecognized command!')


        elif command == "g":
            for game in get_today_game():
                print(game + '\n')

        else: print('Unrecognized command!')


main()

# printer.pprint(list(enumerate(links)))
# print()
# printer.pprint(get_teams()[0])
# printer.pprint(get_links())
# print(get_data(links[]))

# printer.pprint(get_ppg_ranking())
# printer.pprint(get_apg_ranking())
# printer.pprint(get_fgp_ranking())
# printer.pprint(get_eff_ranking())



# printer.pprint(get_teams())



