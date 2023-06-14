#DEFINING THE BLUEPRINT
from flask import Blueprint, render_template


views = Blueprint('views', __name__)
# DEFINING THE BLUEPRINT FINISHED


@views.route('/')
def home():
    return "<h1> testing this out </h1>"
