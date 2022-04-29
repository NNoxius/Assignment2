from calendar import c
import mysql.connector
from mysql.connector import errorcode

DB_NAME = "CSGO"

def create_database(cursor, DB_NAME):
    try:
        cursor.execute(f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
    except mysql.connector.Error:
        print(f"Could not create database {DB_NAME}")


def create_table_players(cursor):
    create_players = '''CREATE TABLE players (
        player_id int NOT NULL AUTO_INCREMENT,
        name nvarchar(100) NOT NULL,
        nickname nvarchar(100) NOT NULL,
        age int NOT NULL,
        nationality nvarchar(100) NOT NULL,
        rating float(3,2),
        team_id int,
        PRIMARY KEY (player_id)
        )'''

    try:
        print("Created table players")
        cursor.execute(create_players)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table players already exists")
        else:
            print(err.msg)


def create_table_coaches(cursor):
    create_coaches = '''CREATE TABLE coaches (
        coach_id int NOT NULL AUTO_INCREMENT,
        name nvarchar(100) NOT NULL,
        nickname nvarchar(100) NOT NULL,
        age int NOT NULL,
        nationality nvarchar(100) NOT NULL,
        team_id int,
        PRIMARY KEY (coach_id)
        )'''

    try:
        print("Created table coaches")
        cursor.execute(create_coaches)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table coaches already exists")
        else:
            print(err.msg)


def create_table_teams(cursor):
    create_teams = '''CREATE TABLE teams (
        team_id int NOT NULL AUTO_INCREMENT,
        name nvarchar(100) NOT NULL,
        color nvarchar(10) NOT NULL,
        PRIMARY KEY (team_id)
        )'''

    try:
        print("Created table teams")
        cursor.execute(create_teams)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table teams already exists")
        else:
            print(err.msg)


def insert_into_players(cursor, cnx):
    queries = [
        ('Freddy Johansson', 'KRIMZ', '27', 'Sweden', '1.09', '1'),
        ('Alex McMeekin', 'ALEX', '26', 'United Kingdom', '0.99', '1'),
        ('Valentin Vasilev', 'poizon', '23', 'Bulgaria', '1.02', '1'),
        ('Peppe Borak', 'Peppzor', '19', 'Sweden', '0.96', '1'),
        ('William Merriman', 'mezii', '23', 'United Kingdom', '1.11', '1'),
        ('Patrick Hansen', 'es3tag', '26', 'Denmark', '0.96', '2'),
        ('Fredrik Sterner', 'REZ', '24', 'Sweden', '1.15', '2'),
        ('Hampus Poser', 'hampus', '23', 'Sweden', '1.05', '2'),
        ('Ludvig Brolin', 'Brollan', '19', 'Sweden', '1.11', '2'),
        ('Nicolas Gonzalez Zamora', 'Plopski', '19', 'Sweden', '1.02', '2'),
        ('Aleksandr Kostyliev', 's1mple', '24', 'Ukraine', '1.35', '3'),
        ('Denis Sharipov', 'electroNic', '23', 'Russia', '1.07', '3'),
        ('Kirill Mikhailov', 'Boombl4', '23', 'Russia', '0.96', '3'),
        ('Ilya Zalutskiy', 'Perfecto', '22', 'Russia', '1.03', '3'),
        ('Valeriy Vakhovskiy', 'b1t', '19', 'Ukraine', '1.12', '3')
    ]

    for query in queries:
        try:
            cursor.execute("INSERT INTO players (name, nickname, age, nationality, rating, team_id) VALUES (%s, %s, %s, %s, %s, %s)", query)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()
            print(f"Inserted data into players")


def insert_into_coaches(cursor, cnx):
    queries = [
        ('Jamie Hall', 'keita', '29', 'United Kingdom', '1'),
        ('Daniel Narancic', 'djL', '28', 'Sweden', '2'),
        ('Andrey Gorodenskiy', 'B1ad3', '35', 'Ukraine', '3')
    ]
    
    for query in queries:
        try:
            cursor.execute("INSERT INTO coaches (name, nickname, age, nationality, team_id) VALUES (%s, %s, %s, %s, %s)", query)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()
            print(f"Inserted data into coaches")


def insert_into_teams(cursor, cnx):
    queries = [
        ('Fnatic', 'FF5900'),
        ('NIP', 'D8FF00'),
        ('Natus Vincere', 'FFEE00',)
    ]
    
    for query in queries:
        try:
            cursor.execute("INSERT INTO teams (name, color) VALUES (%s, %s)", query)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()
            print(f"Inserted data into teams")


def create_players_teams(cursor):
    create_players_teams = '''
        CREATE VIEW players_teams
        AS SELECT players.nickname, players.age, players.nationality, players.rating, teams.name
        FROM players, teams
        WHERE players.team_id = teams.team_id
        '''

    try:
        print("Created view players and teams")
        cursor.execute(create_players_teams)
    except mysql.connector.Error as err:
        print(err.msg)


def start(cursor, cnx):
    try:
        cursor.execute(f"USE {DB_NAME}")
    except mysql.connector.Error as err:
        print(f"Database {DB_NAME} does not exist")
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, DB_NAME)
            print(f"Created database {DB_NAME}")
            cnx.database = DB_NAME
            create_table_players(cursor)
            insert_into_players(cursor, cnx)
            create_table_coaches(cursor)
            insert_into_coaches(cursor, cnx)
            create_table_teams(cursor)
            insert_into_teams(cursor, cnx)
            create_players_teams(cursor)