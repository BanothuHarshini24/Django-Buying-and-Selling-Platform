

# Django-Buying-and-Selling-Platform

This is a selling and buying platform developed using the Django web framework.

# Features

1. Browse products by category
2. Search products by name or description
3. Sort products according to price, and the latest
4. Add products to the wishlist, cart
5. Complete a checkout process
6. View order history, your sales
7. Manage products, orders, and customers database in the admin panel

# Getting started
*Prerequisites* 

1.Python
2.Django
3.Postgresql
4.PgAdmin

# Installation

*Clone the repository

$ git clone https://github.com/BanothuHarshini24/Django-Buying-and-Selling-Platform
$ cd Django-Buying-and-Selling-Platform
 
*Create a virtual environment

$ pip install virtualenv
$ virtualenv env

# Activating the environment

On Windows:
env\Scripts\activate

on Mac OS / Linux:
$ source env/bin/activate

# Installing dependencies:

$ pip install -r requirements.txt4

# Create a PostgreSQL database and user:

sudo -u postgres psql
CREATE DATABASE ecommerce;
CREATE USER ecommerce_user WITH PASSWORD 'ecommerce_password';
ALTER ROLE ecommerce_user SET client_encoding TO 'utf8';
ALTER ROLE ecommerce_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE ecommerce_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE ecommerce TO ecommerce_user;

# Last commands to start:
$ python manage.py makemigrations

$ python manage.py migrate

# Create a super user:
$ python manage.py createsuperuser admin-name

# Run Server:
$ python manage.py runserver
Access the website at: http://127.0.0.1:8000/
