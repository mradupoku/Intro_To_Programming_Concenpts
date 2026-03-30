class Player:
    def __init__(self, player_name, player_position):
        self.player_name = player_name
        self.player_position = player_position

    def __str__(self):
        return f"{self.player_name} ({self.player_position})"

class NFLTeam:
    def __init__(self, team_name, players_list):
        self.team_name = team_name
        self.players_list = players_list

    def display_team(self):
        print(f"Team: {self.team_name}")
        print("-" * 20)
        for player in self.players_list:
            print(player)

#Create Player objects
p1 = Player("Joe Montana", "QB")
p2 = Player("Barry Sanders", "RB")
p3 = Player("Jerry Rice", "WR")
p4 = Player("Graham Gano", "K")

#Add players to a list
all_players = [p1, p2, p3, p4]

#Create Team with team name and the list of players
my_team = NFLTeam("All-Stars", all_players)

#Output the results
my_team.display_team()
