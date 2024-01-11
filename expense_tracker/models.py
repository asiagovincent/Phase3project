from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    
    expenses = relationship('Expense', back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='expenses')

    def __repr__(self):
        return f"<Expense(id={self.id}, amount={self.amount}, description={self.description}, user_id={self.user_id})>"

def create_tables():
    engine = create_engine("sqlite:///your_database_name.db")
    Base.metadata.create_all(bind=engine)

def add_sample_data():
    engine = create_engine("sqlite:///your_database_name.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Adding sample users
    user1 = User(username='john_doe')
    user2 = User(username='jane_smith')
    
    session.add_all([user1, user2])
    session.commit()

    # Adding sample expenses
    expense1 = Expense(amount=50.0, description='Groceries', user=user1)
    expense2 = Expense(amount=20.0, description='Dinner', user=user2)
    
    session.add_all([expense1, expense2])
    session.commit()

if __name__ == "__main__":
    create_tables()
    add_sample_data()
