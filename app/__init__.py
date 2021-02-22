from flask import Flask
from flask_mail import Mail 
from .config import Config

app = Flask(__name__)
app.config.from_obeject(config)


mail = Mail(app)
from app import views