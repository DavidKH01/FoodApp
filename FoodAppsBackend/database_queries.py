import database_connect
import psycopg2.extras
from database_connect import connection, cursor


def test_select():
    cursor.execute("SELECT * FROM foods")
    print(cursor.fetchall())

def get_all_names():
    cursor.execute("SELECT food_name FROM foods")
    name = cursor.fetchall()
    cleaned_data = [item[0].replace('(', '').replace(')', '').replace(',', '') for item in name]
    for item in cleaned_data:
        print(item)
    return cursor.fetchall()

def get_all_foods():
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT id, name, rating, restaurant, category, min_price_range, max_price_range, nationality FROM foods")
    return cursor.fetchall()



def test_insert():
    cursor.execute('INSERT INTO foods(name, rating, restaurant, category, min_price_range, max_price_range, nationality) VALUES (%s, %s,%s, %s,%s,%s, %s)', ("Spicy Chicken Deluxe Sandwich", 9,"Chik Fil A" , "Chicken", 7, 11, "American"))
    cursor.execute('INSERT INTO foods(name, rating, restaurant, category, min_price_range, max_price_range, nationality) VALUES (%s, %s,%s, %s,%s,%s, %s)', ("Cookie Dough Ice Cream", 10,"Harris Teeter" , "Dairy", 4, 10, "American"))
    connection.commit()


def add_new_food(name, rating, restaurant, category, min_price_range, max_price_range, nationality):
    cursor.execute('INSERT INTO foods(name, rating, restaurant, category, min_price_range, max_price_range, nationality) VALUES (%s, %s,%s, %s,%s,%s, %s) RETURNING id', (name, rating, restaurant, category, min_price_range, max_price_range, nationality))

    connection.commit()
    return cursor.fetchone()[0]


# test_select()
get_all_names()


