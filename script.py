import sqlite3
from sqlite3 import Error

try:
    sqliteConnection = sqlite3.connect("C:\\Users\\gusge\\Documents\\GitHub\\hotel_pitangueira2\\db.sqlite3")
    cursor = sqliteConnection.cursor()
except Error as e:
        print(e)

try:
    for q in range(0,70,1):
        sqlite_select_Query1 = "INSERT INTO quartos_quarto(tipo, status) VALUES(1, 'L')"
        cursor.execute(sqlite_select_Query1)

    for q in range(0,30,1):
        sqlite_select_Query2 = "INSERT INTO quartos_quarto(tipo, status) VALUES(2, 'L')"
        cursor.execute(sqlite_select_Query2)
    for q in range(0,10,1):
        sqlite_select_Query3 = "INSERT INTO quartos_quarto(tipo, status) VALUES(3, 'L')"
        cursor.execute(sqlite_select_Query3)

    record = cursor.fetchall()
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")