from wtforms import TextField
from flask_wtf import FlaskForm

class UrlInput(FlaskForm):
    Urlinp = TextField()