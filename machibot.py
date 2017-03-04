#!/usr/bin/env python
import os
import json
import random
import socket

def debug(message):
    print message
    pass

# RandomBot:
# this is the absolute baseline AI
def chooseAction(actionRequest):
    debug(actionRequest)
    choice = random.choice(actionRequest["options"])
    debug(choice)
    return choice

def getRequestString(sock):
    buff = ""
    while True:
        char = sock.recv(1)
        if char == '':
            raise RuntimeError("socket connection broken")
        elif char == "\n":
            break
        else:
            buff += char
    debug("received '{}'".format(buff))
    return buff

def sendString(sock, msg):
    debug("sending {}".format(msg))
    assert("\n" not in msg)
    msg += "\n"
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent

if __name__ == "__main__":
    DEFAULT_IP = "0.0.0.0" 
    DEFAULT_PORT = 1337

    if "MACHI_IP" in os.environ:
        print "setting IP from $MACHI_IP"
        ip = os.environ["MACHI_IP"]
    else:
        print "no $MACHI_IP found, using default IP"
        ip = DEFAULT_IP

    if "MACHI_PORT" in os.environ: 
        print "setting PORT from $MACHI_PORT"
        port = int(os.environ["MACHI_PORT"])
    else:
        print "no $MACHI_PORT found, using default PORT"
        port = DEFAULT_PORT

    address = (ip, port)

    print "binding server to {}".format(str(address))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(1)

    (clientSock, clientAddress) = sock.accept()

    try:
        while True:
            requestStr = getRequestString(clientSock)
            debug("###{}###".format(requestStr))
            request = json.loads(requestStr)
            reply = chooseAction(request)
            sendString(clientSock, reply)
    finally:
        print "closing socket"
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
