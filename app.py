# coding: utf-8

from flask import Flask
from gear.db_config import mysql_db

app = Flask(__name__)
app.config.from_object('gear.config')


@app.before_request
def before_request():
    pass


@app.after_request
def after_request():
    pass


@app.teardown_request
def teardown_request():
    mysql_db.clear_transaction()


if __name__ == '__main__':
    app.run(port=5050, debug=True)
