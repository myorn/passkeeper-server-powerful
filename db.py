""" DB operations module. """
import sqlite3
import uuid
from datetime import datetime

now = datetime.now


def uuid_str():
    """ . """
    return str(uuid.uuid4())


class DBManager:
    """ . """
    con = None

    def __init__(self):
        """ . """
        self.init_tables()

    def get_connection(self):
        """ . """
        if not self.con:
            self.con = sqlite3.connect("main.db")

        return self.con

    def cursor(self):
        """ . """
        return self.get_connection().cursor()

    def init_tables(self):
        """ . """
        cur = self.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS "
                    "USER(id TEXT PRIMARY KEY, name TEXT NOT NULL, pwd TEXT NOT NULL)")
        cur.execute("CREATE TABLE IF NOT EXISTS "
                    "PAYLOAD(id TEXT PRIMARY KEY, "
                    "user_id TEXT, name TEXT NOT NULL, value TEXT NOT NULL, "
                    "FOREIGN KEY(user_id) REFERENCES USER(id))")
        cur.execute("CREATE TABLE IF NOT EXISTS "
                    "TOKENS(id TEXT PRIMARY KEY, user_id TEXT, created_at TEXT, "
                    "FOREIGN KEY(user_id) REFERENCES USER(id))")

    def generic_insert(self, table_name: str, *args):
        """ . """
        placeholders = ("?, " * len(args))[:-2]
        return self.cursor().execute(
            f"INSERT OR IGNORE INTO {table_name} VALUES({placeholders}) RETURNING *",
            args
        ).fetchone()

    def create_user(self, name, pwd):
        """ . """
        return self.generic_insert("USER", uuid_str(), name, pwd)

    def create_payload(self, user_id: uuid, name: str, value: str):
        """ . """
        return self.generic_insert("PAYLOAD", uuid_str(), user_id, name, value)

    def create_token(self, user_id: str):
        """ . """
        return self.generic_insert("TOKENS", uuid_str(), user_id, str(now()))
