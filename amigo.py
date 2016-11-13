#!/usr/bin/python
# Import smtplib for the actual sending function

import smtplib
import random
import sys

class Player(object):
    name = ""
    mail = ""
    msg = ""

    def print_player():
        print name + ": " + email
    # The class "constructor" - It's actually an initializer
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

class Pairplayer(object):
    playerfrom = Player("","")
    playerto = Player("","")

    # The class "constructor" - It's actually an initializer
    def __init__(self, playerfrom, playerto):
        self.playerfrom = playerfrom
        self.playerto = playerto

dictionary_from = {}
dictionary_to = {}
text = ""

def fill_dictionary(arg):
    wo_back_slash = arg[:-1]
    friend_list =  wo_back_slash.split(':', 1)
    dictionary_from[friend_list[0]] = friend_list[1]

def read_list(name):
    f = open(name, 'rw')

    for line in f:
            fill_dictionary(line)

    global dictionary_to
    dictionary_to = dictionary_from.copy()
    mix_names()

def mix_names():
    length = len(dictionary_from)
    i = 0
    time = 0
    listPlayers = []
    while i < length :

        namefrom = random.choice(dictionary_from.keys())
        mailfrom = dictionary_from[namefrom]
        playerfrom = Player(namefrom,mailfrom)

        nameto = random.choice(dictionary_to.keys())
        mailto = dictionary_to[nameto]
        playerto = Player(nameto,mailto)

        if mailto != mailfrom:
            del dictionary_to[nameto]
            del dictionary_from[namefrom]
            newPlayer = Pairplayer(playerfrom,playerto)
            listPlayers.append(newPlayer)
            i= i+1
        time = time+1
        if time == (length*3):
            print "Error, you have to repeat the process. A person has been matched with himself/herself"
            sys.exit()

    send_mail(listPlayers)




def send_mail(players):
    i = 0
    for value in players:
        value.playerfrom.msg = text.replace('[namefrom]',value.playerfrom.name).replace('[nameto]',value.playerto.name)
        username = 'mailtouse@blah.com'
        password = 'psw'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        server.login(username,password)
        server.sendmail(username, value.playerfrom.mail , value.playerfrom.msg)
        server.quit()
        i+=i+1
        print i


if __name__ == "__main__":
    if len(sys.argv) > 2:
        f = open(str(sys.argv[2]), 'rw')
        text = f.read();
        read_list(str(sys.argv[1]))
    else:
        print "Script not properly executed: amigo.py [list_path] [text]"
