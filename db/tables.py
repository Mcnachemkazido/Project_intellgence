from connection import get_connection

def creating_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agents (
	id INT id INTEGER PRIMARY KEY,
    agent_code INT UNIQUE ,
    name VARCHAR(50)  )""")


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS terrorists (
	id id INTEGER PRIMARY KEY,
    name VARCHAR(50) )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
    id id INTEGER PRIMARY KEY,
   	ageent_id INT,
    terrorist_id INT,
    creating_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    information TEXT,
    levl VARCHAR(20),
    FOREIGN KEY (ageent_id) REFERENCES agents(id),
    FOREIGN KEY  (terrorist_id) REFERENCES terrorists(id))""")

    conn.commit()
    cursor.close()
    conn.close()



creating_tables(get_connection())



