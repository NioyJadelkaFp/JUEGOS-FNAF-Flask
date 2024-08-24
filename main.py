from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
@app.route('/fnaf')
def home():
    title = "Fnaf Juegos"

    with open('juegos.json') as json_file:
        juegos = json.load(json_file)

    return render_template('home.html', title=title, juegos=juegos)

if __name__ == '__main__':
    app.run(debug=True)