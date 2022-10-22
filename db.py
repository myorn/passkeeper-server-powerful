import sqlite3
import uuid
from datetime import datetime


class DBManager:
    con = None

    def get_connection(self):
        if not self.con:
            self.con = sqlite3.connect("main.db")

        return self.con

    def init_tables(self):
        cur = self.get_connection().cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS "
                    "USER(id TEXT PRIMARY KEY, name TEXT NOT NULL, pwd TEXT NOT NULL)")
        cur.execute("CREATE TABLE IF NOT EXISTS "
                    "PAYLOAD(id TEXT PRIMARY KEY, user_id TEXT, name TEXT NOT NULL, value TEXT NOT NULL, "
                    "FOREIGN KEY(user_id) REFERENCES USER(id))")
        cur.execute("CREATE TABLE IF NOT EXISTS "
                    "TOKENS(id TEXT PRIMARY KEY, user_id TEXT, created_at TEXT, "
                    "FOREIGN KEY(user_id) REFERENCES USER(id))")

    def create_user(self, name, pwd):
        cur = self.get_connection().cursor()
        cur.execute(
            "INSERT OR IGNORE INTO USER(id, name, pwd) VALUES(?, ?, ?) RETURNING *",
            (str(uuid.uuid4()), name, pwd)
        )
        return cur.fetchone()

    def create_payload(self, user_id: uuid, name: str, value: str):
        cur = self.get_connection().cursor()
        cur.execute(
            "INSERT OR IGNORE INTO PAYLOAD(id, user_id, name, value) VALUES(?, ?, ?, ?) RETURNING *",
            (str(uuid.uuid4()), user_id, name, value)
        )
        return cur.fetchone()

    def create_token(self, user_id: str):
        cur = self.get_connection().cursor()
        cur.execute(
            "INSERT OR IGNORE INTO TOKENS(id, user_id, created_at) VALUES(?, ?, ?) RETURNING *",
            (str(uuid.uuid4()), user_id, str(datetime.now()))
        )
        return cur.fetchone()

