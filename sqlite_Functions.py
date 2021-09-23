import sqlite3

def connection():
    conn = sqlite3.connect("Bal.db")
    c = conn.cursor()
    return conn, c

def checknames(conn,c,name):
    