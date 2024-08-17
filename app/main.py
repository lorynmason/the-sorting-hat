from fastapi import FastAPI
# import mysql.connector
from peewee import MySQLDatabase

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# db = mysql.connector.connect(host = 'mydb', user = 'root', password = 'root', port = 3306)