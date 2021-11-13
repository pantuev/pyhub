from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
from sssimp1 import *
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # определяем метод `do_GET` 
    def do_GET(self):
        global i,v
        self.send_response(200)
        self.end_headers()
        aa=self.requestline
        print(urllib.parse.unquote(aa[6:-15]))
        aaa=urllib.parse.unquote(aa[6:-15])
        if aaa!='avic':
            print(i,aaa)
            v.append(aaa)
            a=aaa1+aaa+aaa2
            a=''
            i+=1
            if i%4==0:
                for k in range(i):
                    a=a+v[k]
                a=aaa1+a+aaa2
                v=[]
                i=0
            self.wfile.write(a.encode('utf-8'))
i=1
v=['1']
httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
#https://docs-python.ru/standart-library/modul-http-server-python/
