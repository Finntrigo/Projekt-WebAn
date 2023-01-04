from flask import Flask
from flask import Blueprint, render_template, redirect, url_for, request, session
from views import views



app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.secret_key = 'key123'

if __name__ == '__main__':
    app.run(port=8000, debug=True)

