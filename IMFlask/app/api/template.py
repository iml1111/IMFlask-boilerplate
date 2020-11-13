'''
Template API
'''
from flask import Blueprint, render_template
from app.api.decorators import timer

template = Blueprint('template', __name__)


@template.route("/")
def page():
	return render_template('index.html')


@template.route("/json")
def hello_json():
	from config import APP_NAME
	return {"APP_NAME": APP_NAME}