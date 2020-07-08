from flask import Flask, send_file, Response
app = Flask(__name__)

PATH = "file.txt"

@app.route('/api/not-working')
def not_working():
    handle = open(PATH, 'r')
    data = handle.readlines()
    return data

@app.route('/api/working')
def working():
    return send_file(PATH)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
