from flask import Flask, render_template, request, redirect
import json


app = Flask(__name__)

@app.route('/')
def home():
    with open('mejora.json') as json_file:
        mejoras = json.load(json_file)

    return render_template('home.html', mejoras=mejoras)


@app.route('/fnaf')
def fnaf():
    title = "Fnaf Juegos"

    with open('juegos.json') as json_file:
        juegos = json.load(json_file)

    return render_template('fnaf.html', title=title, juegos=juegos)

@app.route('/subir')
def Subir():
    return render_template('subir.html')

@app.route('/subire', methods=["POST"])
def subire():

    with open('mejora.json', 'r') as file:
        jsonData = json.load(file)

    tipo = request.form["tipo"]
    title = request.form["SubTitle"]
    informacion = request.form["Info"]
    date = request.form["date"]

    new_data = {
    "title": tipo,
    "subtitle": title,
    "text": informacion,
    "footer": date
    
    }
    jsonData.append(new_data)

    with open('mejora.json', 'w') as file:
        json.dump(jsonData, file, indent=4)

    return redirect("/subir")

if __name__ == '__main__':
    app.run(debug=True)