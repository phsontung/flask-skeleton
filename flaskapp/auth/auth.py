from flask import (
    Blueprint, render_template, redirect, url_for, request, flash, jsonify
)
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_login import login_user, logout_user
from flask_mail import Message

from extensions import bcrypt
from extensions import db
from extensions import mail

from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # Validate credentials
    if not user or not bcrypt.check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # Reload page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('auth/signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:  # if a user is found, ask user try to sign up again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    pwhash = bcrypt.generate_password_hash(password)
    new_user = User(email=email, name=name, password=pwhash.decode('utf8'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/forgot-password')
def forgot_password():
    return render_template('auth/forgot.html')


@auth.route('/forgot-password', methods=['POST'])
def forgot_password_post():
    email = request.form.get('email')
    if not email:
        flash('Please input your email address.')
    else:
        user = User.query.filter_by(email=email).first()
        if not user:  # if a user is found, ask user try to sign up again
            flash('Please input correct email address.')
            return redirect(url_for('auth.forgot_password'))

        html_body = render_template('email/reset_password.html',
                                    username=user.name, reset_url='https://github.com/phsontung/flask-skeleton')
        msg = Message(subject='Reset your password',
                      sender='from@example.com',
                      html=html_body,
                      recipients=[email])
        mail.send(msg)
        flash('Email sent. Please check your email.')
    return redirect(url_for('auth.forgot_password'))  # Reload page


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


# Support another way (JWT) to call APIs to system
@auth.route('/jwt_create', methods=['POST'])
def jwt_create():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    # Validate credentials
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid username or password'}), 400
    else:
        jwt_token = create_access_token(identity=user.id)
        return jsonify(token=jwt_token), 200


@auth.route('/jwt_protected', methods=['GET'])
@jwt_required
def partially_protected():
    # If no JWT is sent in with the request, get_jwt_identity()
    # will return None
    current_user = get_jwt_identity()
    return jsonify(id=current_user), 200
