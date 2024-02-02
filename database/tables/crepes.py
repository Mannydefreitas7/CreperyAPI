from connect import connect
import psycopg2

# SELECT
def select(filter):
    try:
        with connect.cursor() as cur:
             command = "SELECT * FROM crepes"
             if filter:
                 command += " WHERE {filter}"

             cur.execute("SELECT * FROM")
             return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# INSERT
def select(filter):
    try:
        with connect.cursor() as cur:
             command = "SELECT * FROM crepes"
             if filter:
                 command += " WHERE {filter}"

             cur.execute("SELECT * FROM")
             return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)