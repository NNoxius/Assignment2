def get_team_players(cursor, team):
    query = f"SELECT nickname, age, nationality, hltv_rating FROM players, teams WHERE players.team_id = teams.team_id AND teams.name = '{team}';"
    cursor.execute(query)


def get_team_coach(cursor, team):
    query = f"SELECT nickname, age, nationality FROM coaches, teams WHERE coaches.team_id = teams.team_id AND teams.name = '{team}';"
    cursor.execute(query)


def get_team_color(cursor, team):
    query = f"SELECT color FROM teams WHERE name = '{team}';"
    cursor.execute(query)

    for c in cursor:
        for value in c:
            return "#" + value


def get_teams(cursor):
    query = "SELECT name from teams;"
    cursor.execute(query)


def get_players(cursor):
    query = "SELECT * FROM players_teams;"
    cursor.execute(query)


def get_player(cursor, player):
    query = f"SELECT players.name, nickname, age, nationality, hltv_rating, teams.name FROM players INNER JOIN teams ON players.team_id = teams.team_id WHERE nickname = '{player}';"
    cursor.execute(query)


def get_nationality(cursor, nationality):
    query = f"SELECT players.name, nickname, age, nationality, hltv_rating, teams.name FROM players INNER JOIN teams ON players.team_id = teams.team_id WHERE nationality = '{nationality}';"
    cursor.execute(query)
