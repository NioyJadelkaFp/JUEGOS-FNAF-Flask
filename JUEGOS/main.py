from flask import Blueprint, render_template, request, redirect
import json

jg = Blueprint('jg', __name__, template_folder='JUEGOS/templates')

@jg.route('/')
def home():
    with open('JUEGOS/mejora.json') as json_file:
        mejoras = json.load(json_file)

    return render_template('home.html', mejoras=mejoras)

@jg.route('/fnaf')
def fnaf():
    title = "Fnaf Juegos"

    with open('JUEGOS/juegos.json') as json_file:
        juegos = json.load(json_file)

    return render_template('fnaf.html', title=title, juegos=juegos)

@jg.route('/subir')
def subir():
    return render_template('subir.html')

@jg.route('/subire', methods=["POST"])
def subire():
    with open('JUEGOS/mejora.json', 'r') as file:
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

    with open('JUEGOS/mejora.json', 'w') as file:
        json.dump(jsonData, file, indent=4)

    return redirect("/subir")