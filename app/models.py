from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Reviews', backref= backref('restaurant'))
    
    def reviews(self):
        return self.reviews

    def customers(self):
        return[review.customer for review in self.reviews]

# Customer table
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Reviews', backref= backref('customer'))

# reviews delivarables

def full_name(self):
    return f"{self.first_name} {self.last_name}"

def reviews_received(self):
    return self.review_given

def restaurant(self):
    return [review.restaurent for review in self.review_given]

# class table
class Reviews(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    ratings = Column(Integer)

def customer(self):
    return self.customer

def restaurant(self):
    return self.restaurant

