import psycopg2 as pg
import json
import os

# Open the file and load its content
script_dir = os.path.dirname(os.path.abspath(__file__))
credentials_path = os.path.join(script_dir, 'credentials.json')

with open(credentials_path, 'r') as file:
    data = json.load(file)

print(data)

db_host = data['db_host']
db_name = data['db_name']
db_port = data['db_port']
db_user = data['db_user']
db_password = data['db_password']

conn = pg.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password,
    port=db_port
)
print("Connected to the database successfully!")

cursor = conn.cursor()
cursor.execute("SELECT version();")
db_version = cursor.fetchone()
print(f"Database version: {db_version[0]}")
cursor.close()
conn.close()
