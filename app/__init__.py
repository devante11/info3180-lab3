from flask import Flask
from flask_mail import Mail 
from .config import Config

app = Flask(__name__)
app.config.from_obeject(Config)


mail = Mail(app)
from app import views