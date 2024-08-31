from flask import Blueprint

pr = Blueprint('pr', __name__, template_folder='PORTAFOLIO/templates')

@pr.route('/')
def home():
    return "Bienvenido a la sección de Portafolio"

@pr.route('/about')
def about():
    return "about"