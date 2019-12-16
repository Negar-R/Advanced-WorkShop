import psycopg2

# Create DATA BASE!!

# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# conn = psycopg2.connect(user='postgres', password='',
#                         host='localhost', port='5432')

# conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# curs = conn.cursor()

# curs.execute('CREATE DATABASE myMapsa')

# conn.commit()


conn = psycopg2.connect(database='mymapsa', user='postgres', password='',
                        host='localhost', port='5432')


curs = conn.cursor()

curs.execute(
    'CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, name VARCHAR(20) NOT NULL, age int)')

# insert data!
# curs.execute("INSERT INTO users(name, age)VALUES('Ghasem', 16)")
# curs.execute("INSERT INTO users(name, age)VALUES('amirhossein', 24)")
# curs.execute("INSERT INTO users(name, age)VALUES('ali', 30)")
# curs.execute("INSERT INTO users(name, age)VALUES('katayoun', 12)")

# conn.commit()


# curs.execute("UPDATE users SET age= 10 WHERE name = 'katayoun'")


# curs.execute("ALTER TABLE users ADD COLUMN city VARCHAR(50)")
curs.execute(
    "UPDATE users SET city= 'Tehran',age = 10 WHERE name = 'katayoun'")
conn.commit()

curs.execute("SELECT * FROM users")

data = curs.fetchall()

for i in data:
    print(i)