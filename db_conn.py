from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

def connect_db():
    try:
      conn = psycopg2.connect(DATABASE_URL)
      print("Connection successful.")
      return conn
    except psycopg2.Error as error:
       print("Error connecting to the database:", error)

def close_db(conn):
    if conn is not None:
       conn.close()
       print("Connection closed")