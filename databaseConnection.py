import psycopg2
from psycopg2.extras import RealDictCursor

connec_para={
    "dbname": "mydatabase",
    "user": "postgres",
    "password": "password",
    "host": "localhost",
    "port": 5432
     }
connection = psycopg2.connect(**connec_para)
connection.autocommit = True 

cursor = connection.cursor(cursor_factory=RealDictCursor)
create_table='''create table if not exists items(
                id SERIAL PRIMARY KEY,
                name TEXT,
                description TEXT,
                price INT,
                quantity INT
                )'''

cursor.execute(create_table)
