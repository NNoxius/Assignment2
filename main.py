from tokenize import blank_re
import mysql.connector
from mysql.connector import errorcode
import PySimpleGUI as sg
import database_data as dd
import create_database as cb

cnx = mysql.connector.connect(user="root", password="root", host="localhost")
cursor = cnx.cursor()

cb.start(cursor, cnx)


def show_nationality(cursor, nationality):
    layout = []

    dd.get_nationality(cursor, nationality)

    cols = ["Name", "Nickname", "Age", "Nationality", "Rating", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(10,1), justification="center", pad=(4, 1), text_color="#000000"))
    layout.append(columns)

    for p in cursor:
        players = []
        for value in p:
            players.append(sg.Button(value, size=(10, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(players)

    window = sg.Window(nationality, layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    
    window.close()


def show_player(cursor, player):
    layout = []

    dd.get_player(cursor, player)

    cols = ["Name", "Nickname", "Age", "Nationality", "Rating", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(10,1), justification="center", pad=(4, 1), text_color="#000000"))
    layout.append(columns)

    for p in cursor:
        players = []
        for value in p:
            players.append(sg.Button(value, size=(10, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(players)

    window = sg.Window(player, layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        
    window.close()


def show_team(cursor, team):
    color = dd.get_team_color(cursor, team)

    layout = [[sg.Text(team, size=(22,0), justification="center", pad=(6, 1), font=("Arial", 20), background_color=color, text_color="#000000")]]

    dd.get_team_players(cursor, team)

    cols = ["Nickname", "Age", "Nationality", "Rating"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(10,1), justification="center", pad=(4, 1), background_color=color, text_color="#000000"))
    layout.append(columns)

    nicknames = set()
    ages = set()
    nationalities = set()
    ratings = set()

    for p in cursor:
        nicknames.add(p[0])
        ages.add(p[1])
        nationalities.add(p[2])
        ratings.add(p[3])

        player = []
        for value in p:
            player.append(sg.Button(value, size=(10, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(player)

    window = sg.Window(team, layout, background_color=color)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        
    window.close()


def show_teams(cursor):
    layout = []

    dd.get_teams(cursor)

    teams = set()

    for t in cursor:
        teams.add(t[0])

        team = []
        for value in t:
            team.append(sg.Button(value, size=(15, 0), pad=(2, 1)))
        layout.append(team)
    
    window = sg.Window("Teams", layout, background_color="#FFFFFF")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event in teams:
            show_team(cursor, event)
        
    window.close()


def show_players(cursor):
    layout = []

    dd.get_players(cursor)

    cols = ["Nickname", "Age", "Nationality", "Rating", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(10,1), justification="center", pad=(4, 1), text_color="#000000"))
    layout.append(columns)

    nicknames = set()
    ages = set()
    nationalities = set()
    ratings = set()
    teams = set()

    for p in cursor:
        nicknames.add(p[0])
        ages.add(p[1])
        nationalities.add(p[2])
        ratings.add(p[3])
        teams.add(p[4])

        player = []
        for value in p:
            player.append(sg.Button(value, size=(10, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(player)

    window = sg.Window("Players", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event in nicknames:
            show_player(cursor, event)
        if event in nationalities:
            show_nationality(cursor, event)
        print(event)
        
    window.close()


def main(cursor):
    layout = [
        [sg.Button("Teams", size=(10, 2), pad=(2, 1))],
        [sg.Button("Players", size=(10, 2), pad=(2, 1))]
    ]

    window = sg.Window("Counter-Strike: Global Offensive", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Teams":
            show_teams(cursor)
        if event == "Players":
            show_players(cursor)
        
    window.close()


main(cursor)

cursor.close()
cnx.close()
