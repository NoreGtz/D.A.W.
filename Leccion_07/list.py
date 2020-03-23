import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:sushi@localhost:5432/airline")
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT * FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    main()
