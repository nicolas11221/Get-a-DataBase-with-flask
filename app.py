
from flask import Flask, render_template, request, url_for, redirect, flash, jsonify

#Importamos La Base De Datos
from flask_mysqldb import MySQL

app = Flask(__name__)

#MySql Connection
#Importamos La Configuracion De MySql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_productos'
#Inicializamos La Configuracion De Bdd
mysql = MySQL(app)

app.secret_key = 'mysecreatkey'

#Aqui redireccionaremos el usuario y contraseña!
@app.route('/')
def index():
    return("HOLA")

# GET PRODUCTOS
@app.route('/getProducto')
def getProductos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos')
    data = cur.fetchall()
    print(data)
    return jsonify(data)

# GET UTILES ASEO
@app.route('/getUtiles')
def getUtiles():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM utiles_aseo')
    data = cur.fetchall()
    return jsonify(data)


if __name__ == '__main__':
    app.run(port = 8080 , debug = True)



    
# INSERT INTO `productos`(`id`, `nombre`, `stock`) VALUES 
# (1,'Harina',5000),(2,'Azucar',5000), (3,'Fideos',5000),(4,'Tallarines',5000),(5,'Arroz',5000),(6,'Bolsitas_Te',5000),(7,'Atun',5000),(8,'Aceite_Vegetal',5000),(9,'Salsa_De_Tomate',5000),(10,'Porotos',5000),(11,'Lentejas',5000),(12,'Garbanzos',5000),(13,'Leche_En_Polvo',5000),(14,'Jurel_Natural',5000),(15,'Sal',5000),(16,'Pure_De_Papas',5000),(17,'Mermelada',5000),(18,'Cesinas',5000),(19,'Pan_De_Molde',5000),(20,'Snaks',5000),(21,'Leche_Liquida',5000);

# INSERT INTO `utiles_aseo`(`id`, `nombre`, `stock`) VALUES 
# ('1','Jabon','5000'),('2','Shampoo','5000'),('3','Toalla_De_Cara','5000'),('4','Pack_Pasta_Dientes','5000'),('5','Cepillo_De_Dientes','5000'),('6','Peine','5000'),('7','Escobilla','5000'),('8','Esponja','5000'),('9','Talco','5000'),('10','Cortaunas','5000'),('11','Cloro','5000'),('12','Detergente_loza','5000'),('13','Detergente_Ropa','5000'),('14','Confort','5000'),('15','Lisoform','5000'),('16','Limpiapisos','5000'),('17','Toalla_Nova','5000'),('18','Poet','5000');