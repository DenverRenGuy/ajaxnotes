from flask import Flask, render_template, jsonify, request, redirect
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'notes')

@app.route('/')
def index():
    allQuery = 'SELECT * FROM notes'
    notes = mysql.query_db(allQuery)
    return render_template('index.html', notes=notes)

@app.route('/notes/add', methods=['POST'])
def addNote():

    d = request.form
    insertQuery = 'INSERT INTO notes(title, created_at) VALUES ("{}", NOW())'.format(d['title'])
    mysql.query_db(insertQuery)
    returnQuery = 'SELECT * FROM notes'
    notes = mysql.query_db(returnQuery)

    return jsonify(notes)

@app.route('/notes/delete/<id>', methods=['POST'])
def deleteNote(id):

    d = request.form
    deleteQuery = 'DELETE FROM notes WHERE id = :id'
    data = {
        'id': id
    }
    mysql.query_db(deleteQuery, data)

    return redirect('/')

@app.route('/notes/update/<id>', methods=['POST'])
def updateNote(id):
    d = request.form
    updateQuery = 'UPDATE notes SET title = :title, description = :description WHERE id = :id'
    data = {
        'title': d['title'],
        'description': d['description'],
        'id': id
    }
    mysql.query_db(updateQuery, data)
    return jsonify({"status": True})



app.run(debug=True)
