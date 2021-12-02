from flask import Flask, render_template,  request, redirect, url_for, flash, session
from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='gimnasio'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

                #RUTAS DE LOS DIFERENTES TEMPLATES

@app.route('/')
def Index():
    return render_template('index.html')

@app.route ("/rutinas/")
def rutinas():
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

@app.route("/terminosycondiciones/")
def terminosycondiciones():
    return render_template("terminosycondiciones.html")

@app.route('/agregar_rutina')
def agregar_rutina():
    return 'agregar_rutina'



                #DATA BASE

@app.route('/editar_rutina/<id>')
def editar_rutina(id):
    cur= mysql.connection.cursor()
    cur.execute('SELECT * From grupo_muscular WHERE id = %s', (id))
    datos = cur.fetchall()
    return render_template('editar',editor = datos[0])


@app.route('/eliminar_rutina/<string:id>')
def eliminar_rutina(id):
    cur= mysql.connection.cursor()
    cur.execute('DELETE FROM grupo_muscular WHERE id = {0}', format(id)) #Va borrar el ejercicio, hay q hacerle el boton
    mysql.connection.commit()
    flash('Ejercicio borrado correctamente')
    return redirect(url_for('rutinas'))#Cuando se borra vuelve al indice

@app.route('/update/<string:id>', methods = ['POST'])
def actualizar(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
    cur = mysql.connection.cursor()
    cur.exacute("""
    UPDATE ejercicio SET nombre_ejercicio = %s WHERE id = %s """,(nombre,id))
    flash('Ejercicio actualizado')
    return redirect(url_for(Index))






#Carga el template rutina.html
def main():
    if 'nombre' in session:
        return render_template('registro.html')

def inicio():

    if 'nombre' in session:
        return render_template('rutina.html')
    else:
        return render_template('registro.html')
    
#Carga el template rutina.html
def main():
    if 'nombre' in session:
        return render_template('registro.html')

def inicio():

    if 'nombre' in session:
        return render_template('rutina.html')
    else:
        return render_template('registro.html')
    

@app.route("/registrar", methods=['GET','POST'])
def registrar():
    if(request.method=="GET"):
        if 'nombre' in session:
            return render_template("ingresar.html")
        return render_template('inicio.html')
    else:
        user = request.form['n#NombreRegistro']
        email = request.form['nmEmailRegistro']
        contrasenia = request.form['nmContraseniaRegistro']

        #Preparo la Query para ingresar los datos

        SQuery ="INSERT into user (usuario, correo, contrasenia) VALUES (%s, %s, %s)"
        
        #Creo el cursor para que se ejecute

        cur = mysql.connection.cursor()

        #Ejecuto el commit

        mysql.connection.commit()

        #Registro la session
        session['nombre'] = user
        session['email'] = email 

        #Se dirige a index
        return redirect(url_for('inicio'))


#Defino la ruta de ingresar
@app.route("/ingresar", methods=["GET","POST"])

def ingresar():
    if(request.method == "GET"):
        if 'user' in session:
            return render_template('inicio.html')
        
        else:
            return render_template("ingresar.html")

    else:
        #obtengo los datos
        email = request.form['nmCorreoLogin']
        contrasenia = request.form['nmContrasenia']


        cur = mysql.connection.cursor()

        #Preparo la query

        sQuery = "SELECT email, contrasenia, usuario FROM user where email = %s"

        #Ejecuto la sentencia
        cur.exacute(sQuery,[email])

        #Obtengo el Dato

        user = cur.fetchone()

        #Cierro la consulta

        cur.close()




if __name__ == '__main__':
    app.run(port=3000, debug=True)






