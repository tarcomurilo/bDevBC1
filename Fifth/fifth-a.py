from flask import json
import requests
import json

url = 'https://jsonplaceholder.typicode.com/todos/'
req = requests.get(url)

dados = json.loads(req.text)

print(f'Printing {url}')
for dado in dados:
    if dado["completed"]==True:
        print(dado)

