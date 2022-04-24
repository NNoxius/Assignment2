import mysql.connector
from mysql.connector import errorcode
import PySimpleGUI as sg
import database_data as dd
import create_database as cb

cnx = mysql.connector.connect(user="root", password="root", host="localhost")
cursor = cnx.cursor()

cb.start(cursor, cnx)

layout = [

]

dd.get_team_players(cursor, "Fnatic")

for item in cursor:
    player = []
    for value in item:
        player.append(sg.Text(value))
    layout.append(player)

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()