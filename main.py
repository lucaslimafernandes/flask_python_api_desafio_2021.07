##Lucas Lima Fernandes

from flask import Flask, request, render_template
import simplejson
import mysql.connector

#Conexão com mysql
mydb = mysql.connector.connect(
  host="remotemysql.com",
  port='3306',
  database='njw4UldugD',
  user="njw4UldugD",
  password="J45m3E0rs2"
)

dbcursor = mydb.cursor(buffered=True)



def consulta(id_=False, key_='*'):
    """
    Função de SELECT
    args: 
        id_: default False, passar o id para busca no db
        key_: default '*', passar a coluna a ser buscada
    """

    lista = []

    if id_ == False:
        dbcursor.execute('SELECT COUNT(id) from products_base')
        count = dbcursor.fetchone()
        lista.append({'count':count[0]})
        dbcursor.execute('select * from products_base')
    else:
        dbcursor.execute(f'SELECT {key_} from products_base pb where id = {id_}')
    
    result = dbcursor.fetchall()
    try:
        for i in result:
            dic = {
                'id':i[0],
                'image':i[1],
                'name':i[2],
                'categories':i[3],
                'price':i[4],
                'brand':i[5]
            }
            lista.append(dic)
    except:
        for i in result:
            lista.append(dic := {f'{key_}':i[0]})
    return lista


def alterar(id_, alt):
    """
    Função de UPDATE
    args:
        id_: passar o id do item a ser alterado
        alt: passar um dicionário com as colunas(keys) e os novos valores(values)
    """

    for k,v in alt.items():
        dbcursor.execute(f"UPDATE products_base SET {k}='{v}' where id = {id_}")
        
        
def consulta_cat(where, value):
    """
    Função de SELECT pelas colunas brand, categories e name
    args:
        where: passar a coluna de busca
        value: passar o valor a ser buscado
        Obs.: value entre LIKE na consulta SQL
    """
    lista = []
    
    dbcursor.execute(f"SELECT * from products_base pb where {where} LIKE '%{value}%'")
    result = dbcursor.fetchall()
    try:
        for i in result:
            dic = {
                'id':i[0],
                'image':i[1],
                'name':i[2],
                'categories':i[3],
                'price':i[4],
                'brand':i[5]
            }
            lista.append(dic)
    except:
        for i in result:
            lista.append(dic := {f'{key_}':i[0]})
    return lista


##FLASK

app = Flask(__name__)
app.config["DEBUG"] = True


## ROTAS

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/consultaTodos/')
def consulta_todos():

    lista = consulta()
    return f'{simplejson.dumps(lista)}'


@app.route('/consulta/')
def consulta_cat_route():
    
    list_cat = []
    if request.args.get('categories'):
        list_cat.append('categories')
    
    if request.args.get('brand'):
        list_cat.append('brand')
    
    if request.args.get('name'):
        list_cat.append('name')
    
    if len(list_cat) == 1:
        lista = consulta_cat(list_cat[0], request.args.get(list_cat[0]))
        return f'{simplejson.dumps(lista)}'
    else:
        return 'Por gentileza, um paramêtro por vez!'
        

@app.route('/id/<id_>', methods=['GET', 'PATCH'])
def consulta_id(id_):
    if request.method == 'GET':
        lista = consulta(f'{id_}')
        return f'{simplejson.dumps(lista)}'

    elif request.method == 'PATCH':

        lista_keys = []
        dic_changes = {}
        if 'image' in request.headers:
            lista_keys.append('image')
        
        if 'name' in request.headers:
            lista_keys.append('name')
        
        if 'categories' in request.headers:
            lista_keys.append('categories')
        
        if 'price' in request.headers:
            lista_keys.append('price')
        
        if 'brand' in request.headers:
            lista_keys.append('brand')

        for i in lista_keys:
            dic_changes[i] = request.headers[f'{i}']

        alterar(id_, dic_changes)
        return f'{simplejson.dumps(200)}'


@app.route('/id/<id_>/<key_>')
def consulta_id_key(id_, key_):
    lista = consulta(f'{id_}', f'{key_}')
    return f'{simplejson.dumps(lista)}'
