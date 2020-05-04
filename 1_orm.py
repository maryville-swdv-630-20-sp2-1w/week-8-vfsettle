#Implement customer class as ORM database and serve as proxy for FillStore and MenuItem databases from the Pizza Company linked via API. 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Customer(Base):
    def __init__(self, name, email, password, address):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    address = Column(String)
    
    def __repr__(self):
        return "<Customer(name={0}, email={1}, password={2}, address={3})>".format(self.name, self.email, self.password, self.address)

    

def main():
    engine = create_engine('sqlite:///:memory:', echo=False)
    
    Base.metadata.create_all(engine)
    
    #Create customers 
    customer1 = Customer("Cheesy Pie", "cheesy.pie@live.maryville.edu", "dblChzPlz!", "44 Crust Way, Gilroy, CA 11111")
    customer2 = Customer("Pizza Eater", "pizza.eater@live.maryville.edu", "pizza4meYum!", "88 Chicago Style, New York, NY 99999")
    print(customer1, customer2)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    #Add customer to session and retreive it
    session.add(customer1)
    session.add(customer2)
    findName = session.query(Customer).filter_by(name='Pizza Eater').first()
    findEmail = session.query(Customer).filter_by(email='cheesy.pie@live.maryville.edu').first()
    print(findName,findEmail)

main()