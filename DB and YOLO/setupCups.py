from database import *
import psycopg2

dbUrl    = "postgresql://hax:hZ4CJQJZNEOzWRhMPOZU-A@free-tier11.gcp-us-east1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Drobocant-904"

#ESATBLISH CONNECTION TO THER SERVER
conn = psycopg2.connect(dbUrl)

cups = [178446084, 178569732]
cupsLabel = ['A', 'B']

with conn.cursor() as cur:
    for i in range(len(cups)):
        cur.execute("INSERT INTO cups (cupId, cupName) VALUES ('" + str(cups[i]) + "', '" + str(cupsLabel[i]) + "');")
    conn.commit()