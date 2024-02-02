import psycopg2
from database.config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY NOT NULL,
            user_name text NOT NULL,
            first_name text NOT NULL,
            last_name text NOT NULL,
            email text NOT NULL,
            image_data BYTEA NOT NULL,
            is_admin BOOL NULL
        )
        """,
        """ 
        CREATE TABLE orders (
            order_id SERIAL PRIMARY KEY NOT NULL,
            order_name text NOT NULL,
            status text NOT NULL,
            user_id INT NOT NULL,
            calories text
        );
        """,
        """
        CREATE TABLE crepes (
            crepe_id SERIAL PRIMARY KEY NOT NULL,
            crepe_name text NOT NULL,
            image_data BYTEA NOT NULL
        );
        """)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()