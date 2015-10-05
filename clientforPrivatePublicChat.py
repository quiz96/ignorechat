## Keegan helped me debug this
## client


import socket
import sys
import string

server = "irc.efnet.org"       #settings
channel = b"#privatepublicchat"
usernick = input("Username: ")

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
#irc.setblocking(False)
irc.connect((server, 6667))
print(irc.recv ( 4096 ))
irc.send(bytes("NICK %s\r\n" % usernick, "UTF-8"))
irc.send(bytes("USER %s %s bla :%s\r\n" % (usernick, server, usernick), "UTF-8"))
irc.send(bytes("JOIN #privatepublicchat\r\n", "UTF-8"));
irc.send(bytes("PRIVMSG %s :Hello Master\r\n" % "master", "UTF-8"))


def standby():
    rstack = []
    while True:
        #print("looping")
        command = input("rtr: ")
        #print(irc.recv(2040))
        receive = irc.recv(2040)
        rstack = rstack + \
        receive.split(b"\r\n")[1:]
        #print(rstack)
        if (receive[0] == "PING"):
            irc.send(bytes("PONG %s\r\n" % receive[1], "UTF-8"))
        if command[:6] == "/send ": # client sends a message, resulting in
            send(command) # printing all previous messages from that user
            usepr(rstack, (bytes(str.split(command)[1], "utf-8")))
        if command[:10] == "/terminate":
            irc.send(b"QUIT")
            break
        if len(rstack) == 4096:
            rstack = []
    return

def usepr(lst, find):
    #print(lst)
    for mess in lst:
        if find in mess:
            print(mess.split(b"#privatepublicchat")[1:])
    return

## sends a message into app client.

def send(message):
    irc.send(bytes("PRIVMSG #privatepublicchat :" + message[6:] + "\r\n", "UTF-8"))
    return

standby()




