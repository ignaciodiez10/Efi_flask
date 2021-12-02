from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route("/template/")
def home():
    return render_template ("index.html")

@app.route ("/rutinas/")
def Rutinas():
    return render_template ("rutinas.html")

@app.route("/brazo/")
def brazo():
    return render_template("brazo.html")

@app.route("/piernas/")
def piernas():
    return render_template("piernas.html")

@app.route("/espalda/")
def espalda():
    return render_template("espalda.html")

@app.route("/pecho/")
def pecho():
    return render_template("pecho.html")

@app.route("/aerobico/")
def aerobico():
    return render_template("aerobico.html")

if __name__ == '__main__':
    app.run(debug=True)