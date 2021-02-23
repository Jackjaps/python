
import jaydebeapi
import os
from config import Config

class dataInformix:
    def __init__(self):
        self.connectionString_url = 'jdbc:postgresql://{}:{}/{}'.format(Config.DATABASE_CONFIG['hostname'],Config.DATABASE_CONFIG['port'],Config.DATABASE_CONFIG['database'])
        self._conn = jaydebeapi.connect(Config.DATABASE_CONFIG['driver_class'],self.connectionString_url,[Config.DATABASE_CONFIG['user'], Config.DATABASE_CONFIG['password']],os.path.join(Config.DATABASE_CONFIG['driver_path']))
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor
    
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def close(self, params=None):
        self._conn.close()
