from flask import Flask, redirect
from JUEGOS.main import jg
from js.main import js

app = Flask(__name__)


app.register_blueprint(jg, url_prefix='/juegos')
app.register_blueprint(js, url_prefix='/js')

@app.route('/')
def si():
    return redirect("/juegos/")

if __name__ == '__main__':
    app.run(debug=True)
