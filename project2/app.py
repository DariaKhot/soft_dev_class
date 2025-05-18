# Import required libraries and modules
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

def inject_datetime():
    return {'datetime': datetime}

# Initialize the Flask application
app = Flask(__name__)

# Configure database URI and other settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Daria1703@localhost/skincare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Define the User model/table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200))
    orders = db.relationship('Order', backref='user', lazy=True)  # One-to-many relationship with orders

# Define the Product model/table
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    category = db.Column(db.String(50))
    image_filename = db.Column(db.String(100))

# Define the Order model/table
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.Column(db.Text)  # Stored as JSON
    total_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Home page that displays all unique product categories
@app.route('/')
def index():
    categories = list(set([p.category for p in Product.query.all()]))
    return render_template('index.html', categories=categories)

# Page that shows products under a specific category
@app.route('/category/<string:category>')
def show_category(category):
    products = Product.query.filter_by(category=category).all()
    return render_template('category.html', products=products, category=category)

# Add a product to the shopping cart
@app.route('/add_to_cart/<int:product_id>', methods=['GET'])
def add_to_cart(product_id):
    quantity = int(request.args.get(f'quantity_{product_id}', 1))
    cart = session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + quantity
    session['cart'] = cart
    return redirect(url_for('cart'))


# Display the shopping cart with totals and fees
@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart.items():
        product = Product.query.get(int(pid))
        items.append({'product': product, 'quantity': qty})
        total += product.price * qty
    tax = round(total * 0.1, 2)  # 10% tax
    shipping = 5.00  # flat shipping fee
    grand_total = total + tax + shipping
    return render_template('cart.html', items=items, total=total, tax=tax, shipping=shipping, grand_total=grand_total)

# Remove an item from the shopping cart
@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    cart.pop(str(product_id), None)
    session['cart'] = cart
    return redirect(url_for('cart'))

# User registration form and logic
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Check for duplicate username or email
        if User.query.filter_by(username=request.form['username']).first() or User.query.filter_by(email=request.form['email']).first():
            flash("Username or Email already taken.")
            return redirect(url_for('register'))

        # Create and save new user
        user = User(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            username=request.form['username'],
            password=request.form['password'],
            email=request.form['email'],
            address=request.form['address']
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# User login form and logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if user:
            session['user_id'] = user.id  # Store logged-in user's ID
            return redirect(url_for('checkout'))
        flash("Invalid credentials")
    return render_template('login.html')

# Checkout page that processes the order
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cart = session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart.items():
        product = Product.query.get(int(pid))
        items.append({'id': product.id, 'name': product.name, 'quantity': qty, 'price': product.price})
        total += product.price * qty

    tax = round(total * 0.1, 2)
    shipping = 5.00
    grand_total = total + tax + shipping

    # If order is submitted
    if request.method == 'POST':
        order = Order(
            user_id=session['user_id'],
            items=json.dumps(items),
            total_price=grand_total
        )
        db.session.add(order)
        db.session.commit()
        session.pop('cart', None)
        return redirect(url_for('order_complete', order_id=order.id))

    return render_template('checkout.html', items=items, total=total, tax=tax, shipping=shipping, grand_total=grand_total)

# Confirmation page after order submission
@app.route('/order_complete/<int:order_id>')
def order_complete(order_id):
    return render_template('order_complete.html', order_id=order_id)

# Run the app and create tables
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
