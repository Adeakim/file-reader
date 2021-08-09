from typing import BinaryIO
import psycopg2

class Connect:
    @classmethod
    def connect_psycopg2(self):
        connection=psycopg2.connect(
            host= 'localhost',
            database='decagon',
            user='postgres',
            password=1234,
            port= 5432
            
            
        )
        
        return connection
    
    
a=Connect()
a.connect_psycopg2()

