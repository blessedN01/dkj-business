from dkj_business import app
from flask import render_template, redirect, url_for, flash
from dkj_business.models import Product, User, db
from dkj_business.forms import RegisterForm, LoginForm, ProductForm, ModifyProfileForm, ModifyPasswordForm
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename
import os, re
from dkj_business.helpers import *

login_manager = LoginManager(app)

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

def file_type_allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def validate_password(password):
    """Validate form.data strength."""
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r'\d', password):
        return "Password must contain at least one number."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character."
    return None  # Password is valid





@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('UserIndex', username=current_user.username))
    products = db.session.execute(db.select(Product)).scalars().all()
    # Implement summary requirements
    # Every things shold be implemented here
    return render_template("index.html", products=products)

@app.route('/dkj-business/<username>')
@login_required
def UserIndex(username):
    products = db.session.execute(db.select(Product)).scalars().all()
    return render_template("index.html", products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email==form.email.data)).scalar_one_or_none()
        if user:
            if user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for('index', username=current_user.username))
            else:
                flash('Wrong password. Please enter the correct password', category='danger')   
        flash(f'No user found', category='danger')   
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/register", methods=["GET", "POST"])
def register():
    # {{ form.hidden_tag() }}
    form =  RegisterForm()
    if form.validate_on_submit():
        user_exists = db.session.execute(db.select(User).where(User.email==form.email.data)).scalars()
        if not user_exists:
            flash('This email has been already used to create an accont. Please use another email', category='info')
            return render_template('register.html', form=form)
        passwordErrors = form.password.errors
        emailErrors = form.email.errors
        if passwordErrors:
            for error in passwordErrors:
                flash(error, category='danger')
            return render_template("register.html", form=form)
        elif emailErrors:
            for error in emailErrors:
                flash(error, category='danger')
            return render_template("register.html", form=form)
        file = form.profil_picture.data
        user = User(username=form.username.data, first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, phone=form.phone.data)
        if file and file_type_allowed(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            user.profil_picture = filename
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        if file:
            file.save(filepath)
        login_user(user)
        return redirect(url_for("UserIndex", username = current_user.username))
    return render_template("register.html", form=form)
    


# I have to handle this using javascript to display a pop-up that will allow to add product
@app.route("/<username>/add_products", methods=['GET', 'POST'])
@login_required
def add_product(username):
    form = ProductForm()
    if form.validate_on_submit():
        img = form.img.data
        name = form.name.data
        category = form.category.data
        price = form.price.data
        quantity = form.quantity.data
        description = form.description.data
        product = Product(product_name=name, owner_id=current_user.id, category=category, description=description, price=price, quantity=quantity)
        if img and file_type_allowed(img.filename):
            filename = secure_filename(img.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            product.img = filename
        else:
            flash('File error', category='danger')

        if img:
            img.save(filepath)
            
        db.session.add(product)
        db.session.commit()
        return render_template('products.html', product=product)
    return render_template('add_product.html', form=form, username=current_user.username)


@app.route("/myProducts")
@login_required
def myProducts():
    my_products = db.session.execute(db.select(Product).where(Product.owner_id==current_user.id)).scalars().all()
    return render_template('products.html', products=my_products)


@app.route('/profil', methods=['GET', 'POST'])
@login_required
def profil():
    return render_template('profil.html')

@app.route('/modifyProfil', methods=['GET', 'POST'])
@login_required
def modifyProfil():
    form = ModifyProfileForm()
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        price = form.price.data
        quantity = form.quantity.data
        description = form.description.data
        if current_user.check_password(form.password.data):
            flash('Password error!', category='danger')
            return render_template(url_for('profil'))
        product = Product(product_name=name, owner_id=current_user.id, category=category, description=description, price=price, quantity=quantity)
        return render_template(url_for('profil'), product=product)
    return render_template('modifyProfil.html', form=form)

@app.route('/modifyPassword', methods=['GET', 'POST'])
@login_required
def modifyPassword():
    form = ModifyPasswordForm()
    if form.validate_on_submit():
        current_user.set_password(form.new_password.data)
        db.session.commit()
        return redirect(url_for('modifyProfil'))
    return render_template('modifyPassword.html')
