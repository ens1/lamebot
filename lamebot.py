#!/usr/bin/python2
import sys, socket, string
from modules import lastfm, random_imgur, eightball, decide, distro, uwot,          jimmies
HOST="irc.rizon.net"
PORT=6667
NICK="lamebot"
IDENT="lamebot"
REALNAME="Ens1sBot"
CHANNEL="#/g/summer"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
print("Connected to %s:%s" % (HOST, PORT))
s.send("NICK %s\r\n" % NICK)
print("Nick is now %s" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN %s\r\n" % CHANNEL)
print("Joining %s" % CHANNEL)
#Send message when joining
s.send("PRIVMSG %s :I belong to ens1\r\n" % (CHANNEL))


while 1:
    
    readbuffer=readbuffer+s.recv(4096)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )

    for line in temp:
        line=string.rstrip(line)
        line=string.split(line)
        
        try:

            #Pong when pinged
            if(line[0]=="PING"):
                s.send("PONG %s\r\n" %line[1])

            #If this is a message in CHANNEL
            if(line[1]=="PRIVMSG"):
                if(line[2]==CHANNEL):

                    USERNICK=string.split(string.split(line[0], "!")[0], ":")[1]
                

                    #Random imgur
                    if(line[3].lower()==":.imgur"):
                        s.send("PRIVMSG %s :%s\r\n" % (line[2], random_imgur.returnimage()))
    
                    
                    #Send last.fm now playing
                    if(line[3].lower()==":.np"):
                        s.send("PRIVMSG %s :%s\r\n" % (line[2], lastfm.np(line[4])))
                    if(line[3].lower()==":.compare"):
                        s.send("PRIVMSG %s :%s\r\n" % (line[2], lastfm.compare(line[4], line[5])))
                    #Say Hello
                    if(line[3].lower()==":hello"):
                        if(line[4].lower()=="lamebot"):
                            s.send("PRIVMSG %s :Hello %s\r\n" % (line[2], USERNICK))

                    #8ball
                    if(line[3].lower()==":.8ball"):
                        s.send("PRIVMSG %s :%s\r\n" % (line[2], eightball.answer(line[4:])))
    
                    #decide
                    if(line[3].lower()==":.decide"):
                        s.send("PRIVMSG %s :%s\r\n" % (line[2], decide.decide(string.join(line[4:]))))
                    
                    #distro
                    if(line[3].lower()==":.distro"):
                        s.send("PRIVMSG %s :%s\r\n" % (line[2], distro.returndistro(line[4:])))
    
                    #u wot m8?
                    if(line[3].lower()==":.uwotm8"):
                        s.send("PRIVMSG %s :%s\r\n" % (line[2], uwot.m8()))

                    #Are your jimmies rustled?
                    if(line[3].lower()==".rustle"):
                        s.send("PRIVMSG %s :%s\r\n" % (line[2], jimmies.rustle()))

        except IndexError:
            pass
