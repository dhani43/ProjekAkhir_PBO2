import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("banksampah.db")
        # ---
        self.cursor = self.conn.cursor()
    
    def querySelectAllData(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def querySelectOneData(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def queryDeleteData(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def queryUpdateData(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def query(self, query, param=""):
        self.cursor.execute(query, param)
        self.conn.commit()

    def resultOne(self):
        return self.cursor.fetchone()