" Эта хуйня для того чтобы хранить пароли. Спасибо наздоровье "
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from uuid import uuid4

# db
con = sqlite3.connect("tutorial.db")


# init tables
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS USER(id, name, pwd)")
cur.execute("CREATE TABLE IF NOT EXISTS PAYLOAD(id, user_id, name, value)")
cur.execute("CREATE TABLE IF NOT EXISTS TOKENS(id, user_id, created_at)")


# webapp
app = FastAPI()


@app.get("/")
async def root():
    """jhfdsklfjh"""
    return {"message": "хуй"}

if __name__ == '__main__':
    print('хуй')

