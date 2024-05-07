from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/QuienSomos")
def QuienSomos():
    return render_template("QuienesSomos-copy.html")

@app.route("/Sugerencias", methods=['POST','GET'])
def Sugerencias():
    if request.method == 'GET':
        nombre = request.args.get('Nombre')
        correo = request.args.get('Correo')
        asunto = request.args.get('Asunto')
        mensaje = request.args.get('Mensaje')

        if all([nombre, correo, asunto, mensaje]):
            con = sqlite3.connect("db.sqlite")
            con.execute("""INSERT INTO Sugerencias (name , email, asunto, mensaje)
                          VALUES (?, ?, ?, ?)""", (nombre, correo, asunto, mensaje))
            con.commit()
            con.close()
            return redirect(url_for("Sugerencias"))


    return render_template("Sugerencias.html")

@app.route("/VerSugerencias")
def VerSugerencias():
    con = sqlite3.connect("db.sqlite")
    c = con.cursor()
    c.execute("SELECT * FROM Sugerencias ORDER BY id DESC")
    sugerencias = c.fetchall()

    con.close()
    return render_template("VerSugerencias.html", sugerencias=sugerencias)

@app.route("/Facultades")
def Facultades():
    return render_template("Facultades.html")



@app.route("/Facultades/FACDYC")
def FACDYC():
    return render_template("facu/FacuFACDYC.html")

@app.route("/Facultades/FARQ")
def FARQ():
    return render_template("facu/FacuFARQ.html")

@app.route("/Facultades/FCB")
def FCB():
    return render_template("facu/FacuFCB.html")

@app.route("/Facultades/FCFM")
def FCFM():
    return render_template("facu/FacuFCFM.html")

@app.route("/Facultades/FCQ")
def FCQ():
    return render_template("facu/FacuFCQ.html")

@app.route("/Facultades/FFYL")
def FFYL():
    return render_template("facu/FacuFFYL.html")

@app.route("/Facultades/FIC")
def FIC():
    return render_template("facu/FacuFIC.html")

@app.route("/Facultades/FIME")
def FIME():
    return render_template("facu/FacuFIME.html")

@app.route("/Facultades/FOD")
def FOD():
    return render_template("facu/FacuFOD.html")

@app.route("/Facultades/FTSYDH")
def FTSYDH():
    return render_template("facu/FacuFTSYDH.html")
