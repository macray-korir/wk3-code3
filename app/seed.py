from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Reviews

fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.query(Reviews).delete()
    session.commit()

    print("Seeding...")

    restaurants = []
    for i in range(3):
        restaurant = Restaurant(
            name=fake.name(),
            price=random.randint(1, 5)
        )
        session.add(restaurant)
        session.commit()
        restaurants.append(restaurant)

    customers = []
    for i in range(50):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(customer)
        session.commit()
        customers.append(customer)

    reviews = []
    for restaurant in restaurants:
        for i in range(random.randint(1, 5)):
            customer = random.choice(customers)

            review = Reviews(
                ratings=random.randint(1, 5),
                customer_id=customer.id,
                restaurant_id=restaurant.id
            )
            session.add(review)
            session.commit()

    session.close()
    print("Seed completed.")
