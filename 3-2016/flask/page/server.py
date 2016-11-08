from flask import Flask,render_template,request,abort,redirect,url_for
from flask.ext.pymongo import PyMongo
from models import Noticia, Categoria, Imagen
from datetime import date

app = Flask("diario_deportivo")
mongo = PyMongo(app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


def f(x):
    categoria = mongo.db.categorias.find_one({"_id":x["categoria"]})
    x["categoria"] = categoria
    return x

@app.route("/")
def index():
    categorias = mongo.db.categorias.find()
    noticias =  mongo.db.noticias.find().sort("_id",-1)
    noticias = map(f, noticias)
    return render_template('index.html',noticias=noticias,categorias=categorias)

@app.route("/admin")
def admin():
    categorias = mongo.db.categorias.find()
    categorias = map (lambda x: x,categorias)
    return render_template('admin.html',categorias=categorias)

@app.route("/noticias/<categoria_nombre>")
def noticias(categoria_nombre):
    categoria = Categoria(**mongo.db.categorias.find_one_or_404({"nombre":categoria_nombre}))
    noticias = mongo.db.noticias.find({"categoria":categoria._id}).sort("_id",-1)
    categorias = mongo.db.categorias.find()
    return render_template('noticias.html',categorias=categorias,noticias=noticias,categoria_nombre=categoria_nombre)

@app.route("/alta",methods=['POST','GET'])
def alta_noticia():
    
    if request.method == 'POST':
        
        categoria = Categoria(**mongo.db.categorias.find_one_or_404({"nombre":request.form["categoria"]}))
        fecha = date.today().isoformat()
        noticia = Noticia(request.form["titulo"],request.form["copete"],request.form["cuerpo"],categoria._id,fecha)
        mongo.db.noticias.insert_one(noticia.__dict__)
        return redirect(url_for("index"))

    else:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)