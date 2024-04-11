from market_square import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from flask_login import current_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(length=50), nullable=False)
    last_name = db.Column(db.String(length=50), nullable=False)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    date_registered = db.Column(db.DateTime(), default=datetime.utcnow)
    profile_picture = db.Column(db.String(1000), nullable=True, default='default_profile.jpg')
    # budget = db.Column(db.Integer(), nullable=False, default=1000)
    products = db.relationship('Product', backref='owner', lazy=True)


    def check_password_correction(self, attempted_password):
        return self.password_hash == attempted_password


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    previous_price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Integer, nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)
    flash_sale = db.Column(db.Boolean, default=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)
        self.owner_id = current_user.id  # Assign the owner_id to the ID of the current user


    # def __init__(self, **kwargs):
    #     super(Product, self).__init__(**kwargs)
    #     owner = User.query.filter_by(username='Ndman99').first()  # Query the user with the specified username
    #     if owner:
    #         self.owner_id = owner.id


    def check_password_correction(self, attempted_password):
        return self.password_hash == attempted_password