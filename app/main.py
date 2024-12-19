from flask import Flask
from app.routs.sql_queries_rout import sql_queries_bluprint

app = Flask(__name__)
app.register_blueprint(sql_queries_bluprint, url_prefix='/api/sql_queries')

if __name__ == '__main__':
    app.run()
