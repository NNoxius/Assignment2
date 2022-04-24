import mysql.connector
from mysql.connector import errorcode

def get_team_players(cursor, team):
    query = f"SELECT nickname, age, nationality, hltv_rating FROM players, teams WHERE players.team_id = teams.team_id AND teams.name = '{team}';"
    cursor.execute(query)

def get_team_coach(cursor, team):
    query = f"SELECT nickname, age, nationality FROM coaches, teams WHERE coaches.team_id = teams.team_id AND teams.name = '{team}'"

