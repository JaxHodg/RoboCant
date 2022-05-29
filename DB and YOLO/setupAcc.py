from database import *
import psycopg2

dbUrl    = "postgresql://hax:hZ4CJQJZNEOzWRhMPOZU-A@free-tier11.gcp-us-east1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Drobocant-904"

#ESATBLISH CONNECTION TO THER SERVER
conn = psycopg2.connect(dbUrl)

with conn.cursor() as cur:
    cur.execute("INSERT INTO accounts (id, balance, accHolder, cupsTaken, cupsReturned) VALUES ('6033', '0', 'alex', '0', '0');")
    cur.execute("INSERT INTO accounts (id, balance, accHolder, cupsTaken, cupsReturned) VALUES ('1290', '0', 'jax', '0', '0');")
    cur.execute("INSERT INTO accounts (id, balance, accHolder, cupsTaken, cupsReturned) VALUES ('7896', '0', 'chris', '0', '0');")
    cur.execute("INSERT INTO accounts (id, balance, accHolder, cupsTaken, cupsReturned) VALUES ('8033', '0', 'ryan', '0', '0');")
    cur.execute("INSERT INTO accounts (id, balance, accHolder, cupsTaken, cupsReturned) VALUES ('4999', '0', 'oliver', '0', '0');")
    conn.commit()