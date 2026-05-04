from flask import Flask, render_template,request
import sqlite3
from helpers import global_sales,sales_year,sales_genre,total_genres,sales_name,compare_games


app = Flask(__name__)


def check_number(number):
    try:
        number=int(number)
        if number>0:
            return number
        else:
            return None
    except (ValueError,TypeError):
        return None


def correction(text):
    if not text:
        return""
    else:
        return text[0].upper() +text[1:].lower()#ou capitalize()



def erro(template,mensagem,**kwargs):
    return render_template(template,erro=mensagem,**kwargs)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/global",methods=["GET","POST"])
def vgglobal():
    if request.method=="GET":
        return render_template("vgglobal.html")
    else:
        qtd=check_number(request.form.get("quantidade"))
        if not qtd:
            return erro("vgglobal.html","Digite numeros inteiros e maiores que zero")
        

        jogos_global=global_sales(qtd)
        return render_template("vgglobal.html",jogos_global=jogos_global)

@app.route("/anos",methods=["GET","POST"])
def year():
    if request.method=="GET":
        return render_template("vgyear.html")
    else:
        ano=check_number(request.form.get("ano_selecionado"))
        qtd=check_number(request.form.get("quantidade"))
        if not ano or not qtd:
            return erro("vgyear.html","Digite numeros inteiros e maiores que zero")
        

        jogos_ano=sales_year(ano,qtd)
        return render_template("vgyear.html",jogos_ano=jogos_ano)

@app.route("/genero",methods=["GET","POST"])
def genre():
    generos_total=total_genres()
    if request.method=="GET":
        return render_template("genre.html",generos_total=generos_total)

    else:
        
        genre=correction(request.form.get("genero"))
        qtd=check_number(request.form.get("quantidade"))
        if not genre:
            return erro("genre.html","Digite um genero valido",generos_total=generos_total)
        elif genre not in generos_total:
            return erro("genre.html","Digite um genero valido",generos_total=generos_total)

        if not qtd:
            return erro("genre.html","Digite numeros inteiros e maiores que zero",generos_total=generos_total)

        jogos_genre=sales_genre(genre,qtd)
        return render_template("genre.html",generos_total=generos_total,jogos_genre=jogos_genre)

@app.route("/name",methods=["GET","POST"])
def name():
    if request.method=="GET":
        return render_template("vgname.html")
    else:
        name=request.form.get("name")
        if not name:
            return erro("vgname.html","Digite um nome para prosseguir")
        else:
            name=correction(name)
        
        procura=sales_name(name)
        if not procura:
            return erro("vgname.html","Não temos dados desse jogo, confira se ele esta escrito correto")
        else:
            return render_template("vgname.html", procura=procura)

@app.route("/compare",methods=["GET","POST"])
def compare():
    generos_total=total_genres()
    if request.method=="GET":
        return render_template("compare.html",generos_total=generos_total)
    else:
        qtd=request.form.get("quantidade")
        qtd=check_number(qtd)
        if not qtd:
             return erro("compare.html","Insira um numero para prosseguir",generos_total=generos_total)
        
        genre1s=(request.form.get("genre1")or "").strip()
        genre2s=(request.form.get("genre2")or "").strip()
        if not genre1s or not genre2s:
            return erro("compare.html","Insira 2 generos para prosseguir",generos_total=generos_total)
        
        genero1=correction(genre1s)
        genero2=correction(genre2s)

        if genero1 == genero2:
            return erro("compare.html","Os dois generos devem ser diferentes",generos_total=generos_total)

        gen1=compare_games(genero1,qtd)
        gen2=compare_games(genero2,qtd)
        if not gen1 or not gen2:
            return erro("compare.html","Não ha dados sobre um dos generos",generos_total=generos_total)

        return render_template("compare.html",gen1=gen1, gen2=gen2, genero1=genero1 , genero2=genero2  ,generos_total=generos_total)
        
        



if __name__ == "__main__":
    app.run(debug=True)