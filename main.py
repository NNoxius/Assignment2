from tokenize import blank_re
from matplotlib.pyplot import show
import mysql.connector
from mysql.connector import errorcode
import PySimpleGUI as sg
from sympy import E
import database_data as dd
import create_database as cb

cnx = mysql.connector.connect(user="root", password="root", host="localhost")
cursor = cnx.cursor()

cb.start(cursor, cnx)


def show_coach(cursor, coach):
    layout = []

    dd.get_coach(cursor, coach)

    cols = ["Name", "Nickname", "Age", "Nationality", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(12,1), justification="center", pad=(4, 1), text_color="#000000", background_color="#B2BEC3"))
    layout.append(columns)

    for c in cursor:
        coaches = []
        for value in c:
            coaches.append(sg.Button(value, size=(12, 3), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(coaches)

    window = sg.Window(coach, layout, background_color="#B2BEC3")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        
    window.close()

def show_age(cursor, age):
    rating = int(age)
    layout = []

    dd.get_age(cursor, age)

    cols = ["Nickname", "Age", "Nationality", "Rating", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(11,1), justification="center", pad=(4, 1), text_color="#000000", background_color="#B2BEC3"))
    layout.append(columns)

    for p in cursor:
        players = []
        for value in p:
            players.append(sg.Button(value, size=(11, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(players)

    window = sg.Window(rating, layout, background_color="#B2BEC3")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    
    window.close()


def show_nationality(cursor, nationality):
    layout = []

    dd.get_nationality(cursor, nationality)

    cols = ["Nickname", "Age", "Nationality", "Rating", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(11,1), justification="center", pad=(4, 1), text_color="#000000", background_color="#B2BEC3"))
    layout.append(columns)

    for p in cursor:
        players = []
        for value in p:
            players.append(sg.Button(value, size=(11, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(players)

    window = sg.Window(nationality, layout, background_color="#B2BEC3")

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
        columns.append(sg.Text(c, size=(12,1), justification="center", pad=(4, 1), text_color="#000000", background_color="#B2BEC3"))
    layout.append(columns)

    for p in cursor:
        players = []
        for value in p:
            players.append(sg.Button(value, size=(12, 3), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(players)

    window = sg.Window(player, layout, background_color="#B2BEC3")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        
    window.close()


def show_statistics(cursor):
    layout = []

    dd.get_team_avg_rating(cursor)

    cols = ["Team", "Average rating"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(11,1), justification="center", pad=(4, 1), background_color="#B2BEC3", text_color="#000000"))
    layout.append(columns)

    teams = set()

    for s in cursor:
        teams.add(s[0])

        statistic = []
        for value in s:
            statistic.append(sg.Button(value, size=(11, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(statistic)
    
    window = sg.Window("Statistics", layout, background_color="#B2BEC3")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event in teams:
            show_team(cursor, event)
    
    window.close()


def show_team(cursor, team):
    color = dd.get_team_color(cursor, team)

    layout = [[sg.Text(team, size=(22,0), justification="center", pad=(6, 1), font=(20), background_color=color, text_color="#000000")]]

    dd.get_team_players(cursor, team)

    cols = ["Nickname", "Age", "Nationality", "Rating"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(11,1), justification="center", pad=(4, 1), background_color=color, text_color="#000000"))
    layout.append(columns)

    nicknames = set()

    for p in cursor:
        nicknames.add(p[0])

        player = []
        for value in p:
            player.append(sg.Button(value, size=(11, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(player)

    dd.get_team_coach(cursor, team)

    c_nicknames = set()

    for c in cursor:
        c_nicknames.add(c[0])

        coach = []
        for value in c:
            coach.append(sg.Button(value, size=(11, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(coach)

    window = sg.Window(team, layout, background_color=color)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event in nicknames:
            show_player(cursor, event)
        elif event in c_nicknames:
            show_coach(cursor, event)
        
    window.close()


def show_coaches(cursor):
    layout = []

    dd.get_coaches(cursor)

    cols = ["Nickname", "Age", "Nationality", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(11,1), justification="center", pad=(4, 1), text_color="#000000", background_color="#B2BEC3"))
    layout.append(columns)

    nicknames = set()
    teams = set()

    for c in cursor:
        nicknames.add(c[0])
        teams.add(c[3])

        coach = []
        for value in c:
            coach.append(sg.Button(value, size=(11, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(coach)

    window = sg.Window("Coaches", layout, background_color="#B2BEC3")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event in nicknames:
            show_coach(cursor, event)
        elif event in teams:
            show_team(cursor, event)
        
    window.close()


def show_teams(cursor):
    layout = []

    dd.get_teams(cursor)

    teams = set()

    for t in cursor:
        teams.add(t[0])

        team = []
        for value in t:
            team.append(sg.Button(value, size=(15, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(team)
    
    layout.append([sg.Button("Statistics", size=(15, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF"))])
    
    window = sg.Window("Teams", layout, background_color="#B2BEC3")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event in teams:
            show_team(cursor, event)
        if event == "Statistics":
            show_statistics(cursor)
        
    window.close()


def show_players(cursor):
    layout = []

    dd.get_players(cursor)

    cols = ["Nickname", "Age", "Nationality", "Rating", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(11,1), justification="center", pad=(4, 1), text_color="#000000", background_color="#B2BEC3"))
    layout.append(columns)

    nicknames = set()
    ages = set()
    nationalities = set()
    teams = set()

    i = 9
    for p in cursor:
        i += 1
        nicknames.add(p[0])
        ages.add(str(p[1]))
        nationalities.add(p[2])
        teams.add(p[4])

        player = []
        for value in p:
            player.append(sg.Button(value, size=(11, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF"), key=str(value) + str(i)))
        layout.append(player)

    window = sg.Window("Players", layout, background_color="#B2BEC3")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        event = event[0:(len(event)-2)]
        if event in nicknames:
            show_player(cursor, event)
        elif event in nationalities:
            show_nationality(cursor, event)
        elif event in teams:
            show_team(cursor, event)
        elif event in ages:
            show_age(cursor, event)
        
    window.close()


def main(cursor):
    layout = [
        [sg.Button("Teams", size=(15, 4), pad=(2, 1), font=(40), button_color=("#000000", "#FFFFFF"))],
        [sg.Button("Players", size=(15, 4), pad=(2, 1), font=(40), button_color=("#000000", "#FFFFFF"))],
        [sg.Button("Coaches", size=(15, 4), pad=(2, 1), font=(40), button_color=("#000000", "#FFFFFF"))]
    ]

    window = sg.Window("Counter-Strike: Global Offensive", layout, background_color="#B2BEC3")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Teams":
            show_teams(cursor)
        if event == "Players":
            show_players(cursor)
        if event == "Coaches":
            show_coaches(cursor)
            
    window.close()


main(cursor)

cursor.close()
cnx.close()
