
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, Response
import sys
sys.path.append("..")
import proxypy

app = Flask(__name__, static_folder='ui', static_url_path='')

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route("/rrserver/<path:path>")
def crossdom(path):
    proxiedReq = "url=http://recs.richrelevance.com/rrserver/{}?{}".format( path, request.query_string)
    reply = proxypy.get(proxiedReq)
    return Response(reply,status=200,mimetype='application/json')



if __name__ == '__main__':  # pragma: no cover
    app.debug = True
    app.run(port=8111)