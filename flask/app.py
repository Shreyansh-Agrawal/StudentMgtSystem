from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)


def get_tables():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    connection.close()
    return tables

@app.route('/')
def home():
    return get_tables()


@app.route('/table/<string:table_name>')
def table(table_name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT * from {table_name}")
    data = cursor.fetchall()
    print(data)
    connection.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run()
