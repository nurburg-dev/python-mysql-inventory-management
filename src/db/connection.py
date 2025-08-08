import mysql.connector
import os
from typing import Optional

class DatabaseConnection:
    _instance: Optional['DatabaseConnection'] = None
    _connection: Optional[mysql.connector.MySQLConnection] = None
    
    def __new__(cls) -> 'DatabaseConnection':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        if self._connection is None:
            self._connection = self._create_connection()
    
    def _create_connection(self) -> mysql.connector.MySQLConnection:
        return mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'devuser'),
            password=os.getenv('DB_PASSWORD', 'password'),
            database=os.getenv('DB_NAME', 'devdb'),
            autocommit=True
        )
    
    def get_connection(self) -> mysql.connector.MySQLConnection:
        if not self._connection or not self._connection.is_connected():
            self._connection = self._create_connection()
        return self._connection
    
    def close(self) -> None:
        if self._connection and self._connection.is_connected():
            self._connection.close()

def get_db_connection() -> mysql.connector.MySQLConnection:
    db = DatabaseConnection()
    return db.get_connection()