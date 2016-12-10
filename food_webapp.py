# Imports
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
import sqlite3

# sqlite3 Configuaration
DATABASE = 'food_app.db'
DEBUG = True
SECRET_KEY = 'my_food_app'
USERNAME = 'food'
PASSWORD = 'food'

# Configure and initialize the app
app = Flask(__name__)
app.config.from_object(__name__)


if __name__ == "__main__":
	app.run()