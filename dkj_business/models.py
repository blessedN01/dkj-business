from dkj_business import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


# User database model design
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    cash = db.Column(db.Float(), nullable=False, default=1000)
    username = db.Column(db.String(80), unique=True, index=True, nullable=False)
    profil_picture = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    date_of_birth = db.Column(db.Date(), nullable=True) # This line should be fixed because not sure it will work
    products = db.relationship("Product", backref='owned_products', lazy=True)
    purchases = db.relationship("Purchase", backref="purchases")
    is_seller = db.Column(db.Boolean(), default=False)
    # description= db.Column(db.Text(), nullable=True)
    # Create a shop table where users will save their shop info(location, contact, shop_name, and so on and so forth)
    # Design a setting where user cant could set up his account parameters
    # Set up setting according to if user is seller or not


    def __repr__(self):
        return f"User {self.username}"
    def set_passaword(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.password_hash = generate_password_hash(new_password)
            return True
        return False
    def recharge_balance(self, amount):
        self.cash += amount
    def become_seller(self):
        if self.seller_requirments:
            self.is_seller = True
    def seller_requirements():
        pass
    
# Product database model design
class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    product_name = db.Column(db.String(20), nullable=False)
    owner_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    category = db.Column(db.String(20))
    description = db.Column(db.String(length=1024), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False, default=1)
    available = db.Column(db.Boolean(), default=True)
    purchase = db.relationship('Purchase', backref='purchase', lazy=True)

    def change_description(self, new_desc):
        self.description = new_desc

    @property
    def available_quantity(self):
        return self.quantity

# Purchase database model design
class Purchase(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id'))
    product_name = db.Column(db.String(20), nullable=False)
    product_category = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    owner_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    owner_name = db.Column(db.String(80), nullable=False)
    delivered = db.Column(db.Boolean, nullable=False)
    purchase_date = db.Column(db.DateTime(), default=datetime.now()) # This line should be fixed because not sure it will work

    # def add_purchase(self, product_id, product_name, product_category, quantity, owner_id, delivered=False):
    #     self.owner_id = owner_id
    #     self.product_id = product_id
    #     self.product_name = product_name
    #     self.product_category = product_category
    #     self.quantity = quantity
    #     self.delivered = delivered
    def deliver(self):
        self.delivered = True
    def undo_deliverance(self):
        self.delivered = False
