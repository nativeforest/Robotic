
import SimpleHTTPServer
import SocketServer
#my first edit
    
PORT = 8000
    
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler.extensions_map.update({'.webapp': 'application/x-web-app-manifest+json',});
 
httpd = SocketServer.TCPServer(("192.168.1.43", PORT), Handler)
#aqui va la direccion local, con el comando ifconfig la saca, 192.168.1.43:8000
print "Serving at port", PORT
httpd.serve_forever()
