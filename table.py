from connectDB import Connect



class FormTable:
    connection= Connect().connect_psycopg2()
    cursor= connection.cursor()

    @classmethod
    def create_table(self):
        # self.cursor.execute('DROP TABLE if exists users CASCADE ')
        # self.cursor.execute('DROP TABLE if exists books ')
        
        with open('schema.sql','r') as fp:
                self.cursor.execute(fp.read())
                self.connection.commit()
                
    @classmethod         
    def insert_table(self):
            
            with open('seeder.sql','r') as fp:
                self.cursor.execute(fp.read())
                self.connection.commit() 
    
   

