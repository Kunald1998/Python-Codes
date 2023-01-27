import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # To talk to the 'existing database'.
from sqlalchemy.ext.declarative import declarative_base # For the 'base' class.
from sqlalchemy import Column,Integer,String # This import is used to provide the 'data type' for out table.

# Use of the pymysql library is for making the connection with the mysql database.
# PyMySQL is an interface for connecting to a MySQL database server from Python.
# It implements the Python Database API v2. 0 and contains a pure-Python MySQL client library. 
# The goal of PyMySQL is to be a drop-in replacement for MySQLdb.

engine = create_engine("mysql+pymysql://root:@localhost:3306/MarvellousInfosystems",echo=False)

# print(engine) # OUTPUT = Engine(mysql+pymysql://root:***@localhost:3306/MarvellousInfosystems)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

# This student class is inherit the 'Base' class that we created above.
class Automobile(Base):
    __tablename__ = "Automobile"
    
    Car_Id = Column(Integer,primary_key = True)
    Car_Name = Column(String(50))
    Car_Price = Column(Integer)
    Car_Brand = Column(String(50))

# In below syntax we reflected/created table into existing database.
#Base.metadata.create_all(engine)

#####  Below syntax is used to add the data into the table. ####

automobile_obj1 = Automobile(Car_Name = "SwiftZXI",Car_Brand = "Suzuki",Car_Price = 820000)
automobile_obj2 = Automobile(Car_Name = "Supra_2JZ",Car_Brand = "Toyota",Car_Price = 3900000)
automobile_obj3 = Automobile(Car_Name = "Skyline_RB32",Car_Brand = "Nissan",Car_Price = 5600000)
automobile_obj4 = Automobile(Car_Name = "Subru",Car_Brand = "WRX_STI",Car_Price = 1200000)

"""
session.add_all([automobile_obj1,automobile_obj2,automobile_obj3,automobile_obj4])
session.commit()
"""
####  Below syntax is used to 'Read' the data from the table. ####
"""
# 1st Step: Get all the data.
# All the data returned by the 'query' method is stored in the Variable 'automobile_Data'.
automobile_Data1 = session.query(Automobile)
#
# All the data from 'Table' is get stored in 'automobile_Data' variable.
# To display the complete data you need to use for loop. 
for Cars in automobile_Data1:
    print(Cars.Car_Name,Cars.Car_Brand,Cars.Car_Price)

# 2nd Step: Get data in order.
automobile_Data2 = session.query(Automobile).order_by(Automobile.Car_Name)
for name in automobile_Data2:
    print(name.Car_Name)

# 3rd step: Get data by filtering.

automobile_Data3 = session.query(Automobile).filter(Automobile.Car_Name == "Skyline_RB32").first()
print("Data after applying the filter is:",automobile_Data3.Car_Name,automobile_Data3.Car_Price)

# 4th step: Count of Result.

automobile_Data4 = session.query(Automobile).filter((Automobile.Car_Brand == "Suzuki")).count()
print("Data after count Automobile.Car_Brand is:",automobile_Data4)

"""
#### Update the data in Table. ####
# 1st step: Get record.

automobile_1 = session.query(Automobile).filter(Automobile.Car_Brand == "Toyota").first()

Automobile.Car_Name = "MK-2"

session.commit()


