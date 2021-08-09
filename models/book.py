from connectDB import Connect
from datetime import datetime

class Book:
    def __init__(self):
        self.connection= Connect().connect_psycopg2()
        self.cursor= self.connection.cursor()
    
    
    
    def get_all_users(self):
       
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()
            
    def get_by_user_id(self,user_id):
        try:
            self.cursor.execute("SELECT name FROM books WHERE user_id=%s ", (user_id,))
            return self.cursor.fetchall()
        except Exception:
            return "User id not present in table 'Users' "
        
    def create_book_record(self,user_id,name,pages):
        try:
            self.cursor.execute(''' INSERT INTO books(user_id,name,pages)
                                    VALUES(%s,%s,%s)''',(user_id,name,pages))
            self.connection.commit()
            return "Record created"
        except Exception:
            return "User id not present in table 'Users' "

    def get_by_id(self,num):
        self.cursor.execute("SELECT name FROM books WHERE id= %s ", (num,))
        return self.cursor.fetchall()
    
    def update_book_record(self,name,pages,id):
        updated_time=datetime.now()
        self.cursor.execute(''' UPDATE books
                            SET name=%s,pages=%s,uptime_at=%s WHERE id = %s''',(name,pages,updated_time,id)
                                    
                                    )
        self.connection.commit()
        return "Record updated"
    def del_user_record(self,id):        
            self.cursor.execute(''' DELETE FROM books
                                    WHERE id=%s''',(id,))
            self.connection.commit()     
            return "Rocord deleted"


    # book=Book()
    # book.create_book_record('')
    #
