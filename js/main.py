from flask import Blueprint, render_template

js = Blueprint('js', __name__, template_folder='templates')

@js.route('/')
def home():
    title = "100 Componentes Con Js"
    return render_template('HomeJs.html', title=title)
