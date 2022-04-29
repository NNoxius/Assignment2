def get_team_players(cursor, team):
    query = f"SELECT nickname, age, nationality, rating FROM players, teams WHERE players.team_id = teams.team_id AND teams.name = '{team}';"
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
    query = f"SELECT players.name, nickname, age, nationality, rating, teams.name FROM players INNER JOIN teams ON players.team_id = teams.team_id WHERE nickname = '{player}';"
    cursor.execute(query)


def get_nationality(cursor, nationality):
    query = f"SELECT * FROM players_teams WHERE nationality = '{nationality}';"
    cursor.execute(query)


def get_age(cursor, age):
    query = f"SELECT * FROM players_teams WHERE age = '{age}';"
    cursor.execute(query)


def get_team_avg_rating(cursor):
    query = f"SELECT name, AVG(rating) FROM players_teams GROUP BY name;"
    cursor.execute(query)


def get_coaches(cursor):
    query = "SELECT nickname, age, nationality, teams.name FROM coaches, teams WHERE coaches.team_id = teams.team_id"
    cursor.execute(query)


def get_coach(cursor, coach):
    query = f"SELECT coaches.name, nickname, age, nationality, teams.name FROM coaches INNER JOIN teams ON coaches.team_id = teams.team_id WHERE nickname = '{coach}';"
    cursor.execute(query)