import unittest
from grade import Grade
import sqlite3

class TestGrade(unittest.TestCase):
    def setUp(self):
        connection= sqlite3.connect('gradedb.sqlite')
        self.cur= connection.cursor()
        
        self.grade=Grade()
        self.grade.create_table()
        self.grade.insert_to_table()
        
    
    def test_create_table(self):
        table=self.grade.create_table()  
        self.assertIsNone(table) 
         
    def test_create_student(self):
        create= self.grade.create_student_record()
        self.assertIsNone(create)
    
    def test_del_studente_record(self):
        delete= self.grade.del_student_record('123-12-1234')
        self.assertIsNone(delete)
    
    def test_student_that_passed(self):
        passed=self.grade.student_that_passed()
        self.assertEqual(len(passed),5)
        self.assertIsNotNone(passed)
        self.assertIsInstance(passed,list)    
    
        
    def test_student_that_failed(self):
         failed=self.grade.student_that_failed()
         self.assertEqual(len(failed),11)
         self.assertIsNotNone(failed)
         self.assertIsInstance(failed,list)
         
    
        
    def tearDown(self):
        self.grade.del_table()
        self.grade=None
        
if __name__=='__main__':
    unittest.main()