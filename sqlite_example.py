import sqlite3

db = sqlite3.connect('my_database.db')

curs = db.cursor()

create_table = '''CREATE TABLE IF NOT EXISTS demo
(name TEXT PRIMARY KEY, age INTEGER); '''
curs.execute(create_table)

select_all = '''SELECT * FROM demo;'''
curs.execute(select_all)

print(curs.fetchone())

dan = ["Dan", 24]
paul = ["Paul", 21]

insert_values = '''INSERT INTO demo VALUES(?, ?);'''
curs.execute(insert_values, dan)
curs.execute(insert_values, paul)

curs.execute(select_all)
print(curs.fetchone())
print(curs.fetchone())
print(curs.fetchone())

db.close()