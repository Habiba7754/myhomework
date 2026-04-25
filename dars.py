import pymysql

# class MySQL:
#     def __init__(self):
#         self.ConnectDB()
#         self.create_tb()
#         self.CreateDB()

#     def ConnectDB(self):
#         self.db = pymysql.connect(
#             host="localhost",
#             user="root",
#             password="1234",
#             database="School"

#         )
#         self.c = self.db.cursor()

    # def CreateDB(self):
    #     self.c.execute("CREATE DATABASE IF NOT EXISTS School")
    #     self.c.execute("USE School")

    # def create_tb(self):
    #     self.c.execute('''create table if not exists company(
    #                    name varchar(50),
    #                    location varchar(50),
    #                    capital int,
    #                    employees_count int,
    #                    establishedAt int,
    #                    monthly_expenses int
    #                    )''')
        
    # def insert(self):
    #     self.c.execute("""insert into company values
    #                     ('Alpha Tech', 'Tashkent', 500000, 120, 2015, 20000),
    #                     ('Beta Solutions', 'Samarkand', 300000, 80, 2018, 15000),
    #                     ('Gamma Group', 'Tashkent', 700000, 200, 2012, 30000),
    #                     ('Delta Corp', 'Bukhara', 250000, 50, 2020, 10000),
    #                     ('Epsilon LLC', 'Tashkent', 450000, 90, 2016, 18000)""")
    #     self.db.commit()
        
#     def first(self):
#         self.c.execute("select name from company order by name")
#         return self.c.fetchall()
    
#     def second(self):
#         self.c.execute("select capital from company order by capital desc")
#         return self.c.fetchall()
    
#     def third(self):
#         self.c.execute("select * from company order by employees_count")
#         return self.c.fetchall()
    
#     def fourth(self):
#         self.c.execute("select * from company where location = 'Tashkent'")
#         return self.c.fetchall()
    
#     def fifth(self):
#         self.c.execute("select location, count(*) from company group by location")
#         return self.c.fetchall()
    
#     def olti(self):
#         self.c.execute("select name, (2026 - establishedAt) * monthly_expenses * 12 AS total_expenses from company")
#         return self.c.fetchall()
    

        
# c1 = MySQL()
# 1
# print(c1.first())

# 2
# print(c1.second())

# 3
# print(c1.third())

# 4
# print(c1.fourth())

# 5
# print(c1.fifth())

# 6
# print(c1.olti())

# ---------------------------------------------

# class MySQL:
#     def __init__(self):
#         self.ConnectDB()
#         self.create_tb()
#         self.CreateDB()

#     def ConnectDB(self):
#         self.db = pymysql.connect(
#             host="localhost",
#             user="root",
#             password="1234",
#             database="School"

#         )
#         self.c = self.db.cursor()

#     def CreateDB(self):
#         self.c.execute("CREATE DATABASE IF NOT EXISTS School")
#         self.c.execute("USE School")

#     def create_tb(self):
#         self.c.execute('''create table if not exists Restoranlar(
#                         id INT AUTO_INCREMENT PRIMARY KEY,
#                         name VARCHAR(100),
#                         address VARCHAR(150),
#                         maxFoodPrice INT,
#                         minFoodPrice INT,
#                         employeesCount INT,
#                         experience INT)''')
    
#     def insert(self):
#         self.c.execute("""insert into restoranlar (name, address, maxFoodPrice, minFoodPrice, employeesCount, experience) values
#                         ('Master Grill', 'Tashkent', 200000, 50000, 30, 5),
#                         ('Marmar Steak', 'Samarkand', 180000, 40000, 25, 4),
#                         ('Maroqand Restoran', 'Bukhara', 150000, 30000, 20, 6),
#                         ('Modern Food', 'Tashkent', 220000, 60000, 35, 7),
#                         ('Milan Cafe', 'Andijan', 100000, 20000, 15, 3),
#                         ('Metro Bites', 'Tashkent', 90000, 15000, 18, 2),
#                         ('Moon Restaurant', 'Namangan', 250000, 70000, 40, 8),
#                         ('Market Taste', 'Fergana', 130000, 25000, 22, 5),
#                         ('Marmar', 'Tashkent', 170000, 45000, 28, 6),
#                         ('Burger Master', 'Samarkand', 120000, 20000, 20, 4)""")
#         self.db.commit()

#     def first(self):
#         self.c.execute('select * from restoranlar where name like "M%r" order by maxFoodPrice')
#         return self.c.fetchall()

#     def second(self):
#         self.c.execute("select name from restoranlar order by minFoodPrice limit 3")
#         return self.c.fetchall()

#     def third(self):
#         self.c.execute("select name, maxFoodPrice from restoranlar order by experience desc, maxFoodPrice desc limit 4")
#         return self.c.fetchall()
    
# r1 = MySQL()
# r1.insert()

# 1
# print(r1.first())

# 2
# print(r1.second())

# 3
# print(r1.third())