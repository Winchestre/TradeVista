from market_square.models import db
from market_square.models import User  # Import your User model

def find_user_by_email(email):
    # Query the database for a user with the specified email address
    user = User.query.filter_by(email_address=email).first()

    # Check if a user with the specified email address was found
    if user:
        print("User found:")
        print("First Name:", user.first_name)
        print("Last Name:", user.last_name)
        print("Username:", user.username)
        # Print any other relevant user information
    else:
        print("No user found with the email address:", email)
