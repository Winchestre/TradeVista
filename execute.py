from market_square import app
from market_square.models import db
from market_square.models import User  # Import your User model

# Create tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)