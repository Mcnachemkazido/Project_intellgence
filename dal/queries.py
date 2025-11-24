from db.connection import get_connection


def running_free_sql(conn,query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()




coon = get_connection()
cursor = coon.cursor()
cursor.execute(  """insert into agents(agent_code, name )
                 VALUES (?,?)""",(131111111111111121,"menacehm"))
coon.commit()



print(running_free_sql(get_connection(),"select * from agents "))