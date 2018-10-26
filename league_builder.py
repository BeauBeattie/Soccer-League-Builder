"""
Python Web Development Techdegree
Project 2 - Soccer League
--------------------------------
A program that imports a CSV fileand generates teams based on the 
experience of players.
--------------------------------
Beau Beattie
"""

import csv


def import_csv(filename):
    # Import CSV file and return list of players
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        players = list(reader)
        return players


def sort_players(players, experienced, inexperienced):
    #  Sort players into experienced and inexperienced
    for player in players:
        if player['Soccer Experience'] == "YES":
            experienced.append(player)
        else:
            inexperienced.append(player)
    return experienced, inexperienced


def assign_players(team, sharks, dragons, raptors):
    #  Loop through players and assign to each team one by one
    count = 1
    for player in team:
        if count == 1:
            sharks.append(player)
            count += 1
        elif count == 2:
            dragons.append(player)
            count += 1
        elif count == 3:
            raptors.append(player)
            count = 1
    return sharks, dragons, raptors


def output_teams_to_text(team, team_name):
    #  Output a list of teams to a .txt file with relevant information
    with open("teams.txt", "a") as teamfile:
        teamfile.write(team_name + "\n")
        for player in team:
            teamfile.write("{}, {}, {} \n".format(player['Name'],
                                                  player['Soccer Experience'],
                                                  player['Guardian Name(s)']))
        teamfile.write("\n")


def write_guardian_letters(team, team_name, practice_date):
    #  Write a .txt letter for the guardian of each player with relevant info
    for player in team:
        player_file_name = "_".join(player["Name"].lower().split())
        with open(player_file_name, "a") as player_file:
            player_file.write(
                "Dear " + player["Guardian Name(s)"] + ", \n \n" +
                "Welcome to a new season of Soccer!  Here are the details "
                "for the new season:\n"
                "Name: " + player["Name"] + "\n"
                "Team: " + team_name + "\n"
                "First practice session: " + practice_date + "\n \n"

                "Many thanks,\n"
                "The Soccer League"
            )


if __name__ == "__main__":
    players = import_csv("soccer_players.csv")

    #  Define variables
    experienced = []
    inexperienced = []

    sort_players(players, experienced, inexperienced)

    sharks = []
    dragons = []
    raptors = []

    assign_players(experienced, sharks, dragons, raptors)
    assign_players(inexperienced, sharks, dragons, raptors)

    output_teams_to_text(sharks, "SHARKS")
    output_teams_to_text(dragons, "DRGONS")
    output_teams_to_text(raptors, "RAPTORS")

    write_guardian_letters(sharks, "Sharks", "November 1st, 6pm")
    write_guardian_letters(dragons, "Dragons", "November 2nd, 6pm")
    write_guardian_letters(raptors, "Raptors", "November 5th, 7pm")
