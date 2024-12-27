import sqlite3

class Database:
    def __init__(self, path:str):
        self.path = path
        
    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    CREATE TABLE IF NOT EXISTS complaints (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        phone_number TEXT,
                        complain TEXT
                    )
                """
            )
            
            conn.commit()
            
    
    def save_complain(self, data:dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    INSERT INTO complaints (name, phone_number, complain)
                    VALUES (?,?,?)
                """,
                (data['name'], data['phone_number'], data['complain'])
            )