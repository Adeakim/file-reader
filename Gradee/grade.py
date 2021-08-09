import sqlite3
import csv

class Grade:
    connection= sqlite3.connect('gradedb.sqlite')
    cur= connection.cursor()
        
    # def __init__(self,filename):
    #     self.filename=filename
        
        
    def read_csv(self):
        with open('grades.csv','r') as fin: 
            dr = csv.DictReader(fin) 
            to_db = [(i['Last name'], i['First name'],i['SSN'],i['Test1'],
                      i['Test2'],i['Test3'],i['Test4'],i['Final'],i['Grade']) for i in dr]
            return to_db

                
            
    def create_table(self):
        self.cur.execute('''CREATE TABLE if not exists students 
                            ('Last name' VARCHAR, 
                            'First name' VARCHAR, 
                            SSN VARCHAR, 
                            Test1 REAL, Test2 REAL, Test3 REAL, Test4 REAL, 
                            Final REAL, Grade VARCHAR);''')

        self.connection.commit()
    def insert_to_table(self):

            self.cur.executemany('''INSERT INTO students ('Last name', 
                             'First name', SSN, Test1, Test2, Test3, Test4, Final, Grade) 
                             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''',self.read_csv())
            self.connection.commit()


    def create_student_record(self,first_name,last_name,ssn,test1,test2,test3,test4,final,grade):
            self.cur.execute('''INSERT INTO students ('Last name', 
                             'First name', SSN, Test1, Test2, Test3, Test4, Final, Grade) 
                             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''',(first_name,last_name,ssn,test1,test2,test3,test4,final,grade))
            self.connection.commit()
            
    def update_student(self,test1,test2,test3,test4,final,grade,ssn):
        self.cur.execute('''UPDATE students
                        SET 'First name'=?,SSN=?,Test1=?,Test2=?,Test3=?, Test4=?, Final=?, Grade=?
                        WHERE SSN=?
                         ''',(test1,test2,test3,test4,final,grade,ssn))
        self.connection.commit()
    def all(self):
        return self.cur.execute('SELECT * FROM students').fetchall()
        
    def del_student_record(self,SSN):
        self.cur.execute('DELETE FROM students where SSN=?',(SSN,))
        
    def student_that_passed(self):
        return self.cur.execute("SELECT * FROM students WHERE Final>=50 ").fetchall()
    
    def student_that_failed(self):
        return self.cur.execute("SELECT * FROM students WHERE Final<50 ").fetchall()   
    
    def student_test1(self):
        return self.cur.execute("SELECT * FROM students WHERE Test1 > 45.0 ").fetchall()  
    
            
            
   
