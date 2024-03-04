import os
import psycopg2
from dotenv import load_dotenv, find_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
connection = cursor = db = None




def connect():
  global connection, cursor
  
  connection = psycopg2.connect(
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            host=os.environ.get('DB_HOST'),
            port=os.environ.get('DB_PORT'))
  

  # Create a cursor object
  cursor = connection.cursor()

  # Execute SQL query
  cursor.execute("SELECT * FROM foods")

  # Fetch all rows from the result set
  # rows = cursor.fetchall()

  # Print the fetched rows
  # for row in rows:
  #     print(row)

  

connect()









# def connect():
#   connection = psycopg2.connect(
#             database=os.environ.get('DB_NAME'),
#             user=os.environ.get('DB_USER'),
#             password=os.environ.get('DB_PASSWORD'),
#             host=os.environ.get('DB_HOST'),
#             port=os.environ.get('DB_PORT'))
  
#   cursor = connection.cursor()
#   cursor.execute("SELECT * FROM Foods")
#   print(cursor.execute("SELECT * FROM foods"))

# connect()


# def get_db():
#     if not (connection and cursor and db):
#         connect()
#     return connection, cursor, db




##################################################
#please install dependencies for whatever you use including supabase
# import os
# from supabase import create_client, Client
# from dotenv import load_dotenv, find_dotenv
# dotenv_path = find_dotenv()
# load_dotenv(dotenv_path)

# url: str = os.environ.get("supabaseURL")
# key: str = os.environ.get("supabaseKey")
# db_url = os.environ.get("databaseURL")


# supabase: Client =  create_client(url,key)


# def connect():    
#   try:
#     # response = supabase.table('Foods').select("*").execute()
#     response = supabase.table('Foods').select("food_name").eq('nationality', 'american').execute()
#     for item in response.data:
#       print(item)
#   except Exception as e:
#     print("An error occurred", e)


# connect()
########################################################





# import os
# import psycopg2
# from dotenv import load_dotenv
# load_dotenv()
# connect = cursor = db = None

  
# def connect():
#     global connect, cursor, db
#     try:
#         connect = psycopg2.connect(
#             database=os.environ.get('DB_NAME'),
#             user=os.environ.get('DB_USER'),
#             password=os.environ.get('DB_PASSWORD'),
#             host=os.environ.get('DB_HOST'),
#             port=os.environ.get('DB_PORT')
#         )
#         cursor = connect.cursor()
#         db = cursor.execute()

#     except (Exception, psycopg2.DatabaseError) as error:
#         if connect:
#             connect.rollback()
#         print(error)


# def get_db():
#     if not (connect and cursor and db):
#         connect()
#     return connect, cursor, db

