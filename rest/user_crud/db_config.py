from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configuration
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Dooste,2004'
app.config['MYSQL_DATABASE_DB'] = 'roytuts'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
