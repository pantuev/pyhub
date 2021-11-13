from urllib.parse import unquote
import socketserver, time  # получить серверы сокетов, объекты-обработчики
def now():
    return time.ctime(time.time())
myHost = '212.109.192.73'
# компьютер-сервер, '' означает локальный хост
myPort =8888
datapop=''
iii=0
# использовать незарезервированный номер порта
status="200 OK"
typ="text/html; charset=utf-8"
ll1="""
<!DOCTYPE HTML>
<html>
<head>
<meta content="text/html; charset="utf-8">
</head>
<body>
<h1>
"""
ll2="""
</h1>
 </body>
</html>
"""
lq1="""
<!DOCTYPE HTML>
<html>
<head>
<meta content="text/html; charset="utf-8">
<title>Обработка данных форм</title>
 </head>
 <body>
  <form action=\""""
lq2="""\" METHOD="get">
<br/>Введите   <p><label for="name">Имя <em>*</em></label><input type="text" name="name"></p>
  </form>
 </body>
</html>
"""
splay="""
<!DOCTYPE html>
<html>
	<head>
		<title>УЮТНЫЙ ЛАБИРИНТ ДЛЯ ЧЕРЕПАХИ</title>
<p>Сделайте черепахе самые длинные лабиринты, какие сможете!!!!</p>
<canvas width="530" height="380"></canvas>
<script>
//==============================================================
//7X7==30 6x6==22  5x5==16  8X8==36 9X9==44 10X10==60 11X11==72 
//
//
//=================================================================
function lab1view(){
 cx.fillStyle = "black";
 cx.font = "20px Georgia";
canvas.width = canvas.width;
for(var i=0;i<14;i++){for(var j=0;j<14;j++){l=lab1[i][j];
tx=i*sizeofcell*2+sizeofcell+10*coeffsize;
ty=j*sizeofcell+sizeofcell+10*coeffsize;
ngx=tx.toString();
ngy=ty.toString();
nb=l.toString();
cx.strokeText(nb, tx,  ty);
;}}
}
//============================================================
function labview(){
 cx.fillStyle = "black";
 cx.font = "20px Georgia";
canvas.width = canvas.width;
for(var i=0;i<14;i++){for(var j=0;j<14;j++){l=lab[i][j];
tx=i*sizeofcell*2+sizeofcell+10*coeffsize;
ty=j*sizeofcell+sizeofcell+10*coeffsize;
ngx=tx.toString();
ngy=ty.toString();
nb=l.toString();
cx.strokeText(nb, tx,  ty);
;}}
}
//========================================================
function lab1copy(){
//alert('oooooooooooooooooooooooooooooooo');
     //   bez ogranichenija granici voobsche poka!!!
for(var i=0;i<14;i++){for(var j=0;j<14;j++){lab1[i][j]=lab[i][j];}}
}
//======================================================
function voln(){
     //   volnovoj algoritm s dopolneniem - bez ogranichenija granici voobsche poka!!!
//alert(n);
xt=0;
yt=0;
        cur=1;
        x=xt;
        y=yt;
        lab1[x][y]=cur;
       var ischange=1;

while(ischange>0)
 {cur=cur+1;
            ischange=0;

            for(x=0;x<n;x++)
    {
                for(y=0;y<n;y++)
      {

if(y+1<n){if(lab1[x][y+1]==0 && lab1[x][y]==(cur-1)){lab1[x][y+1]=cur;ischange=1;}}
if(x+1<n){if(lab1[x+1][y] == 0 && lab1[x][y]==cur-1){lab1[x+1][y]=cur;ischange=1;}}
if(x-1>-1){if(lab1[x-1][y] == 0 && lab1[x][y]==cur-1){lab1[x-1][y]=cur;ischange=1;}}
if(y-1>-1){if(lab1[x][y-1] == 0 && lab1[x][y]==cur-1){lab1[x][y-1]=cur;ischange=1;}}


      }
    }
}
}
//================================================================
function waywin(){
// obrabotka - puti po volnovomu algoritmu ! ! x0 y0-end poin
x0=n;y0=n;
putt=[];

        cur=lab1[x0][y0];
        x=x0;
        y=y0;
        while(cur-1>0){
         putt.push([x,y]);
cur=cur-1;s=0;
if(y<n && s<1){
//y+1
if(lab1[x][y+1] == cur){
y=y+1;s=1;
}
}
            if(x<n && s==0){
//x+1
if(lab1[x+1][y] == cur){x=x+1;s=1;
}
}
            if(x-1>-1 && s==0){
if(lab1[x-1][y] == cur){
x=x-1;s=1;
}
}
            if(y-1>-1 && s==0){
if(lab1[x][y-1] == cur){
y=y-1;s=1;
}
}
}
}
//======================================================================
function showputt(){
// putt to lab
var d;
for(d of putt){lab[d[0]][d[1]]=199;
nsteps=putt.length;
}
}
//------------------------------
function inilabs() {
for(var i=0;i<14;i++){for(var j=0;j<14;j++){lab1[i][j]=0;}}
for(var i=0;i<14;i++){for(var j=0;j<14;j++){lab[i][j]=0;}}
putt=[];
//
  }
//===================================================
function setka() {
//alert(lab);
nhod=1;
cx.fillStyle = "red";
  for ( x = 10; x < n*sizeofcell+11; x =x+ sizeofcell) {
 p=0;p=(x-10)/sizeofcell;
 tt=p; ttt=tt.toFixed(0); i=Number(ttt);
  for ( y = 10; y < n*sizeofcell+11; y =y+ sizeofcell) {
 p=0;p=(y-10)/sizeofcell;
tt=p; ttt=tt.toFixed(0); j=Number(ttt);
if(lab[i][j]>-0.5  ){
cx.fillStyle = "black";
if (lab[i][j]==199){cx.fillStyle = "blue";nhod=nhod+1;}
}else{
cx.fillStyle = "red";}
cx.fillRect(x, y, sizeofcell-5*coeffsize, sizeofcell-5*coeffsize);
  }
  }
for(var i=0;i<14;i++){for(var j=0;j<14;j++){if(lab[i][j]==199){lab[i][j]=0}}};
}
function ugli() {
     cx.fillStyle = "blue";
  cx.fillRect(10, 10, sizeofcell-5*coeffsize, sizeofcell-5*coeffsize);
     cx.fillStyle = "green";
 cx.fillRect( n*sizeofcell+10, n*sizeofcell+10, sizeofcell-5*coeffsize, sizeofcell-5*coeffsize);
}
//=============================================== switch off !!!------
function bukvi() {
cx.fillStyle = "black";
  cx.font = "20px Georgia";
  for (var x = 10; x < n*sizeofcell+11; x=x+ sizeofcell)    {
 p=0;p=(x-10)/sizeofcell;
 tt=p;var ttt=tt.toFixed(0);i=Number(ttt);
  for (var y = 30; y < (n+1)*sizeofcell+1; y =y+ sizeofcell) {
 p=0;p=(y-30)/sizeofcell;
 tt=p;var ttt=tt.toFixed(0);j=Number(ttt);
//if(lab[i][j]=199){
//cx.strokeText(g, x+5, y-3);}
 								}
  								}
		}
//--------------------------------------------
function bokovaja() {

nx=440;
nxw=477;
 for (var y = 10; y < (nn+2)*sizeofcell+11; y += sizeofcell) {cx.fillStyle = "green";
  cx.fillRect(nx, y, 3*(sizeofcell-5*coeffsize), sizeofcell-5*coeffsize);cx.fillStyle = "white";
cx.fillRect(nxw, y, 3*(sizeofcell-5*coeffsize), sizeofcell-5*coeffsize);
  }
}
//===========================================
function nomersboku() {
//     cx.fillStyle = "blue";
//  cx.fillRect(440, 240, sizeofcell-5*ncoeffsize, nsizeofcell-5*ncoeffsize);
     cx.fillStyle = "red";
 cx.fillRect( 440, 9*sizeofcell+11, 2*sizeofcell-5*coeffsize, 2*sizeofcell-5*coeffsize);
cx.fillStyle = "black";
  cx.font = "24px Georgia";
  for (var y = 30; y < (nn+3)*sizeofcell+1; y += sizeofcell) {
var ys=0;ys=(y-30)/sizeofcell +5;
ng=ys.toString();
nputt=nsteps.toString();
  cx.fillText(ng, nx+7, y-3);
  
    }
//cx.fillText('          ', nx+12, y+77);
  cx.font = "28px Georgia";
cx.fillText(nputt, nx+18, y+81);
}
// ------------------------------------------------
function nomeralone(xx,yy) {
 cx.fillStyle = "black";
 cx.font = "20px Georgia";var t=0.1;t=(yy-15)/sizeofcell;
var tt=t;var ttt=tt.toFixed(0);var tttt=Number(ttt);
n1=tttt%7+5;
// ====================  n  =======================
n=n1-1;
var nnn='0';nnn=n1.toString();
//+'* x='+tttt.toString()+' y='+yy.toString();
//  cx.fillText(yy%100, xx-xx%sizeofcell+sizeofcell+10*coeffsize, yy-yy%sizeofcell+sizeofcell-5*coeffsize);     
cx.strokeText(nnn, xx-xx%sizeofcell+sizeofcell+10*coeffsize, yy-yy%sizeofcell+sizeofcell-5*coeffsize);
	}
// ========================================== begin of programm ============
 var g='.';
var ng='..';
  var canvas = document.querySelector("canvas");
  var cx = canvas.getContext("2d");
nsteps=0;
lab1=[];for(var i=0;i<14;i++){a=[];for(var j=0;j<14;j++){a.push(0);}
lab1.push(a);}
putt=[];for(var i=0;i<14;i++){a=[];for(var j=0;j<14;j++){a.push(0);}
putt.push(a);}
lab=[];for(var i=0;i<14;i++){a=[];for(var j=0;j<14;j++){a.push(0);}
lab.push(a);}
var n1 = 12;
var n=n1-1;
var sizeofcell=400;
sizeofcell=sizeofcell/n1;var t=0.1;t=sizeofcell;
sizeofcell=Number(t.toFixed(0));
  var coeffsize=0;coeffsize=sizeofcell;
  var nn1 = 5;nn=nn1-1;
  var nsizeofcell=300;nsizeofcell=nsizeofcell/nn1;
  var ncoeffsize=0;ncoeffsize=nsizeofcell;
  ncoeffsize=ncoeffsize/40;
  coeffsize=coeffsize/40;
// alert(coeffsize+'----'+sizeofcell);
n=4;
inilabs();
//voln();
setka();
ugli();
//alert(lab);
bukvi();
//alert('lab');
bokovaja();
//alert('labw');
nomersboku();
nomeralone(470,30);
xt=0;
yt=0;
var yy0=30;
twoswitch=-1;
// ==============================!!!!!!main loop!!!!!!!!!===============================
canvas.addEventListener('click', function(event){var xx=event.offsetX; var yy= event.offsetY;
cx.fillStyle = "red";
if (xx < 430 || (xx>430 && yy>235) ) 
		{twoswitch=-1*twoswitch;
canvas.width = canvas.width;
 ugli(); 
//bukvi();
bokovaja();nomeralone(470,yy0);
 cx.fillStyle = "red";
 cx.font = "20px Georgia";
tx=xx-xx%sizeofcell+sizeofcell+10*coeffsize;ttx=(tx-10)/sizeofcell;
 tttx=ttx.toFixed(0); ttttx=Number(tttx);ng=ttttx.toString();
ty=yy-yy%sizeofcell+sizeofcell-5*coeffsize;tty=(ty-10)/sizeofcell;
 ttty=tty.toFixed(0);tttty=Number(ttty);	ng=tttty.toString();
//cx.strokeText(ng, xx-xx%sizeofcell+sizeofcell+10*coeffsize,  yy-yy%sizeofcell+sizeofcell-5*coeffsize);
a=lab[ttttx-1][tttty-1];
if(a<-0.1){lab[ttttx-1][tttty-1]=0;}
if(a>-0.1){lab[ttttx-1][tttty-1]=-1;}
setka(); ugli();bokovaja();nomeralone(470,yy0);
lab1copy();n=n+1;voln();n=n-1;waywin();showputt(); nomersboku();
//if(twoswitch<1){labview()};
setka(); ugli();
//=============================== xx>430 ====  click of mouse x coord =============
		}else {
canvas.width = canvas.width;var t=0.1;t=(yy-15)/sizeofcell;
// recount number of cells nXn
var tt=t;var ttt=tt.toFixed(0);var tttt=Number(ttt);
n1=tttt%7+5;n=n1-1;inilabs();
setka(); ugli(); bukvi();bokovaja();  nomersboku();
// aligning of position of new number n
var xx0=470; if( xx<466)
{
nomeralone(xx0,yy);yy0=yy;
} else {nomeralone(xx,yy);yy0=yy;}


		}
}, false);

// ====================================================================================
</script>
</head>
<body>
<p>5x5==16 6x6==22 7X7==30 8X8==38 9X9==50 10X10==60 11X11==72 ???
</body>
</html>

"""
class MyClientHandler(socketserver.BaseRequestHandler):
    mycli=[]
    def handle(self):
        global lq1,lq2,ll1,ll2,mycli          
        dd=lq1+lq2
# для каждого клиента
        print(self.client_address, now()) # показать адрес этого клиента
# имитировать блокирующие действия
        while True:
# self.request – сокет клиента
            data = self.request.recv(1024) # чтение, запись в сокет клиента          
            if not data: break        #    end of connection and handle!!!
            try:
                print("request.recv(1024)")
                datastr=data.decode('utf-8') # fOArom byte coding to str
            except:
                break
#          ===      datastr='GET \?1 qqq kkkkk kklll kkkkkk' # put standard data if it is strange!!!
            if datastr[0:3]=='GET':      # GET - standard answer from browser, used form 'submite'
                print('get=',datastr.split())
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
                            raise SystemExit(1)
                        else:
                            dd=ll1+datapop+' = '+str(MyClientHandler.mycli)+' use_play '+ll2
            else:     #  else is case not normal first question from client, but it is DATA!!!
#                     firstcall
                dd=lq1+lq2
#         ====   end if  datastr='GET \?1 qqq kkkkk kklll kkkkkk' # put standard data if it is strange!!!
            if True:           
                try:
                    ddt=str(dd).encode('utf-8')   # from byte coding to str
                except:
                    print('errrrrrrrrrrrrrrrrrr',dd)
                    break
                try:
                    print('sending answer dd=',dd )
                    self.request.send(b"HTTP/1.1 " + status .encode("utf-8") + b"\r\n")
                    self.request.send(b"Content-Type: text/html; charset=utf-8\r\n\r\n")
                    self.request.sendall(ddt)
                    MyClientHandler.mycli.append(self.client_address)
                except:
                    break
#          end of WHILE!!! - next чтение, запись в сокет клиента but socket is the same
        print(MyClientHandler.mycli,'mycli')
        self.request.close()    #  next request, but socket is the same
# создать сервер с поддержкой многопоточной модели выполнения,
# слушать/обслуживать клиентов непрерывно
myaddr = (myHost, myPort)
server = socketserver.ThreadingTCPServer(myaddr, MyClientHandler)
dd=lq1+lq2
server.serve_forever()
