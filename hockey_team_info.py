"""
Description:
 Example of using a complex data structure to store related information

Usage:
 python hockey_team_info.py
"""
def main():
    # Create a complex data structure that holds information about a hockey team
    team_info = {
        'name': 'Maple Leafs',
        'city': 'Toronto',
        'players': [
            'marner',
            'tavares',
            'matthews'
        ],
        'games': [
            {
                'opponent': 'Canadiens',
                'goals for': 3,
                'goals against': 1
            },
            {
                'opponent': 'Red Wings',
                'goals for': 6,
                'goals against': 2
            }
        ]
    }

    # Print a team cheer
    print_cheer(team_info)

    # Add some more players
    print_roster(team_info)
    add_players_to_team(team_info, ['knies', 'samsonov', 'reilly'])
    print_roster(team_info)

    # Add some more games
    print_opponents(team_info)
    add_game(team_info, 'Lightning', 3, 2)
    add_game(team_info, 'Bruins', 12, 0)
    print_opponents(team_info)

def print_cheer(team):
    """Prints a cheer for the team

    Args:
        team (dict): Team information data structure
    """
    # TODO: Print a cheer for the team that contains the team name and city 
    print(f"Let's go {team['city']} {team['name']}!")

def print_roster(team):
    """Prints a dash list of all player names

    Args:
        team (dict): Team information data structure
    """
    # TODO: Print a heading
    print(f"\n{team['city']} {team['name']} team roster:")
    # TODO: Print a dash list of all player names
    for player_name in team['players']:
        print(f'- {player_name}')

def add_players_to_team(team, new_players):
    """Adds one or more players to the team

    Args:
        team (dict): Team information data structure
        new_players (list): Names of players to add
    """
    # TODO: Append new players to the list
    team['players'].extend(new_players)
    # TODO: Capitalize first letter of each players name
    for i,  player_name in enumerate(team['players']):
        team['players'][i] = player_name.capitalize()
    # TODO: Sort the player list alphabetically
    team['players'].sort()
    return

def print_opponents(team):
    """Prints list of opponents the team has played a game against.

    Args:
        team (dict): Team information data structure
    """
    # TODO: Print comma-separated list of opponent names
    #print(f"\nThe {team['city']} {team['name']} have played games against", end = ' ')
    #for i, game in enumerate(team['games']):
        #if i < len(team['games']) - 1:
            #print(game['opponent'], end = ', ')
        #else:
            #print(game['opponent'], end = '.')

    opponent_names = [game['opponent'] for game in team['games']]
    print(', '.join(opponent_names), end='.')

def add_game(team, opp, gf, ga):
    """Adds one game to the team information data structure

    Args:
        team (dict): Team information data structure
        opp (str): Name of opponent
        gf (int): Goals for
        ga (int): Goals against
    """
    new_game = {
        'opponent': 'Red Wings',
        'goals for': 6,
        'goals against': 2
    }
    team['games'].append(new_game)

if __name__ == '__main__':
    main()