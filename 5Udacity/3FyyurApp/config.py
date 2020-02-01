import os


SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://johnpicasso@localhost:5432/fyyurapp'

# Connect to the database

