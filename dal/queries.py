

def running_free_sql(conn,query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.commit()
    return result


def add_agent(conn,code,name):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO agents(agent_code,name)
                    VALUES(?,?)""",(code,name))
    conn.commit()
    cursor.close()
    return f" המשתמש נוסף בהצלחה  {code}   {name} "


def add_terroris(conn,name):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO terrorists(name)
     VALUES(?)  """,(name,))
    conn.commit()
    cursor.close()

    return f"המחבל נוסף בהצלחה{name}"



def creating_a_report(conn,ageent_id,terrorist_id , information,levl):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO `reports`
        (ageent_id, terrorist_id, information, levl) 
        VALUES (?,?,?,?) """,(ageent_id,terrorist_id,information,levl))
        conn.commit()
        cursor.close()
        return "הדוח עלה בהצלחה"
    except Exception as e:
        if "FOREIGN KEY" in e:
            return "FOREIGN KEY constraint failed"



def deleting_a_report(coon,report_id,agent_id):
    cursor = coon.cursor()
    cursor.execute("""DELETE FROM reports
                    WHERE id = ? AND ageent_id = ?""",(report_id,agent_id))
    coon.commit()
    cursor.close()
    return f"נמחק בהצלחה"


