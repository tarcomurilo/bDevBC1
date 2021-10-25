from flask import Flask
from flask import request as flaskreq
import requests
import json

app = Flask(__name__)
port = 5600

def getdata(url):
    req = requests.get(url)
    dados = json.loads(req.text)
    return dados

url = 'https://jsonplaceholder.typicode.com/todos/'
dados = getdata(url)

@app.route("/")
def hello_world():

    if flaskreq.args.get('completed') == None or flaskreq.args.get('userId') == None:
        return '[]'

    if flaskreq.args.get('completed') == 'False' or flaskreq.args.get('completed') == 'false':
        completedValue = False
    else:
        completedValue = True

    userId = int(flaskreq.args.get('userId'))
 
    newDados = []

    for dado in dados:
        if dado['completed'] == completedValue and dado['userId'] == userId:
            newDados.append(dado)
    
    return str(newDados)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)