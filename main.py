" Эта хуйня для того чтобы хранить пароли. Спасибо наздоровье "
import gzip
from datetime import datetime, timedelta
from io import StringIO
from fastapi import Body, FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, validator # pylint: disable=E0611
import bcrypt

from db import DBManager

db = DBManager()


# validation structs
class AuthStruct(BaseModel):
    """ . """
    name: str = Field(max_length=100)
    pwd: str = Field(max_length=100)

    @validator('pwd', 'name')
    def must_not_contain_space(cls, v): # pylint: disable=E0213
        """ . """
        assert ' ' not in v, 'must not contain a space'
        return v

    @validator('name')
    def name_alphanumeric(cls, v): # pylint: disable=E0213
        """ . """
        assert v.isalnum(), 'must be alphanumeric'
        return v


class PushPayloadStruct(BaseModel): # pylint: disable=R0903
    """ . """
    payload: str = Field(max_length=10000)


# webapp
app = FastAPI(docs_url=None, redoc_url=None)


# get salt
salt = bcrypt.gensalt()


# store date here
LAST_REGISTER = None


@app.post("/YOUR/RANDOM/ENDPOINT/86c5ceb27e1bf441130299c0209e5f35b8"
          "8089f62c06b2b09d65772274f12057/register") # change this!
async def register(req: AuthStruct = Body(embed=True)):
    """ Register user via login and pass. """
    global LAST_REGISTER # pylint: disable=W0603

    if LAST_REGISTER and LAST_REGISTER + timedelta(days=1) > datetime.now():
        raise HTTPException(status_code=404)

    LAST_REGISTER = datetime.now()

    # TODO: check if username is not occupied

    # insert user
    user_id = db.create_user(req.name, get_salty_hash(req.pwd))[0]

    # get token
    token = db.create_token(user_id)[0]

    return token


@app.post("/auth-me")
async def auth_me(req: AuthStruct = Body(embed=True)):
    """ Auth user via login and pass. """
    # match pwd

    # create token

    # return token
    return req


@app.get("/get-payload/{name}")
async def get_payload(name: str = Query(max_length=100, regex=r'^\S+$')):
    """ Get payload by name and auth token. """
    # check if auth token is valid

    # get payload by user_id and payload name

    # return a payload
    return name


@app.post("/push-payload/{name}")
async def push_payload(
        name: str = Query(max_length=100, regex=r'^\S+$'),
        req: PushPayloadStruct = Body(embed=True)
        ):
    """ Push payload by name and auth token. """
    # check if auth token is valid

    # get payload by user_id and payload name

    # return ok
    return {name, req}


def compress_str(s: str) -> bytes:
    """ Compress string. """

    out = StringIO()
    fobj = gzip.GzipFile(fileobj=out, mode="w")
    fobj.write(s)
    fobj.close()

    return out.getvalue()


def decompress_str(b: bytes) -> str:
    """ Decompress string. """

    fobj = gzip.GzipFile(StringIO(b))
    result = fobj.read()
    fobj.close()

    return result


def get_salty_hash(passwd: str) -> bytes:
    """ Hash it. """
    return bcrypt.hashpw(passwd.encode('utf8'), salt)


def match_password(passwd, hashed: str) -> bool:
    """ Match it. """
    return bcrypt.checkpw(passwd.encode('utf8'), hashed)


if __name__ == '__main__':
    # Will be moved in the tests later
    # user = db.create_user("test", "test")
    # print(user)
    # payload = db.create_payload(user[0], "test", "test")
    # print(payload)
    # token = db.create_token(user[0])
    # print(token)

    print('хуй')
