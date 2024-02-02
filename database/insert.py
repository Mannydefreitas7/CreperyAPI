import psycopg2
from connect import connect
from models.crepe import CrepeSchema


# INSERT
def insert(table, payload):
    sql = "INSERT INTO %s"
    keys = dict(payload).keys()
    values = ""
    columns = ""

    for index, key in enumerate(keys):
        if index != len(keys):
            columns += "{key},"
            values += dict(payload)[key] + ", "
        else:
            columns += "{key}"
            values += dict(payload)[key]

    sql += "({columns}) VALUES({values})"

    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, table)
                cur.commit()
                return payload
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    user_data = {
        "crepe_id": 0,
        "name": "crepe",
        "description": "",
        "calories": "",
        "topping_id": 1,
        "image_data": ""
    }
    schema = CrepeSchema()
    result = schema.load(user_data)
    insert("crepes", result)
