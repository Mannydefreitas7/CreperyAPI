from sqlite3 import OperationalError
import psycopg2
from config import load_config

def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    print(sqlFile)
    fd.close()
    config = load_config()
    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')
    try:
        with  psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in sqlCommands:
                    if command is not '':
                        cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print("Command skipped: ", error)

if __name__ == '__main__':
    executeScriptsFromFile()