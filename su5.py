#!/usr/bin/python3
#-*- coding: UTF-8 -*-
# version 3.4 local server call 212.109.192.73:8888/
from urllib.parse import unquote
import socketserver, time  # получить серверы сокетов, объекты-обработчики
def now():
    return time.ctime(time.time())
myHost = '212.109.192.73'
#myHost = ''
# компьютер-сервер, '' означает локальный хост
myPort =8888
datapop=''
iii=0
# использовать незарезервированный номер порта
status="200 OK"
typ="text/html; charset=utf-8"
lt0="""
<tt>
"""
lt1="""
</tt>
"""
ltz='| * '
ltp='| . '
ltd='|___'
ltf='____'
lte='|'
ll1="""
<!DOCTYPE HTML>
<html>
<head>
<meta content="text/html; charset="utf-8" size=\"20\">
</head>

"""
ll2="""
<p>
  LL1 Введите координаты через точку - например,  5.10   - и нажмите ENTER!
 </body>
</html>
"""
lq1="""
<!DOCTYPE HTML>
<html>
<head>
<meta content="text/html; charset="utf-8" size=\"20\">
<title>Обработка данных форм</title>
 </head>
 <body>
  <form action=\"\" METHOD=\"get\">"""
lq2="""
<br/>Введите   <p><label for=\"name\">Имя <em>*</em></label><input type=\"text\" size=\"20\" maxlength=\"5\" name=\"name\"></p>
   <p><button  formtarget=\"output\">Отправить</button></p>
  </form>
 LQ2 Введите координаты через точку - например,  5.10   - и нажмите ENTER!
 </body>
</html>
"""
splay="""
<!DOCTYPE html>
<html>
	<head><meta charset="utf-8"></head>
<form action=\"\" METHOD=\"get\">
   <p><button  formtarget="output">Отправить</button></p>
  </form>
</body>
</html>

"""
class MyClientHandler(socketserver.BaseRequestHandler):
    mycli=[]
    def handle(self):
        def sendsquare():   #----output ---square field -----
            coords=[]
            dd=''
            for sj in MyClientHandler.mycli:
                sja=sj.split()
                if len(sja)==2:
                    sdigits_and_point=sja[1]
                    if sdigits_and_point.count('.')==1:
                        pp=sdigits_and_point.index('.')
                        xcoor=int(sdigits_and_point[:pp])
                        ycoor=int(sdigits_and_point[pp+1:])
                        coords.append([sja[0],xcoor,ycoor])
#                        print(coords)
                else:
                    print(sj,'not coords')
                    continue
            if len(coords)>0:
                scoord=''
                sp=''
                sp0=''
                for i in range(1,11):
                    scoord=''
                    sp=''
                    sp0+=ltf
                    for j in range(1,11):
                        sp+=ltd
                        sco=ltp
                        for aurl,cx,cy in coords:
                            if cx==j and cy==i:
                                sco=ltz
                        scoord+=sco
#-------------------------------------------dd - output ---------
                    dd+=scoord+lte+'<br/>\n'+sp+lte+'<br/>\n'
#                print(dd)
                return '<tt>'+'<b>'+sp0+'<br/>'+dd+'</b></tt>'
#-----------------------------------------------------------------
        global lq1,lq2,ll1,ll2,mycli,stopyes
        dd=lq1+lq2
        coords=[]
# для каждого клиента
        print(self.client_address, now()) # показать адрес этого клиента
# имитировать блокирующие действия
        while True:
# self.request – сокет клиента
            data = self.request.recv(1024) # чтение, запись в сокет клиента          
            if not data: break        #    end of connection and handle!!!
            try:
#                print("request.recv(1024)")
                datastr=data.decode('utf-8') # fOArom byte coding to str
            except:
                break
#          ===      datastr='GET \?1 qqq kkkkk kklll kkkkkk' # put standard data if it is strange!!!
            if datastr[0:3]=='GET':      # GET - standard answer from browser, used form 'submite'
#                print('get=',datastr.split())
                try:
                    csc=datastr.split()[1][0:]  # GET - submite answer ,csc = text in ....?name=PETR
                except:
                    print(csc,'=short data! datastr.split()[1][4:]')   #no success... Why?!..........
                    break
                if  not csc.find('favicon.ico')==-1:        #not normal answer, often spam from browser...
                    print('favicon.ico!!!!!!!!!!!!!!!!=',csc.find('favicon.ico'))
                    break
                else:
                    lename=csc.find('?name=')
                    dd=lq1+lq2
                    if lename>0:
#                       secondcall
                        datapop=csc[lename+6:]
                        if datapop=="play" or datapop=='PLAY':
                            dd=splay
                        elif datapop=="stop" or datapop=='Stop':
                            stopyes=1
                            self.server.shutdown()
                        else:
#                            dd=ll1+datapop+' = '+str(MyClientHandler.mycli)+' use_play '+ll2
                            dd=ll1+datapop+'=? use_play or stop'+ll2
            else:     #  else is case not normal first question from client, but it is DATA!!!
#                     firstcall
                dd=lq1+lq2
#         ====   end if  datastr='GET \?1 qqq kkkkk kklll kkkkkk'
# put standard data if it is strange!!!
            if True:           
                try:
                    ddt=str(dd).encode('utf-8')   # from byte coding to str
                except:
                    print('errrrrrrrrrrrrrrrrrr',dd)
                    break
                try:
#                    print('sending answer dd=',dd )
                    self.request.send(b"HTTP/1.1 " + status .encode("utf-8") + b"\r\n")
                    self.request.send(b"Content-Type: text/html; charset=utf-8\r\n\r\n")
                    self.request.sendall(ddt)
                    MyClientHandler.mycli.append(self.client_address[0]+' '+datapop)
                    ddt1=str(lq1+sendsquare()+lq2).encode('utf-8')  # from byte coding to str
#                    self.request.send(b"HTTP/1.1 " + status .encode("utf-8") + b"\r\n")
#                    self.request.send(b"Content-Type: text/html; charset=utf-8\r\n\r\n")
                    self.request.sendall(ddt1)
                except:
                    break
#          end of WHILE!!! - next чтение, запись в сокет клиента but socket is the same
#        print(MyClientHandler.mycli,'mycli')
        self.request.close()    #  next request, but socket is the same
# создать сервер с поддержкой многопоточной модели выполнения,
# слушать/обслуживать клиентов непрерывно
stopyes=0
myaddr = (myHost, myPort)
server = socketserver.ThreadingTCPServer(myaddr, MyClientHandler)
dd=lq1+lq2
if stopyes==1:exit(0)
server.serve_forever()

