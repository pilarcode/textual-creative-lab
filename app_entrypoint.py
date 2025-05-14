from textual_serve.server import Server

server = Server(host="localhost",  port=8005, command="python app.py")
#server = Server(host="0.0.0.0",  port=8005, command="python app.py")
server.serve(debug=True)