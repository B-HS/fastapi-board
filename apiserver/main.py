from sqlite3 import Cursor
from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse

import json
import pymysql
import dbinfo
import dbquery


def get_json_get_all(result):
    result_ary = []
    tmpjson = {}
    for i, k in result:
        print(i, k)
        result_ary.append({"id":i, "username":k})
    return result_ary


hsdb = pymysql.connect(
    user=dbinfo.db_connect("user"),
    passwd=dbinfo.db_connect("passwd"),
    host=dbinfo.db_connect("host"),
    port=dbinfo.db_connect("port"),
    db=dbinfo.db_connect("db"),
    charset=dbinfo.db_connect("charset")
)

cursor = hsdb.cursor()

# cursor.execute(dbquery.db_query("insertuser", "user", "id", "username", 20, "TeSTING"))
hsdb.commit()


cursor.execute(dbquery.db_query("getall", "user"))
get_all_list_result = cursor.fetchall()



# print(json.dumps(get_json_get_all(result)))



app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/useres")
def read_users():
    


    return JSONResponse(content=get_json_get_all(get_all_list_result))
    
    # json.dumps(get_json_get_all(get_all_list_result))