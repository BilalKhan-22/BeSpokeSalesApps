import os
from flask import Flask, render_template, request, url_for, redirect
import datetime
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()

# #§  Products – Name, Manufacturer, Style, Purchase Price, Sale Price, Qty On Hand, Commission Percentage

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    style = db.Column(db.String(80), unique=True, nullable=False)
    purchase_price = db.Column(db.Float)
    sale_price = db.Column(db.Float)
    qty_on_hand = db.Column(db.Integer)
    commission_percentage = db.Column(db.Float)

    def __repr__(self):
        return f'<Product {self.name}>'

# §  Salesperson – First Name, Last Name, Address, Phone, Start Date, Termination Date, Manager

class Salesperson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String)
    # start_date = db.Column(db.DateTime)
    start_date = db.Column(db.String(100))
    termination_date = db.Column(db.String(100))
    manager = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return f'<Salesperson {self.first_name}>'


# §  Customer – First Name, Last Name, Address, Phone, Start Date(what is a start date for a customer?)

# class Customer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(100), nullable=False)
#     lastname = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(80), unique=True, nullable=False)
#     age = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime(timezone=True),
#                         server_default=func.now())
#     bio = db.Column(db.Text)

#     def __repr__(self):
#     return f'<Student {self.firstname}>'


# §  Sales – Product, Salesperson, Customer, Sales Date 

# class Sales(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(100), nullable=False)
#     lastname = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(80), unique=True, nullable=False)
#     age = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime(timezone=True),
#                         server_default=func.now())
#     bio = db.Column(db.Text)

#     def __repr__(self):
#     return f'<Student {self.firstname}>'


# §  Discount – Product, Begin Date, End Date, Discount Percentage

# class Discount(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(100), nullable=False)
#     lastname = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(80), unique=True, nullable=False)
#     age = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime(timezone=True),
#                         server_default=func.now())
#     bio = db.Column(db.Text)

#     def __repr__(self):
#     return f'<Student {self.firstname}>'


@app.route('/')
def products():
    products = Product.query.all()
    return render_template('index.html', products=products)


@app.route('/product/<int:product_id>/')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@app.route('/product/<int:product_id>/edit/', methods=('GET', 'POST'))
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        name = request.form['name']
        manufacturer = request.form['manufacturer']
        style = request.form['style']
        purchase_price = request.form['purchase_price']
        sale_price = request.form['sale_price']
        qty_on_hand = request.form['qty_on_hand']
        commission_percentage = request.form['commission_percentage']


        product.name = name
        product.manufacturer = manufacturer
        product.style = style
        product.purchase_price = purchase_price
        product.sale_price = sale_price
        product.qty_on_hand = qty_on_hand
        product.commission_percentage = commission_percentage


        #Is this supposed to be add or update?       
        db.session.add(product)
        db.session.commit()

        return redirect(url_for('products'))
    return render_template('edit_product.html', product=product)


@app.route('/salespersons/')
def salespersons():
    salespersons = Salesperson.query.all()
    return render_template('salespersons.html', salespersons=salespersons)


@app.route('/salesperson/<int:salesperson_id>/')
def salesperson(salesperson_id):
    print('HEREEE')
    salesperson = Salesperson.query.get_or_404(salesperson_id)
    print('HEREEE')
    return render_template('salesperson.html', salesperson=salesperson)


@app.route('/salesperson/<int:salesperson_id>/edit/', methods=('GET', 'POST'))
def edit_salesperson(salesperson_id):
    salesperson = Salesperson.query.get_or_404(salesperson_id)

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        address = request.form['address']
        phone = request.form['phone']
        start_date = request.form['start_date']
        termination_date = request.form['termination_date']
        manager = request.form['manager']


        salesperson.first_name = first_name
        salesperson.last_name = last_name
        salesperson.address = address
        salesperson.phone = phone
        salesperson.start_date = start_date
        salesperson.termination_date = termination_date
        salesperson.manager = manager


        #Is this supposed to be add or update?       
        db.session.add(salesperson)
        db.session.commit()

        return redirect(url_for('salespersons'))
    return render_template('edit_salesperson.html', salesperson=salesperson)


# @app.route('/create/', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         firstname = request.form['firstname']
#         lastname = request.form['lastname']
#         email = request.form['email']
#         age = int(request.form['age'])
#         bio = request.form['bio']
#         student = Student(firstname=firstname,
#                           lastname=lastname,
#                           email=email,
#                           age=age,
#                           bio=bio)
#         db.session.add(student)
#         db.session.commit()

#         return redirect(url_for('index'))

#     return render_template('create.html')

#     # ...


# @app.route('/<int:student_id>/edit/', methods=('GET', 'POST'))
# def edit(student_id):
#     student = Student.query.get_or_404(student_id)

#     if request.method == 'POST':
#         firstname = request.form['firstname']
#         lastname = request.form['lastname']
#         email = request.form['email']
#         age = int(request.form['age'])
#         bio = request.form['bio']

#         student.firstname = firstname
#         student.lastname = lastname
#         student.email = email
#         student.age = age
#         student.bio = bio

#         db.session.add(student)
#         db.session.commit()

#         return redirect(url_for('index'))

#     return render_template('edit.html', student=student)


# @app.post('/<int:student_id>/delete/')
# def delete(student_id):
#     student = Student.query.get_or_404(student_id)
#     db.session.delete(student)
#     db.session.commit()
#     return redirect(url_for('index'))