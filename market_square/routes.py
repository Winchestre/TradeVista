#!/usr/bin/env python3

import os
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify, send_from_directory, abort
from market_square import app
from market_square.forms import RegistrationForm, LoginForm, SellerLoginForm, ProductForm, ProfilePictureForm, ProductProfilePictureForm
from market_square.models import User, Product
from market_square import db
from flask_login import login_user, logout_user, login_required, current_user
from market_square.query_user import find_user_by_email
from werkzeug.utils import secure_filename
from datetime import datetime
import traceback

@app.route('/')
@app.route('/home')
def home_page():
    items = Product.query.filter_by(flash_sale=True)
    return render_template('home.html', items=items)

@app.route('/about')
def about_page():
    return "About Page"

@app.route('/market')
def market_page():
    return render_template('market.html')


@app.route('/public_shop')
def public_shop_page():
    return render_template('public_shop.html')


@app.route('/register', methods=['GET', 'POST'])
def registration_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_created = User(first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            username=form.username.data,
                            email_address=form.email_address.data,
                            password_hash=form.password1.data)
        db.session.add(user_created)
        db.session.commit()
        login_user(user_created)

        flash(f"Account created successfully! Welcome {user_created.first_name}", 'success')
        return redirect(url_for('market_page'))
    else:
        # Handle form validation errors
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, 'danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        # Redirect the authenticated user to another page, such as the shop page
        return redirect(url_for('market_page'))

    form = LoginForm()
    if form.validate_on_submit():
        user_to_login = User.query.filter_by(username=form.username.data).first()
        if user_to_login and user_to_login.check_password_correction(form.password.data):
            login_user(user_to_login)
            flash(f'You have been successfully logged in as: {user_to_login.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Incorrect username or password! Please try again', category='danger')
    return render_template('login.html', form=form)


@app.route('/seller_login', methods=['GET', 'POST'])
def seller_login_page():
    if current_user.is_authenticated:
        #flash('You are already logged in', category='info')
        # Redirect the authenticated user to another page, such as the shop page
        return redirect(url_for('shop_page', user_id=current_user.id))

    form = SellerLoginForm()
    if form.validate_on_submit():
        user_to_login = User.query.filter_by(username=form.username.data, id=form.user_id.data).first()
        if user_to_login and user_to_login.check_password_correction(form.password.data):
            login_user(user_to_login)
            flash(f'You have been successfully logged in as: {user_to_login.username}', category='success')
            return redirect(url_for('shop_page', user_id=user_to_login.id))
        else:
            flash('Incorrect username, user ID or password! Please try again', category='danger')
    return render_template('seller_login.html', form=form)


@app.route('/shop/<int:user_id>')
def shop_page(user_id):
    user = User.query.get(user_id)
    return render_template('shop.html', user=user)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))


@app.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product_name = form.product_name.data
        current_price = form.current_price.data
        previous_price = form.previous_price.data
        in_stock = form.in_stock.data
        flash_sale = form.flash_sale.data

        file = form.product_picture.data

        file_name = secure_filename(file.filename)

        file_path = f'./media/{file_name}'

        file.save(file_path)

        new_product = Product()
        new_product.product_name = product_name
        new_product.current_price = current_price
        new_product.previous_price = previous_price
        new_product.in_stock = in_stock
        new_product.flash_sale = flash_sale

        new_product.product_picture = file_path
        new_product.date_added = datetime.utcnow()
        owner_id=current_user.id
        
        try:
            db.session.add(new_product)
            db.session.commit()
            flash(f'{product_name} added Successfully', category='success')
            print('Product Added')
            return render_template('add_product.html', form=form)
        except Exception as e:
            print("Error:", e)
            traceback.print_exc()
            db.session.rollback()
            flash('Product Not Added!!', category='danger')
    
    return render_template('add_product.html', form=form)



@app.route('/product', methods=['GET', 'POST'])
@login_required
def product():
    items = Product.query.order_by(Product.date_added).all()
    return render_template('product.html', items=items)


@app.route('/view_products')
@login_required
def view_products():
    # Query products added by the current user
    products = Product.query.filter_by(owner_id=current_user.id).all()
    return render_template('view_product.html', items=products)

# @app.route('/product/<int:product_id>')
# @login_required
# def view_product(product_id):
#     product = Product.query.get_or_404(product_id)
#     # Check if the current user is the owner of the product
#     if current_user != product.owner:
#         abort(403)  # Forbidden error if the user is not the owner
#     # Render the product details template if the user is the owner
#     return render_template('view_product.html', product=product)


# @app.route('/product/<int:product_id>')
# @login_required
# def view_product(product_id):
#     product = Product.query.get(product_id)
#     if product is None:
#         abort(404)  # Product does not exist
#     if product.owner_id != current_user.id:
#         abort(403)  # User does not have permission to access this product
#     # Render template to display the product
#     return render_template('view_product.html', product=product)


@app.route('/media/<path:filename>')
def view_image(filename):
    return send_from_directory('../media', filename)


@app.route('/update_product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def update_item(product_id):
    form = ProductForm()
    product_to_update = Product.query.get(product_id)
    form.product_name.render_kw = {'placeholder': product_to_update.product_name}
    form.previous_price.render_kw = {'placeholder': product_to_update.previous_price}
    form.current_price.render_kw = {'placeholder': product_to_update.current_price}
    form.in_stock.render_kw = {'placeholder': product_to_update.in_stock}
    form.flash_sale.render_kw = {'placeholder': product_to_update.flash_sale}

    if form.validate_on_submit():
        product_name = form.product_name.data
        current_price = form.current_price.data
        previous_price = form.previous_price.data
        in_stock = form.in_stock.data
        flash_sale = form.flash_sale.data

        file = form.product_picture.data
        file_name = secure_filename(file.filename)
        file_path = f'./media/{file_name}'

        file.save(file_path)

        try:
            Product.query.filter_by(id=product_id).update(dict(product_name=product_name,
                                                                current_price=current_price,
                                                                previous_price=previous_price,
                                                                in_stock=in_stock,
                                                                flash_sale=flash_sale,
                                                                product_picture=file_path))

            db.session.commit()
            flash(f'{product_name} updated Successfully')
            print('Product Upadted')
            return redirect('/product')
        except Exception as e:
            print('Product not Upated', e)
            flash('Item Not Updated!!!')

    return render_template('update_product.html', form=form)


@app.route('/delete_product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def delete_product(product_id):
    try:
        product_to_delete = Product.query.get(product_id)
        db.session.delete(product_to_delete)
        db.session.commit()
        flash('One product deleted')
        return redirect('/product')
    except Exception as e:
        print('product not deleted', e)
        flash('product not deleted!!')
    return redirect('/product')


@app.route('/users')
@login_required
def users_page():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/search', methods=['GET', 'POST'])
def search_page():
    if request.method == 'GET':
        search_query = request.args.get('search')
        if search_query:
            items = Product.query.filter(Product.product_name.ilike(f'%{search_query}%')).all()
        else:
            items = []
        return render_template('search.html', items=items)

    elif request.method == 'POST':
        search_query = request.form.get('search')
        if search_query:
            items = Product.query.filter(Product.product_name.ilike(f'%{search_query}%')).all()
        else:
            items = []
        return render_template('search.html', items=items)

    # In case of any other HTTP methods, return an empty response or handle as needed
    return '', 405  # Method Not Allowed



@app.route('/profile', methods=['GET', 'POST'])  # Handle both GET and POST requests
@login_required
def profile():
    owner_id = current_user.id
    user = User.query.get_or_404(owner_id)
    form = ProfilePictureForm()  # Create an instance of the ProfilePictureForm

    if form.validate_on_submit():  # If the form is submitted
        if form.profile_picture.data:  # If a profile picture is uploaded
            file = form.profile_picture.data
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            current_user.profile_picture = file_path  # Update the user's profile picture field
            db.session.commit()
            flash('Profile picture uploaded successfully!', 'success')
            return redirect(url_for('profile', owner_id=user.id))  # Redirect to the profile page to display the updated picture

    # Render the profile template with the form and user information
    return render_template('profile.html', user=user, form=form)


@app.route('/product_owner_profile/<int:owner_id>', methods=['GET', 'POST'])
def product_owner_profile(owner_id):
    user = User.query.get_or_404(owner_id)
    form = ProductProfilePictureForm()

    return render_template('product_owner_profile.html', user=user, form=form)


# @app.route('/product_owner_profile/<string:username>', methods=['GET', 'POST'])
# def product_owner_profile(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     form = ProductProfilePictureForm()

#     return render_template('product_owner_profile.html', user=user, form=form)
