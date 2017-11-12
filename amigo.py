#!/usr/bin/python
# Import smtplib for the actual sending function

import smtplib
import random
import sys

class Player(object):
    name = ""
    mail = ""
    msg = ""

    def to_string(self):
        return self.name + ": " + self.mail
    # The class "constructor" - It's actually an initializer
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

class Pairplayer(object):
    playerfrom = Player("","")
    playerto = Player("","")

    def to_string(self):
        return "From: " + self.playerfrom.to_string() + " to: " + self.playerto.to_string()

    # The class "constructor" - It's actually an initializer
    def __init__(self, playerfrom, playerto):
        self.playerfrom = playerfrom
        self.playerto = playerto

dictionary_from = {}
dictionary_to = {}
text = ""
subject = "Amigo invisible 2017"

def fill_dictionary(arg):
    global dictionary_from
    wo_new_line = arg[:-1]
    friend_list =  wo_new_line.split(':', 1)
    dictionary_from[friend_list[0]] = friend_list[1]

def read_list(name):
    f = open(name, 'rw')
    print "Reading list"
    for line in f:
            fill_dictionary(line)

    global dictionary_to
    dictionary_to = dictionary_from.copy()
    print "List readed"

def mix_names():
    print "Mixing names"
    length = len(dictionary_from)
    i = 0
    time = 0
    list_players = []
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
            new_player = Pairplayer(playerfrom,playerto)
            list_players.append(new_player)
            i= i+1
        time = time+1
        if time == (length*3):
            print "Error, you have to repeat the process. A person has been matched with himself/herself"
            sys.exit()

    print "Names mixed"
    return list_players


def send_mail(players):
    i = 1
    print "Sending mails"
    for value in players:
        value.playerfrom.msg = text.replace('[namefrom]',value.playerfrom.name).replace('[nameto]',value.playerto.name)
        username = 'manoinocenteavila@gmail.com'
        password = 'manoinocente'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        server.login(username,password)
        #Add the Subject
        message ='Subject: {}\n\n{}'.format(subject, value.playerfrom.msg)
        server.sendmail(username, value.playerfrom.mail , message)
        server.quit()
        print "The " + str(i) + " mail has been sent"
        i = i+1
    print "All mails have been sent"

if __name__ == "__main__":
    if len(sys.argv) > 2:
        f = open(str(sys.argv[2]), 'rw')
        text = f.read();
        read_list(str(sys.argv[1]))
        list_players = mix_names()
        send_mail(list_players)
    else:
        print "Script not properly executed: amigo.py [list_path] [text]"
