# https://docs.python.org/3/howto/sockets.html
# https://stackoverflow.com/questions/8627986/how-to-keep-a-socket-open-until-client-closes-it
# https://stackoverflow.com/questions/10091271/how-can-i-implement-a-simple-web-server-using-python-without-using-any-libraries

'''
from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)#creating a telephone to receive requests by the browser
    try :
        serversocket.bind(('localhost',9000))
        serversocket.listen(5)#take one request at a time but  can hold at max 5 requests in queue
        while(1):
            (clientsocket, address) = serversocket.accept()#accept blocks an intercepts a request for connection by some browser-can simultaneously talk and listen
            #next line only runs if a connection is made 

            rd = clientsocket.recv(5000).decode()#we get in utf 8 and convert it to utf 16-read 5000 characters
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])#get the first line

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())#encode to utf 8 again to send this to the client web browser
            clientsocket.shutdown(SHUT_WR)#close the client side 

    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)

    serversocket.close()#close the server
    #browser automatically makes a favicon for the icon of the webpage even if we never asked for it
    #open webpage at the localhost and the spcified port-see results displayed again and again as we refresh the page

print('Access http://localhost:9000')
createServer()
'''
#own attempt
from socket import *
def serverMethod():

    socket1=socket(AF_INET,SOCK_STREAM)
    try:
        socket1.bind(('localhost',7000))
        socket1.listen(7)
        while(1):#while always true(infinite loop)
            (clientsocket1,address)=socket1.accept()
            rd=clientsocket1.recv(2500).decode()
            pieces=rd.split("\n")
            if(len(pieces)!=0):
                print(pieces[0])
            data1="HTTP/1.1 200 OK\r\n"
            data1+="Content-Type:text/html;charset=utf-8\r\n"
            data1+="\r\n"
            data1+="<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket1.sendall(data1.encode())
            clientsocket1.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("error\n")
        print(exc)
    socket1.close()
print("access http://localhost:7000")
serverMethod()

