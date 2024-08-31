from flask import Flask, render_template, redirect
from JUEGOS.main import jg
from PORTAFOLIO.main import pr

app = Flask(__name__)

app.register_blueprint(jg, url_prefix='/juegos')
app.register_blueprint(pr, url_prefix='/portafolio')

@app.route('/')
def si():
    return redirect("/juegos/")

if __name__ == '__main__':
    app.run(debug=True)
