import sqlite3

def total_genres():
    db = sqlite3.connect("jogos.db")
    distinct=db.execute("SELECT DISTINCT genre FROM jogos").fetchall()
    db.close()
    return [i[0] for i in distinct]


def global_sales(quantidade):
    db = sqlite3.connect("jogos.db")
    names = db.execute("SELECT name, global_sales FROM jogos ORDER BY global_sales DESC LIMIT ?",(quantidade,)).fetchall()
    db.close()
    return names
    

def sales_year(ano,qtd):
    db=sqlite3.connect("jogos.db")
    ano_escolhido=db.execute("SELECT name,global_sales FROM jogos WHERE year=? ORDER BY global_sales DESC LIMIT ?",(ano,qtd),).fetchall()
    db.close()
    return ano_escolhido
    
def sales_genre(genero,qtd):
    db=sqlite3.connect("jogos.db")
    genero=db.execute("SELECT name,global_sales FROM jogos WHERE genre=? ORDER BY global_sales DESC LIMIT (?)",(genero,qtd),).fetchall()
    db.close()
    return genero
    
def sales_name(name):
    db=sqlite3.connect("jogos.db")
    nome=db.execute("SELECT name,platform,genre,publisher,year,global_sales FROM jogos WHERE name LIKE ?",(f"%{name}%",)).fetchall()
    db.close()
    return nome
        
def compare_games(genero,qtd):
    db=sqlite3.connect("jogos.db")
    jogos=db.execute("SELECT name FROM jogos WHERE genre=? ORDER BY global_sales DESC LIMIT ?",(genero,qtd),).fetchall()
    db.close()
    return [jogo[0] for jogo in jogos]
    
        
    


    

