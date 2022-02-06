import sqlite3 as sq

def read_sqlite_table():
    try:
        sqlite_connection = sq.connect('answ.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from spisok"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        for row in records:
            print("IMG:", row[0])
            print("quest:", row[1])
            print("answer:", row[2])
            print("ilink:", row[3], end="\n\n")

        cursor.close()

    except sq.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
