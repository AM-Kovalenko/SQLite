import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()




    # cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score")
    # result = cur.fetchall()
    # print(result)
    # for res in result:
    #     print(res)

    # # Удаление таблицы
    #cur.execute("DROP TABLE games")


    # # Создание таблицы
    # cur.execute("""CREATE TABLE IF NOT EXISTS users (
    #
    # name TEXT NOT NULL,
    # sex INTEGER DEFAULT 1,
    # old INTEGER,
    # score INTEGER
    # )""")


    # # Создание таблицы
    # cur.execute("""CREATE TABLE IF NOT EXISTS games (
    # user_id INTEGER ,
    # score INTEGER,
    # time INTEGER
    # )""")

    # заполнение таблицы users
    # cur.execute("INSERT INTO users VALUES "
    #             "('Михаил', 1, 19, 1000),"
    #             "('Алекс', 1, 20, 100), "
    #             "('Вася', 1, 21, 200), "
    #             "('123', 1, 22, 5000), "
    #             "('Миха', 2, 23, 1000), "
    #             "('Настя', 2, 29, 1500)")

    # заполнение таблицы games

    cur.execute("INSERT INTO games VALUES"
                "(1, 100, 10 ),"
                "(2, 200, 20 ),"
                "(3, 300, 30 ),"
                "(4, 400, 40 ),"
                "(5, 500, 50 ),"
                "(6, 100, 60 ),"
                "(1, 1000, 70 ),"
                "(1, 1000, 80 ),"
                "(2, 500, 90 ),"
                "(3, 500, 100 )")