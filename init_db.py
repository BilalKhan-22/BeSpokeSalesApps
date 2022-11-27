from app import db, Product

turbo_bike = Product(name = 'Turbo', manufacturer = 'BeSpoke', style = 'Red', purchase_price = 30.00, sale_price = 30.00, qty_on_hand = 10, commission_percentage = 10)
casual_bike = Product(name = 'Cruiser', manufacturer = 'BeSpoke', style = 'Blue', purchase_price = 20.00, sale_price = 20.00, qty_on_hand = 20, commission_percentage = 10)
junior_bike = Product(name = 'Junior', manufacturer = 'BeSpoke', style = 'Green', purchase_price = 15.00, sale_price = 15.00, qty_on_hand = 20, commission_percentage = 10)



db.session.add_all([casual_bike, junior_bike])

db.session.commit()

from app import db, Salesperson

sp1 = Salesperson(first_name = 'John', last_name = 'Doe', address = '123 Birch Court', phone = '470-123-4052', manager = 'Ryan Reynolds')
sp2 = Salesperson(first_name = 'Amy', last_name = 'Young', address = '435 Birch Roaf', phone = '470-254-8956', manager = 'Bryan Bunty')



db.session.add_all([sp1, sp2])

db.session.commit()



# comment1 = Comment(content='Comment for the first post', post=post1)
# comment2 = Comment(content='Comment for the second post', post=post2)
# comment3 = Comment(content='Another comment for the second post', post_id=2)
# comment4 = Comment(content='Another comment for the first post', post_id=1)

# from app import db, Student
# student_objects = [
#     Student(firstname='Bilal',
#                lastname='Khan',
#                email='blololand@example.com',
#                age=20,
#                bio='hi biology student'),
#     Student(firstname='Shah',
#                lastname='Hash',
#                email='Hashisgay@example.com',
#                age=22,
#                bio='hello geology student'),
#     Student(firstname='bro',
#                 lastname='man',
#                 email='mom@example.com',
#                 age=22,
#                 bio='hello geology student'),
#     Student(firstname='guy',
#                 lastname='women',
#                 email='your@example.com',
#                 age=22,
#                 bio='hello geology student'),
# ]
# db.session.add_all(student_objects)
# db.session.commit