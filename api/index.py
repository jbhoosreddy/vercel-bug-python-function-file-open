from flask import Flask, send_file
app = Flask(__name__)

PATH = "file.txt"

@app.route('/not-working')
def not_working():
    handle = open(PATH, 'r')
    data = handle.readlines()
    return data

@app.route('/working')
def working():
    send_file(PATH)
