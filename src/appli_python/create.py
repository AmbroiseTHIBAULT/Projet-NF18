#!/usr/bin/python3

import psycopg2


def createTables(conn):
    cur = conn.cursor()
    cur.execute(open("../creation.sql", "r").read())
    conn.commit()
    cur.close()


def insertDonnees(conn):
    cur = conn.cursor()
    cur.execute(open("../insertion.sql", "r").read())
    conn.commit()
    cur.close()
