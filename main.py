" Эта хуйня для того чтобы хранить пароли. Спасибо наздоровье "
import sqlite3
from uuid import uuid4
from fastapi import FastAPI
from pydantic import BaseModel
import bcrypt

# db
con = sqlite3.connect("main.db")


# init tables
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS USER(id, name, pwd)")
cur.execute("CREATE TABLE IF NOT EXISTS PAYLOAD(id, user_id, name, value)")
cur.execute("CREATE TABLE IF NOT EXISTS TOKENS(id, user_id, created_at)")


# webapp
app = FastAPI()


@app.post("/auth-me")
async def auth_me():
    """ Auth user via login and pass. """

    # create token

    # return token
    return {"message": "хуй"}


@app.post("/get-payload/{name}")
async def get_payload(name: str):
    """ Get payload by name and auth token. """

    # check if auth token is valid

    # get payload by user_id and payload name

    # return a payload
    return {"message": "хуй"}


@app.post("/push-payload/{name}")
async def push_payload():
    """ Push payload by name and auth token. """

    # check if auth token is valid

    # get payload by user_id and payload name

    # return ok
    return 


@app.post("/auth-me")
async def auth_me():
    """ Auth user via login and pass. """
    return {"message": "хуй"}


if __name__ == '__main__':
    print('хуй')

