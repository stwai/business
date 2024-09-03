from app import db
from app.models import User

# Function to add dummy data to the user table
def add_dummy_data():
    # Creating five dummy users
    user1 = User(username='user1', email='user1@example.com')
    user2 = User(username='user2', email='user2@example.com')
    user3 = User(username='user3', email='user3@example.com')
    user4 = User(username='user4', email='user4@example.com')
    user5 = User(username='user5', email='user5@example.com')

    # Add the users to the session
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)

    # Commit the session to the database
    db.session.commit()
    print("Dummy data added successfully!")

# Entry point for the script
if __name__ == '__main__':
    add_dummy_data()