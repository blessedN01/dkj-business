from dkj_business import app
from flask import render_template, redirect, request, url_for, flash
from dkj_business.models import Product, User, db
from dkj_business.forms import RegisterForm, LoginForm, ProductForm, ModifyProfileForm, ModifyPasswordForm
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename
import re, os

login_manager = LoginManager(app)

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int('user_id'))

def file_type_allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def validate_password(password):
    """Validate password strength."""
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
    products = db.session.execute(db.select(Product)).scalars
    # Implement summary requirements
    # Every things shold be implemented here
    return render_template("index.html", products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm
    if form.validate_on_submit:
        user = db.session.execute(db.select(User).where(email=form.email.data)).first()
        login_user(user)
        return redirect(url_for('/'))
    return render_template('/')
@app.route('/logout')
@login_required
def logout():
    logout_user(current_user)
    return redirect(url_for('/'))

@app.route("/register", methods=["GET", "POST"])
def register():
    # {{ form.hidden_tag() }}
    form =  RegisterForm()
    if form.validate_on_submit:
        error =validate_password(form.password.data)
        if error:
            flash(error, category='danger')
            return redirect(url_for('register'))
        file = form.profil_picture.data
        if file and file_type_allowed(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            filename = secure_filename(file.filename)
        user = User(username=form.username.data, email=form.email.data, profil_picture=filename, phone=form.phone.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        if file:
            file.save(filepath)
        return render_template(url_for("/"))
    return render_template(url_for("/"))
    


# I have to handle this using javascript to display a pop-up that will allow to add product
@app.route("/add_products", methods=['GET', 'POST'])
@login_required
def add_products():
    form = ProductForm()
    if form.validate_on_submit:
        name = form.name.data
        category = form.category.data
        price = form.price.data
        quantity = form.quantity.data
        description = form.description.data
        product = Product(product_name=name, owner_id=current_user.id, category=category, description=description, price=price, quantity=quantity)
        db.session.add(product)
        db.session.commit()
        return render_template('products.html', product=product)
    return render_template('add_products.html', form=form)

@login_required
@app.route("/myProducts")
def myProducts():
    my_products = db.execute(db.select(Product).where(owner_id=current_user.id)).scalars().all()
    return render_template('products.html', products=my_products)


@app.route('/profil', methods=['GET', 'POST'])
def profil():
    return render_template(url_for('profil.html'))

@app.route('/modifyProfil', methods=['GET', 'POST'])
@login_required
def modifyProfil():
    form = ModifyProfileForm()
    if form.validate_on_submit:
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
    if form.validate_on_submit:
        current_user.set_password(form.new_password.data)
        db.session.commit()
        return redirect(url_for('modifyProfil'))
    return render_template('modifyPassword.html')
