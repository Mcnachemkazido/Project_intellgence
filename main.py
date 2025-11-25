from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from dal import queries
from db.connection import get_connection
from dal import update_csv
from fastapi import UploadFile






app = FastAPI()

@app.get("/")
def welcome():
    return "welcome"

class Query(BaseModel):
    query: str


@app.post("/free")
def running_free(query:Query):
    try:
        return queries.running_free_sql(get_connection(),query.query)

    except Exception as e:
        return {"error":str(e)}


class AgentData(BaseModel):
    name:str
    code:int

@app.post("/add_agent")
def adding_agent(agen_data:AgentData):
    try:
        return queries.add_agent(get_connection(),agen_data.code,agen_data.name)

    except Exception as e:
        return {"error":str(e)}



class TrorData(BaseModel):
    name:str

@app.post("/add_terroris")
def adding_terroris(name:TrorData):
    try:
        return queries.add_terroris(get_connection(),name.name)

    except Exception as e:
        return {"error": str(e)}


class ReportData(BaseModel):
    ageent_id:int
    terrorist_id:int
    information:str
    levl:str

@app.post("/creating")
def creating_a_report(data:ReportData):
    try:
        return queries.creating_a_report(get_connection(),data.ageent_id,
                                    data.terrorist_id,data.information,data.levl)
    except Exception as e:
        return {"error": str(e)}


@app.get("/deleting")
def deleting_report(report_id:int,agent_id:int):
    try:
        return queries.deleting_a_report(get_connection(),report_id,agent_id)

    except Exception as e:
        return {"error": str(e)}


@app.post("/upload-csv")
def upload_csv(file:UploadFile):
    x = update_csv.extract_csv(file)
    coon = get_connection()
    cursor = coon.cursor()
    cursor.executemany("""INSERT INTO agents(agent_code,name)
                        VALUES(?,?)""",x)
    coon.commit()
    cursor.close()




if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)