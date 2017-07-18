#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Queen of Agorà 1.3
# Coded by Nightmare

import urllib
import urllib2
import socket
import os, sys
import time, re
import string, random
from TorCtl import TorUtil, PathSupport, TorCtl

class MyWinnerIs(object):
    def __init__(self, numero_voti, tipa):
        self.numero_voti = numero_voti
        self.tipa = tipa
        proxy_handler = urllib2.ProxyHandler({'http': 'http://127.0.0.1:8118'})
        self.opener = urllib2.build_opener(proxy_handler)
##        self.opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0))')]
        self.opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1;)')]

    def vote(self):
##        data = urllib.urlencode( { "votato": self.clip_id } )
##        url = "http://REDACTED.it/REDACTED-sondaggio/wp-content/plugins/sondaggi/vedisondaggio.php?question_id=2053&idAnswer=113973&answer_id113973=17116&submit=Vota&backurl=http://REDACTED.it/REDACTED-sondaggio/wp-content/vedi_2053.html";
        url = "http://REDACTED.it/REDACTED-sondaggio/wp-content/plugins/sondaggi/vedisondaggio.php?question_id=2053&idAnswer=113973&answer_id113973="+self.tipa+"&submit=Vota&recaptcha_response_field=Reinvented&recaptcha_challenge_field=02_Ed3BjRT1NP4-G-grOt&backurl=http://REDACTED.it/REDACTED-sondaggio/wp-content/vedi_2053.html"
        request = urllib2.Request(url)
        conn = self.opener.open(request)#, data).read()
        data = conn.read()
        return data

    def check_ip(self):
        html = self.opener.open("http://checkip.dyndns.org").read()
        ricerca = re.search("\d+\.\d+\.\d+\.\d+", html)
        return ricerca.group(0)

    def timed(self,times):
        for m in range(int(times)):
            self.vote()
        return

    def resetTor(self):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(("localhost",9051))
            c = PathSupport.Connection(s)
            c.authenticate('Agora')
            c.send_signal(3)
            c.close()
        except socket.error, e:
            print "[!] Couldn't connect to TOR."
            sys.exit(-1)

    def start_loop(self,wait=random.randint(15,60)):
        volte = 0
        while volte<self.numero_voti:
            try:
                self.resetTor()
                response = self.vote()
                volte += 1
                sys.stdout.write("[ %s ] IP: %s - %s di %s\n" % (time.ctime(), self.check_ip(), volte, numero_voti))
                Posizione = string.find(response, '"poll-esitovoto"',0)
                print 'Risposta: %s' % (response[Posizione+21:Posizione+43])
            except KeyboardInterrupt:
                print "\nho votato", volte, "volte\n"
                raw_input()
                return

def url2id(addrs):
    filename = os.path.basename(addrs)
    options = filename.split("?")[1].split("&")
    for opt in options:
        if "votato=" in opt: return opt.replace("votato=","")
    return addrs

if __name__ == "__main__":
##    opener = urllib2.build_opener()
##    status = opener.open('http://agora.REDACTED.it/status.txt').read()
    status='2'
    if(status=='x'):
        sys.exit('Error: Division by 0')
    print ''
    print '-'*54
    s = '| coded by Nightmare for Agorà - 03/06/2010 - ver1.3 |'
    print unicode(s, "utf-8")
    print '-'*54
    print ''
    if(status=='0'):
        print('Stop al televoto')
        raw_input()
        sys.exit()
    elif(status=='1'):
        print '\o/ Only The Queen \o/'
        tipa = '17116'
    elif(status=='2'):
        print '1 - Tatiana C'
        s = '2 - Maria (Queen of Agorà)'
        print unicode(s, "utf-8")    
        print '3 - Natalia R'
        print '4 - Caterina S'
        print '5 - Elena B'
        print '6 - Giulia F'
        print '7 - Nicole F'
        print '8 - Giulia M'
        print '9 - Beatrice B\n'
        print 'q - abort mission\n'
        var = raw_input("Scegli chi votare: ").strip()
        print ''
        if(var=='q'):
            print('cya')
            raw_input()
            sys.exit()
        elif(var=='1'):
            print('Problem, l1v3x?')
            raw_input()
            sys.exit()
        elif(var=='2'):
            tipa = '17116'
        elif(var=='3'):
            tipa = '17224'
        elif(var=='4'):
            tipa = '17119'
        elif(var=='5'):
            tipa = '17118'
        elif(var=='6'):
            tipa = '17219'
        elif(var=='7'):
            tipa = '17223'
        elif(var=='8'):
            tipa = '17080'
        elif(var=='9'):
            tipa = '17124'
        else:
            print('GTFO')
            raw_input()
            sys.exit()
    elif(status=='3'):
        print '1 - Tatiana C'
        s = '2 - Maria (Queen of Agorà) - In Pausa'
        print unicode(s, "utf-8")    
        print '3 - Natalia R'
        print '4 - Caterina S'
        print '5 - Elena B'
        print '6 - Giulia F'
        print '7 - Nicole F'
        print '8 - Giulia M'
        print '9 - Beatrice B\n'
        print 'q - abort mission\n'
        var = raw_input("Scegli chi votare: ").strip()
        print ''
        if(var=='q'):
            print('cya')
            raw_input()
            sys.exit()
        elif(var=='1'):
            print('Problem, l1v3x?')
            raw_input()
            sys.exit()
        elif(var=='2'):
            print('Ho detto in pausa :|')
            raw_input()
            sys.exit()
        elif(var=='3'):
            tipa = '17224'
        elif(var=='4'):
            tipa = '17119'
        elif(var=='5'):
            tipa = '17118'
        elif(var=='6'):
            tipa = '17219'
        elif(var=='7'):
            tipa = '17223'
        elif(var=='8'):
            tipa = '17080'
        elif(var=='9'):
            tipa = '17124'
        else:
            print 'GTFO'
            raw_input()
            sys.exit()
    else:
        sys.exit('Error: Division by 0')
    print 'IMMA CHARGIN MAH LAZER\n'
    value = " ".join(sys.argv[1:])
##    if "http://" in value: value = url2id(value)
    if value=="":
        numero_voti = 9000
    else:
        numero_voti = int(value)
    voter = MyWinnerIs(numero_voti, tipa)
    voter.start_loop()
