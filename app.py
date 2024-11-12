from flask import Flask,render_template,request
import socket
from flask import jsonify
from flask import Flask, send_from_directory, render_template, redirect
from flask_cors import CORS
import psycopg2
app = Flask(__name__)

CORS(app)
cors = CORS(app, resources={r"/retro*": {"origins": "*"}})


# #URL EXTERNA
# DATABASE_URL = 'postgres://dje:09bucZ8dC94FmlMXgHLsMqnD3llkkTDc@dpg-clu2q3q1hbls73e8rngg-a.oregon-postgres.render.com/portfolio_k8vd'

##URL INTERNA+
DATABASE_URL = 'postgres://dje:09bucZ8dC94FmlMXgHLsMqnD3llkkTDc@dpg-clu2q3q1hbls73e8rngg-a/portfolio_k8vd'

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT * FROM tbretroalimentacion")
rows = cur.fetchall()
for row in rows:
    print(row)

@app.route("/")
def index():
        return "INICIO DE LA APP FUNCIONA"
   
    
@app.route('/retro', methods=['POST'])
def create_user():
    data = request.json
    print(data['nombre'])
    idVar       =   '0'
    nombreVar   =   str(data['nombre'])
    consejoVar  =   str(data['consejo'])
    sql = """INSERT INTO tbretroalimentacion (id,nombreConsejero,consejo) VALUES ('"""+idVar+"""','"""+nombreVar+"""','"""+consejoVar+"""')"""
    cur.execute(sql)
    conn.commit()
    return jsonify(data)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
