import mysql.connector
import PySimpleGUI as sg
import database_data as dd
import create_database as cb


# Connect to database
cnx = mysql.connector.connect(user="root", password="root", host="localhost")
cursor = cnx.cursor()

# Create database
cb.start(cursor, cnx)


# Display coaches in new window
def show_coach(cursor, coach):
    layout = []

    # Get coaches from database
    dd.get_coach(cursor, coach)

    # Add column headers to layout
    cols = ["Name", "Nickname", "Age", "Nationality", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(12,1), justification="center", pad=(4, 1), text_color="#000000", background_color="#B2BEC3"))
    layout.append(columns)

    # Add data to layout
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


# Display players with age
def show_age(cursor, age):
    rating = int(age)
    layout = []

    # Get players with age from database
    dd.get_age(cursor, age)

    # Add column headers to layout
    cols = ["Nickname", "Age", "Nationality", "Rating", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(11,1), justification="center", pad=(4, 1), text_color="#000000", background_color="#B2BEC3"))
    layout.append(columns)

    # Add data to layout
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


# Display players with nationality
def show_nationality(cursor, nationality):
    layout = []

    # Get players with nationality from database
    dd.get_nationality(cursor, nationality)

    # Add column headers to layout
    cols = ["Nickname", "Age", "Nationality", "Rating", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(11,1), justification="center", pad=(4, 1), text_color="#000000", background_color="#B2BEC3"))
    layout.append(columns)

    # Add data to layout
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


# Display player
def show_player(cursor, player):
    layout = []

    # Get player from database
    dd.get_player(cursor, player)

    # Add column headers to layout
    cols = ["Name", "Nickname", "Age", "Nationality", "Rating", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(12,1), justification="center", pad=(4, 1), text_color="#000000", background_color="#B2BEC3"))
    layout.append(columns)

    # Add data to layout
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


# Display team statistics
def show_statistics(cursor):
    layout = []

    # Get statistics from database
    dd.get_team_avg_rating(cursor)

    # Add column headers to layout
    cols = ["Team", "Average rating"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(11,1), justification="center", pad=(4, 1), background_color="#B2BEC3", text_color="#000000"))
    layout.append(columns)

    teams = set()

    # Add data to layout
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
        # If team button pressed display team
        if event in teams:
            show_team(cursor, event)
    
    window.close()


# Display team
def show_team(cursor, team):
    # Get team color from database
    color = dd.get_team_color(cursor, team)

    layout = [[sg.Text(team, size=(22,0), justification="center", pad=(6, 1), font=(20), background_color=color, text_color="#000000")]]

    # Get team players from database
    dd.get_team_players(cursor, team)

    # Add column headers to layout
    cols = ["Nickname", "Age", "Nationality", "Rating"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(11,1), justification="center", pad=(4, 1), background_color=color, text_color="#000000"))
    layout.append(columns)

    nicknames = set()

    # Add data to layout
    for p in cursor:
        nicknames.add(p[0])

        player = []
        for value in p:
            player.append(sg.Button(value, size=(11, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF")))
        layout.append(player)

    # Get team coach from database
    dd.get_team_coach(cursor, team)

    c_nicknames = set()

    # Add data to database
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
        # If nickname button pressed display player
        if event in nicknames:
            show_player(cursor, event)
        # If coach nickname button pressed display player
        elif event in c_nicknames:
            show_coach(cursor, event)
        
    window.close()


# Display coaches
def show_coaches(cursor):
    layout = []

    # Get coaches from database
    dd.get_coaches(cursor)

    # Add column headers to layout
    cols = ["Nickname", "Age", "Nationality", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(11,1), justification="center", pad=(4, 1), text_color="#000000", background_color="#B2BEC3"))
    layout.append(columns)

    nicknames = set()
    teams = set()

    # Add data to layout
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
        # If nickname button pressed display player
        if event in nicknames:
            show_coach(cursor, event)
        # If team button pressed display team
        elif event in teams:
            show_team(cursor, event)
        
    window.close()


# Display teams
def show_teams(cursor):
    layout = []

    # Get teams from database
    dd.get_teams(cursor)

    teams = set()

    # Add data to layout
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
        # If team button pressed display team
        if event in teams:
            show_team(cursor, event)
        # If statistics button pressed display statistics
        if event == "Statistics":
            show_statistics(cursor)
        
    window.close()


# Display players
def show_players(cursor):
    layout = []

    # Get players from database
    dd.get_players(cursor)

    # Add column headers to layout
    cols = ["Nickname", "Age", "Nationality", "Rating", "Team"]
    columns = []
    for c in cols:
        columns.append(sg.Text(c, size=(11,1), justification="center", pad=(4, 1), text_color="#000000", background_color="#B2BEC3"))
    layout.append(columns)

    nicknames = set()
    ages = set()
    nationalities = set()
    teams = set()

    # Add data to layout
    i = 9
    for p in cursor:
        i += 1
        nicknames.add(p[0])
        ages.add(str(p[1]))
        nationalities.add(p[2])
        teams.add(p[4])

        player = []
        for value in p:
            # Add special key to later make same buttons output same event
            player.append(sg.Button(value, size=(11, 2), pad=(2, 1), button_color=("#000000", "#FFFFFF"), key=str(value) + str(i)))
        layout.append(player)

    window = sg.Window("Players", layout, background_color="#B2BEC3")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        # Remove numbers from key to make same buttons output same event
        event = event[0:(len(event)-2)]
        # If nickname button pressed display player
        if event in nicknames:
            show_player(cursor, event)
        # If nationality button pressed display nationalities
        elif event in nationalities:
            show_nationality(cursor, event)
        # If team button pressed display teams
        elif event in teams:
            show_team(cursor, event)
        # If age button pressed display ages
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
        # If teams button pressed display teams
        if event == "Teams":
            show_teams(cursor)
        # If players button pressed display players
        if event == "Players":
            show_players(cursor)
        # If coaches button pressed display coaches
        if event == "Coaches":
            show_coaches(cursor)
            
    window.close()


# Start program
main(cursor)

cursor.close()
cnx.close()
