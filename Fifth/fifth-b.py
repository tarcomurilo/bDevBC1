import requests
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

def getdata(url):
    req = requests.get(url)
    dados = json.loads(req.text)
    return dados

url = 'https://jsonplaceholder.typicode.com/todos/'
dados = getdata(url)
print(dados[0])

hostName = "localhost"
serverPort = 8003

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(bytes("[", "utf-8"))

        vars = self.path
        vars = vars.replace("/",'')
        vars = vars.split('&')
        kvars = {}

        for var  in vars:
            tvar = var.split("=")
            if len(tvar) == 2:
                kvars[tvar[0]] = tvar[1]
        
        comma = False
        for dado in dados: 

            if kvars.get("completed") == "False":
                completedValue = False
            else:
                completedValue = True

            idValue = int(kvars.get("userId"))
            dadoComp = dado.get("completed")
            dadoId = dado.get("userId")
            
            if dadoComp == completedValue and idValue == dadoId:
                if comma == False:
                    comma = True
                else:
                    self.wfile.write(bytes(f', ', "utf-8"))
                
                print(completedValue, " = ", dadoComp, " - ", idValue, " = ", dadoId)
                self.wfile.write(bytes(f'{dado}', "utf-8"))

        self.wfile.write(bytes(f']', "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), Server)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")



