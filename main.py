from Gradee.grade import Grade
from models.book import Book
from models.user import User
from table import FormTable
from connectDB import Connect


# c=Connect()
# c.connect_psycopg2()
#
# FormTable
# table=FormTable()
# table.create_table()
# table.insert_table()


# #Book

# book=Book()
# # print(book.get_by_id(1))#
# print (book.del_user_record(2))
# print (book.del_user_record(3))
# print (book.del_user_record(4))
# print (book.create_book_record(2,'Men are from venus',1000))
# print (book.del_user_record(4))
# # print(book.get_by_id(3))
# # print(book.update_book_record('Men are from mars, women are from venus',1000,2))

# #User
# user=User()
#
# print(user.all())
# print(user.create_user_record('drRash19','Rashford','Marcus'))
# # print(user.get_by_id(1))
# print(user.update_user_record('froz','Funsho','Wiliams',1))
# # print(user.del_user_record(1))


grade= Grade()
# print(grade.student_that_failed())
print(grade.all())
# # print(grade.student_that_passed())


