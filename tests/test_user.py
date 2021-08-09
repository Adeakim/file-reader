import unittest
from models.user import User



class TestUser(unittest.TestCase):
    def setUp(self):
       self.user=User()
        
    def test_get_all(self):
        get_all= self.user.all()
        self.assertIsInstance(get_all,list)
        self.assertIsNotNone(get_all)
        
    def test_get_by_id(self):  
        get_by_id=self.user.get_by_id(1)
        self.assertIsNotNone(get_by_id)
        self.assertIsInstance(get_by_id,list)
    
    def test_update(self):
        update= self.user.update_user_record('froz','Ade','Peter',1)
        self.assertIsNotNone(update)
        self.assertIsInstance(update,str)
        self.assertEqual(update,'Record updated')
        
    def test_delete(self):
        delete=self.user.del_user_record(1)
        self.assertEqual(delete,'Record deleted')
        self.assertIsNotNone(delete)
    
    
    