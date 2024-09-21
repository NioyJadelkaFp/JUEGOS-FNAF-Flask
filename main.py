from flask import Flask, render_template, request, redirect
import json

jg = Flask(__name__)

@jg.route('/')
@jg.route('/home')
def home():

    title = 'Home'
    with open('mejora.json') as json_file:
        mejoras = json.load(json_file)

    return render_template('home.html', mejoras=mejoras, title=title)

@jg.route('/fnaf')
def fnaf():
    title = "Fnaf Juegos"

    with open('juegos.json') as json_file:
        juegos = json.load(json_file)

    return render_template('fnaf.html', title=title, juegos=juegos)

@jg.route('/sincategorias')
def SinCar():
    title = "Sin Categoria"

    #with open('JUEGOS/juegos.json') as json_file:
        #juegos = json.load(json_file)

        #juegos=juegos

    return render_template('SinCaregoria.html', title=title)

@jg.route('/gameloft')
def gameold():
    title = "Juegos Old"

    with open('game.json') as json_file:
        juegos = json.load(json_file)

    return render_template('gameOld.html', title=title, juegos=juegos)

@jg.route('/subir')
def subir():
    return render_template('subir.html')

@jg.route('/subire', methods=["POST"])
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
    jg.run(debug=True)
