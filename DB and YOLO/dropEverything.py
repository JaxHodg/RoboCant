from database import *
import configparser as cParse
import os
import psycopg2

#
# TODO
# Learn to host SQL server on docker: https://hub.docker.com/_/mysql -- done
# Then test csv methods -- done
# gitignore password ini -- not done
# create a wipe script
#

#LOAD CONFIG
config = cParse.ConfigParser()
config.read('settings.ini')
dbConfig = config['DATABASE']

dbName   = dbConfig['DBNAME']
dbUrl    = "postgresql://hax:hZ4CJQJZNEOzWRhMPOZU-A@free-tier11.gcp-us-east1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Drobocant-904"
port     = dbConfig['PORT']
headFold = dbConfig['HEAD_FOLD']

#ESATBLISH CONNECTION TO THER SERVER
conn = psycopg2.connect(dbUrl)

#GET THE DIR OF ALL THE DATA NEEDING TO BE PUSHED
curDir = os.getcwd();
headFiles = os.listdir(curDir + '//' + headFold);

try:
    with conn.cursor() as cur:
        for headFile in headFiles:
            cur.execute(
                "DROP TABLE " + headFile.split('.')[0] + ";"
            )
            conn.commit()

except:
    print("DB already set up-1")