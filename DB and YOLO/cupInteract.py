from database import *
import psycopg2

dbUrl = "postgresql://hax:hZ4CJQJZNEOzWRhMPOZU-A@free-tier11.gcp-us-east1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Drobocant-904"

def returnCup(id):
    #ESATBLISH CONNECTION TO THER SERVER
    conn = psycopg2.connect(dbUrl)

    with conn.cursor() as cur:
        cur.execute("SELECT accid FROM cups WHERE cupid='"+str(id)+"';")
        aid = cur.fetchall()
        conn.commit()
          
        cur.execute(createUpdateQuery("cups", "accid=NULL", "cupid='"+str(id)+"'"))
        cur.execute(createUpdateQuery("accounts", "balance=balance+190, cupsReturned=cupsReturned+1", "id='"+str(aid[0][0])+"'"))
        conn.commit()
    # try:
    # except:
    #     print("failed to return cup")

def takeCup(id, aid):
    #ESATBLISH CONNECTION TO THER SERVER
    conn = psycopg2.connect(dbUrl)  

    with conn.cursor() as cur:
        cur.execute(createUpdateQuery("cups", "accid='"+str(aid)+"'", "cupid='"+str(id)+"'"))
        cur.execute(createUpdateQuery("accounts", "balance=balance-200, cupsTaken=cupsTaken+1", "id='"+str(aid)+"'"))
        conn.commit()

    # try:
        
    # except:
    #     print("failed to withdraw cup")