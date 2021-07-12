import sqlite3 as sq

with sq.connect("cars.db") as con:
    cur = con.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    price INTEGER 
    )""")

    cur.execute("INSERT INTO cars VALUES(1, 'AUDI', 55555)")
    cur.execute("INSERT INTO cars VALUES(2,'Mersedes', 5123)")
    cur.execute("INSERT INTO cars VALUES(3, 'Skoda', 2323355)")
    cur.execute("INSERT INTO cars VALUES(4, 'Volvo', 532152)")
    cur.execute("INSERT INTO cars VALUES(5, 'Bentley', 567657)")