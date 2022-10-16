" Эта хуйня для того чтобы хранить пароли. Спасибо наздоровье "
import sqlite3
from uuid import uuid4
from fastapi import Body, FastAPI, Query
from pydantic import BaseModel, Field, validator
from io import StringIO
import bcrypt
import gzip


# db
con = sqlite3.connect("main.db")


# init tables
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS USER(id, name, pwd)")
cur.execute("CREATE TABLE IF NOT EXISTS PAYLOAD(id, user_id, name, value)")
cur.execute("CREATE TABLE IF NOT EXISTS TOKENS(id, user_id, created_at)")


# validation structs
class AuthStruct(BaseModel):
    name: str = Field(max_length=100)
    pwd: str = Field(max_length=100)

    @validator('pwd', 'name')    
    def must_not_contain_space(cls, v):
        assert ' ' in v, 'must not contain a space'
        return v

    @validator('name')
    def name_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v


class PushPayloadStruct(BaseModel):
    payload: str = Field(max_length=10000)


# webapp
app = FastAPI()


# get salt
salt = bcrypt.gensalt()


@app.post("/auth-me")
async def auth_me(req: AuthStruct = Body(embed=True)):
    """ Auth user via login and pass. """
    # match pwd

    # create token

    # return token
    return {"message": "хуй"}


@app.post("/get-payload/{name}")
async def get_payload(name: str = Query(max_length=100, regex='^\S+$')):
    """ Get payload by name and auth token. """

    # check if auth token is valid

    # get payload by user_id and payload name

    # return a payload
    return {"message": "хуй"}


@app.post("/push-payload/{name}")
async def push_payload(name: str = Query(max_length=100, regex='^\S+$'), req: PushPayloadStruct = Body(embed=True)):
    """ Push payload by name and auth token. """

    # check if auth token is valid

    # get payload by user_id and payload name

    # return ok
    return


def compress_str(s: str) -> bytes:
    """ Compress string. """

    out = StringIO()
    f = gzip.GzipFile(fileobj=out, mode="w")
    f.write(s)
    f.close()

    return out.getvalue()


def decompress_str(b: bytes) -> str:
    """ Decompress string. """

    f = gzip.GzipFile(StringIO.StringIO(text))
    result = f.read()
    f.close()

    return result


def get_salty_hash(passwd: str) -> bytes:
    """ Hash it. """
    return bcrypt.hashpw(passwd, salt)


def match_password(passwd, hashed: str) -> bool:
    """ Match it. """
    return bcrypt.checkpw(passwd, hashed):


if __name__ == '__main__':
    print('хуй')

