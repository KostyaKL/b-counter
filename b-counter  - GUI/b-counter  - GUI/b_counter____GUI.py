# -*- coding: utf-8 -*-

# -------------------------Made by Kostya Lokshin - Gaf Maarahot Baha 6, Feb 2015----------------------------

#to do list
#connect counter

#!/usr/bin/python
# -*- coding: utf-8 -*-

"Experimental sample gui2py application demo of sizer usage"

__author__ = "Kostya Lokshin (klokshin@gmail.com)"
__copyright__ = "Copyright (C) 2015 - Kostya Lokshin"

import datetime
import decimal
import os
import sys
import usb
import time
import pickle
import wx, locale
import thread
from arduino.usbdevice import ArduinoUsbDevice
from win32api import GetSystemMetrics
import winsound, sys

 


# disable ubuntu unified menu
os.environ['UBUNTU_MENUPROXY'] = '0'

import gui



bombnum=u'0'
bombpase=u'0'
shiftpase=u'0'
bombtype=u'<- ??? ??? ????'
startime = time.time()
#shifttime = time.time()
b=0  #bomb pase
c=0  #shift pase
ddelay=0


def logicloop (loopy):
    try:
        theDevice = ArduinoUsbDevice(idVendor=0x16c0, idProduct=0x05df)
    
    except:
        gui.alert(u'?? ???? ?? ???? ?????? ????? ??? ????? ????? \n ??? ?? ????? ????? ?? ????? ????')



    try:
        
        f=open('data.txt', 'r')
        a=pickle.load(f)
        #print a, "Bombs So Far At:", time.ctime()
    
    except:
        a=0

    b=0
    f=open('pase.txt', 'w')
    pickle.dump(b, f)
    f.close()

    startime=time.time()
    f=open('startime.txt', 'w')
    pickle.dump(startime, f)
    f.close()


    c=0
    f=open('shiftpase.txt', 'w')
    pickle.dump(c, f)
    f.close()

    shifttime=time.time()
    f=open('shifttime.txt', 'w')
    pickle.dump(shifttime, f)
    f.close()

    



    
        
    while True:
        lastChar = chr(theDevice.read())
        sys.stdout.flush()
        
        while (lastChar == "0"):
            

            lastChar = chr(theDevice.read())

            if (lastChar == "1"):
                winsound.PlaySound('bomb.wav', winsound.SND_FILENAME)

                f=open('data.txt', 'r')
                a=pickle.load(f)

                a=a+1
                #print a, "Bombs So Far At:", time.ctime()

                ddelay=0
         
                bombnum=a
                mywin['count'].left = '860'
                if (9<a<100):
                    mywin['count'].left = '790'
                if (99<a<1000):
                    mywin['count'].left = '720'
                if (999<a):
                    mywin['count'].left = '660'
                mywin['count'].size = (0,0)
                mywin['count'].text = u'%s' %(bombnum)
                mywin['count'].transparent=False
                mywin['count'].transparent=True
                mywin['count'].bgcolor='transparent'


                
                f=open('data.txt', 'w')
                pickle.dump(a, f)
                f.close()
                lastChar = chr(theDevice.read())


                mywin['statusbar'].text = u"???? ?????? ?????? ????: %s" % (time.ctime())

                f=open('pase.txt', 'r')
                b=pickle.load(f)
                b=b+1


                f=open('startime.txt', 'r')
                startime=pickle.load(f)
                
                pase = time.time()
                avg=(pase-startime)
                
                #print "time passed: ", avg
                avgpase=(b/avg)*3600
                #print b
                #print "bomb pase: ", avgpase

                avgpase=int(avgpase)
                bombpase=avgpase
                print bombpase
                if (bombpase<1):
                    mywin['bombpase'].fgcolor=u'#FFFFFF'                 
                    mywin['bombpase'].left='800'
                    mywin['bombpase'].top='500'
                    mywin['bombpase'].size = (0,0)
                    mywin['bombpase'].text=u'--'
                    mywin['bombpase'].transparent=False
                    mywin['bombpase'].transparent=True
                    mywin['bombpase'].bgcolor='transparent'
                if (1<=bombpase<10):
                    mywin['bombpase'].fgcolor=u'#FFFFFF'
                    mywin['bombpase'].left='800'
                    mywin['bombpase'].size = (0,0)
                    mywin['bombpase'].text = u'%s' %(bombpase)
                    mywin['bombpase'].transparent=False
                    mywin['bombpase'].transparent=True
                    mywin['bombpase'].bgcolor='transparent'
                if (10<=bombpase<=33):
                    mywin['bombpase'].fgcolor=u'#FFFFFF'
                    mywin['bombpase'].left='775'
                    mywin['bombpase'].top='480'
                    mywin['bombpase'].size = (0,0)
                    mywin['bombpase'].text = u'%s' %(bombpase)
                    mywin['bombpase'].transparent=False
                    mywin['bombpase'].transparent=True
                    mywin['bombpase'].bgcolor='transparent'
                if (34<=bombpase<=99):
                    mywin['bombpase'].fgcolor=u'#FFFFFF'
                    mywin['bombpase'].left='775'
                    mywin['bombpase'].top='480'
                    mywin['bombpase'].size = (0,0)
                    mywin['bombpase'].text = u'%s' %(bombpase)
                    mywin['bombpase'].transparent=False
                    mywin['bombpase'].transparent=True
                    mywin['bombpase'].bgcolor='transparent'
                if (99<bombpase):
                    mywin['bombpase'].fgcolor=u'#FFFFFF'
                    mywin['bombpase'].left='780'
                    mywin['bombpase'].top='500'
                    mywin['bombpase'].size = (0,0)
                    mywin['bombpase'].text=u'--'
                    mywin['bombpase'].transparent=False
                    mywin['bombpase'].transparent=True
                    mywin['bombpase'].bgcolor='transparent'
                f=open('pase.txt', 'w')
                pickle.dump(b, f)
                f.close()


                f=open('shiftpase.txt', 'r')
                c=pickle.load(f)
                c=c+1


                f=open('shifttime.txt', 'r')
                shifttime=pickle.load(f)
                
                shiftpase = time.time()
                shiftavg=(shiftpase-shifttime)
                
                #print "time passed: ", shiftavg
                shiftavgpase=(c/shiftavg)*3600
                #print c
                #print "bomb pase: ", shiftavgpase

                shiftavgpase=int(shiftavgpase)
                shiftbombpase=shiftavgpase
                print shiftbombpase
                if (shiftbombpase<1):
                    mywin['shiftbombpase'].fgcolor=u'#FFFFFF'                 
                    mywin['shiftbombpase'].left='800'
                    mywin['shiftbombpase'].top='700'
                    mywin['shiftbombpase'].size = (0,0)
                    mywin['shiftbombpase'].text=u'--'
                    mywin['shiftbombpase'].transparent=False
                    mywin['shiftbombpase'].transparent=True
                    mywin['shiftbombpase'].bgcolor='transparent'
                if (1<=shiftbombpase<10):
                    mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
                    mywin['shiftbombpase'].left='800'
                    mywin['shiftbombpase'].size = (0,0)
                    mywin['shiftbombpase'].text = u'%s' %(shiftbombpase)
                    mywin['shiftbombpase'].transparent=False
                    mywin['shiftbombpase'].transparent=True
                    mywin['shiftbombpase'].bgcolor='transparent'
                if (10<=shiftbombpase<=33):
                    mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
                    mywin['shiftbombpase'].left='775'
                    mywin['shiftbombpase'].top='680'
                    mywin['shiftbombpase'].size = (0,0)
                    mywin['shiftbombpase'].text = u'%s' %(shiftbombpase)
                    mywin['shiftbombpase'].transparent=False
                    mywin['shiftbombpase'].transparent=True
                    mywin['shiftbombpase'].bgcolor='transparent'
                if (34<=shiftbombpase<=99):
                    mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
                    mywin['shiftbombpase'].left='775'
                    mywin['shiftbombpase'].top='680'
                    mywin['shiftbombpase'].size = (0,0)
                    mywin['shiftbombpase'].text = u'%s' %(shiftbombpase)
                    mywin['shiftbombpase'].transparent=False
                    mywin['shiftbombpase'].transparent=True
                    mywin['shiftbombpase'].bgcolor='transparent'
                if (99<shiftbombpase):
                    mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
                    mywin['shiftbombpase'].left='780'
                    mywin['shiftbombpase'].top='700'
                    mywin['shiftbombpase'].size = (0,0)
                    mywin['shiftbombpase'].text=u'--'
                    mywin['shiftbombpase'].transparent=False
                    mywin['shiftbombpase'].transparent=True
                    mywin['shiftbombpase'].bgcolor='transparent'
                f=open('shiftpase.txt', 'w')
                pickle.dump(c, f)
                f.close()

                while(ddelay < 50000000):
                    ddelay = ddelay + 1
                    
                
                break

            

    

def zero (evt):
    a=0
    f=open('data.txt', 'w')
    pickle.dump(a, f)
    f.close()
    f=open('data.txt', 'r')
    var1=pickle.load(f)
    #print var1, "Bombs So Far At:", time.ctime()

    bombnum=a
    mywin['count'].left = '860'
    mywin['count'].size = (0,0)
    mywin['count'].text = u'%s' %(bombnum)
    mywin['count'].transparent=False
    mywin['count'].transparent=True
    mywin['count'].bgcolor='transparent'

    startime=time.time()
    f=open('startime.txt', 'w')
    pickle.dump(startime, f)
    f.close()

    shifttime=time.time()
    f=open('shifttime.txt', 'w')
    pickle.dump(shifttime, f)
    f.close()
    
    b=0
    f=open('pase.txt', 'w')
    pickle.dump(b, f)
    f.close()

    c=0
    f=open('shiftpase.txt', 'w')
    pickle.dump(c, f)
    f.close()

    
    mywin['bombpase'].fgcolor=u'#FFFFFF'
    mywin['bombpase'].left='800'
    mywin['bombpase'].size = (0,0)
    mywin['bombpase'].text = u'0'
    mywin['bombpase'].transparent=False
    mywin['bombpase'].transparent=True
    mywin['bombpase'].bgcolor='transparent'

    mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
    mywin['shiftbombpase'].left='800'
    mywin['shiftbombpase'].size = (0,0)
    mywin['shiftbombpase'].text = u'0'
    mywin['shiftbombpase'].transparent=False
    mywin['shiftbombpase'].transparent=True
    mywin['shiftbombpase'].bgcolor='transparent'


def zeroavg (evt):
    startime=time.time()
    f=open('startime.txt', 'w')
    pickle.dump(startime, f)
    f.close()

    shifttime=time.time()
    f=open('shifttime.txt', 'w')
    pickle.dump(shifttime, f)
    f.close()

    b=0
    f=open('pase.txt', 'w')
    pickle.dump(b, f)
    f.close()

    c=0
    f=open('shiftpase.txt', 'w')
    pickle.dump(c, f)
    f.close()
    
    mywin['bombpase'].fgcolor=u'#FFFFFF'
    mywin['bombpase'].left='800'
    mywin['bombpase'].size = (0,0)
    mywin['bombpase'].text = u'0'
    mywin['bombpase'].transparent=False
    mywin['bombpase'].transparent=True
    mywin['bombpase'].bgcolor='transparent'

    mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
    mywin['shiftbombpase'].left='800'
    mywin['shiftbombpase'].size = (0,0)
    mywin['shiftbombpase'].text = u'0'
    mywin['shiftbombpase'].transparent=False
    mywin['shiftbombpase'].transparent=True
    mywin['shiftbombpase'].bgcolor='transparent'


def zeroshift (evt):
    shifttime=time.time()
    f=open('shifttime.txt', 'w')
    pickle.dump(shifttime, f)
    f.close()

    c=0
    f=open('shiftpase.txt', 'w')
    pickle.dump(c, f)
    f.close()
    mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
    mywin['shiftbombpase'].left='800'
    mywin['shiftbombpase'].size = (0,0)
    mywin['shiftbombpase'].text = u'0'
    mywin['shiftbombpase'].transparent=False
    mywin['shiftbombpase'].transparent=True
    mywin['shiftbombpase'].bgcolor='transparent'

   


def bombt (evt):
    mywin['factype'].visible = True
    mywin['barad had'].visible = True
    mywin['barad kaved'].visible = True
    mywin['zarit'].visible = True
    mywin['baradplada'].visible = True

    

    
    

def load (evt):
    #print "lets begin"
    mywin['factype'].visible = True
    mywin['barad had'].visible = True
    mywin['barad kaved'].visible = True
    mywin['zarit'].visible = True
    mywin['baradplada'].visible = True


    f=open('data.txt', 'r')
    a=pickle.load(f)
                
    bombnum=a
    mywin['count'].left = '860'
    if (9<a<100):
        mywin['count'].left = '790'
    if (99<a<1000):
        mywin['count'].left = '720'
    if (999<a):
        mywin['count'].left = '660'
    mywin['count'].size = (0,0)
    mywin['count'].text = u'%s' %(bombnum)
    mywin['count'].transparent=False
    mywin['count'].transparent=True
    mywin['count'].bgcolor='transparent'


    startime=time.time()
    f=open('startime.txt', 'w')
    pickle.dump(startime, f)
    f.close()

    shifttime=time.time()
    f=open('shifttime.txt', 'w')
    pickle.dump(shifttime, f)
    f.close()

    
    b=0
    f=open('pase.txt', 'w')
    pickle.dump(b, f)
    f.close()

    c=0
    f=open('shiftpase.txt', 'w')
    pickle.dump(c, f)
    f.close()
    
    #print startime

    mywin.height=1040
    mywin.width=1920
    mywin.left='0'
    mywin.top='0'
    mywin.border='none'
    mywin.caption=False
    mywin.resizabe=False
    mywin.stay_on_top=True
    mywin.tool_window=True

   
    

def baradhad (evt):
    mywin['bombtype'].text = u'??? ??'
    mywin['bombtype'].left = '800'
    mywin['factype'].visible = False
    mywin['barad had'].visible = False
    mywin['barad kaved'].visible = False
    mywin['zarit'].visible = False
    mywin['baradplada'].visible = False

def baradkaved (evt):
    mywin['bombtype'].text = u'??? ???'
    mywin['bombtype'].left = '750'
    mywin['factype'].visible = False
    mywin['barad had'].visible = False
    mywin['barad kaved'].visible = False
    mywin['zarit'].visible = False
    mywin['baradplada'].visible = False

def zarit (evt):
    mywin['bombtype'].text = u'?????'
    mywin['bombtype'].left = '800'
    mywin['factype'].visible = False
    mywin['barad had'].visible = False
    mywin['barad kaved'].visible = False
    mywin['zarit'].visible = False
    mywin['baradplada'].visible = False


def baradplada (evt):
    mywin['bombtype'].text = u'??? ????'
    mywin['bombtype'].left = '700'
    mywin['factype'].visible = False
    mywin['barad had'].visible = False
    mywin['barad kaved'].visible = False
    mywin['zarit'].visible = False
    mywin['baradplada'].visible = False
  



def menu_edit_count (evt):
    mywin['edit_count'].visible=True
    mywin['load'].visible=True
    mywin['initi'].visible=True
    mywin['cans'].visible=True
    mywin['count'].visible=False
    mywin['made'].visible=False
    mywin['bombs'].visible=False
    mywin['bombpase'].visible=False
    mywin['ryth'].visible=False
    mywin['shiftbombpase'].visible=False
    mywin['shiftryth'].visible=False
    mywin['hour'].visible=False

def count_load (evt):

    a=mywin['edit_count'].value
    try:
        a=int(a)
        f=open('data.txt', 'w')
        pickle.dump(a, f)
        f.close()
        f=open('data.txt', 'r')
        var1=pickle.load(f)
        #print var1, "Bombs So Far At:", time.ctime()
        
        bombnum=a
        mywin['count'].left = '860'
        if (9<a<100):
            mywin['count'].left = '790'
        if (99<a<1000):
            mywin['count'].left = '720'
        if (999<a):
            mywin['count'].left = '660'
        #mywin['count'].left = '660'
        mywin['count'].size = (0,0)
        mywin['count'].text = u'%s' %(bombnum)
        mywin['edit_count'].visible=False
        mywin['load'].visible=False
        mywin['initi'].visible=False
        mywin['cans'].visible=False
        mywin['count'].visible=True
        mywin['made'].visible=True
        mywin['bombs'].visible=True
        mywin['bombpase'].visible=True
        mywin['ryth'].visible=True
        mywin['shiftbombpase'].visible=True
        mywin['shiftryth'].visible=True
        mywin['hour'].visible=True
        mywin['edit_count'].value=''
    except:
        gui.alert(u'?? ????? ???? ????? ????')

def cans (evt):
    mywin['edit_count'].visible=False
    mywin['load'].visible=False
    mywin['initi'].visible=False
    mywin['cans'].visible=False
    mywin['count'].visible=True
    mywin['made'].visible=True
    mywin['bombs'].visible=True
    mywin['bombpase'].visible=True
    mywin['ryth'].visible=True
    mywin['shiftbombpase'].visible=True
    mywin['shiftryth'].visible=True
    mywin['hour'].visible=True
    mywin['edit_count'].value=''


def addbomb (evt):
    print 'start sond'
    winsound.PlaySound('bomb.wav', winsound.SND_FILENAME)
    print 'stop sound'

    f=open('data.txt', 'r')
    a=pickle.load(f)
    a=a+1


    


    
    f=open('data.txt', 'w')
    pickle.dump(a, f)
    f.close()
    
    bombnum=a
    mywin['count'].left = '860'
    if (9<a<100):
        mywin['count'].left = '790'
    if (99<a<1000):
        mywin['count'].left = '720'
    if (999<a):
        mywin['count'].left = '660'
    mywin['count'].size = (0,0)
    mywin['count'].text = u'%s' %(bombnum)
    mywin['count'].transparent=False
    mywin['count'].transparent=True
    mywin['count'].bgcolor='transparent'
    print bombnum

    
    f=open('pase.txt', 'r')
    b=pickle.load(f)
    b=b+1
    f=open('pase.txt', 'w')
    pickle.dump(b, f)
    f.close()

    f=open('startime.txt', 'r')
    startime=pickle.load(f)
                
    pase = time.time()
    avg=(pase-startime)
                
    avgpase=(b/avg)*3600
    avgpase=int(avgpase)
    bombpase=avgpase
    if (bombpase<1):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='800'
        mywin['bombpase'].top='500'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text=u'--'
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'
    if (1<=bombpase<10):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='800'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text = u'%s' %(bombpase)
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'
    if (10<=bombpase<=33):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='775'
        mywin['bombpase'].top='480'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text = u'%s' %(bombpase)
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'
    if (34<=bombpase<=99):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='775'
        mywin['bombpase'].top='480'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text = u'%s' %(bombpase)
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'
    if (99<bombpase):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='780'
        mywin['bombpase'].top='500'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text=u'--'
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'


    f=open('shiftpase.txt', 'r')
    c=pickle.load(f)
    c=c+1
    f=open('shiftpase.txt', 'w')
    pickle.dump(c, f)
    f.close()

    f=open('shifttime.txt', 'r')
    shifttime=pickle.load(f)
                
    shiftpase = time.time()
    shiftavg=(shiftpase-shifttime)
                
    shiftavgpase=(c/shiftavg)*3600
    shiftavgpase=int(shiftavgpase)
    shiftbombpase=shiftavgpase

    if (shiftbombpase<1):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'                 
        mywin['shiftbombpase'].left='800'
        mywin['shiftbombpase'].top='700'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text=u'--'
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'
    if (1<=shiftbombpase<10):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
        mywin['shiftbombpase'].left='800'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text = u'%s' %(shiftbombpase)
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'
    if (10<=shiftbombpase<=33):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
        mywin['shiftbombpase'].left='775'
        mywin['shiftbombpase'].top='680'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text = u'%s' %(shiftbombpase)
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'
    if (34<=shiftbombpase<=99):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
        mywin['shiftbombpase'].left='775'
        mywin['shiftbombpase'].top='680'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text = u'%s' %(shiftbombpase)
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'
    if (99<shiftbombpase):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
        mywin['shiftbombpase'].left='780'
        mywin['shiftbombpase'].top='700'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text=u'--'
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'

    


def removebomb (evt):
    f=open('data.txt', 'r')
    a=pickle.load(f)
    a=a-1
    f=open('data.txt', 'w')
    pickle.dump(a, f)
    f.close()
    
    bombnum=a
    mywin['count'].left = '860'
    if (9<a<100):
        mywin['count'].left = '790'
    if (99<a<1000):
        mywin['count'].left = '720'
    if (999<a):
        mywin['count'].left = '660'
    mywin['count'].size = (0,0)
    mywin['count'].text = u'%s' %(bombnum)
    mywin['count'].transparent=False
    mywin['count'].transparent=True
    mywin['count'].bgcolor='transparent'


    f=open('pase.txt', 'r')
    b=pickle.load(f)
    b=b-1
    f=open('pase.txt', 'w')
    pickle.dump(b, f)
    f.close()

    f=open('startime.txt', 'r')
    startime=pickle.load(f)
                
    pase = time.time()
    avg=(pase-startime)
                
    avgpase=(b/avg)*3600
    avgpase=int(avgpase)
    bombpase=avgpase
    if (bombpase<1):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='800'
        mywin['bombpase'].top='500'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text=u'--'
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'
    if (1<=bombpase<10):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='800'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text = u'%s' %(bombpase)
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'
    if (10<=bombpase<=33):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='775'
        mywin['bombpase'].top='480'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text = u'%s' %(bombpase)
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'
    if (34<=bombpase<=99):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='775'
        mywin['bombpase'].top='480'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text = u'%s' %(bombpase)
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'
    if (99<bombpase):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='780'
        mywin['bombpase'].top='500'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text=u'--'
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'

    f=open('shiftpase.txt', 'r')
    c=pickle.load(f)
    c=c-1
    f=open('shiftpase.txt', 'w')
    pickle.dump(c, f)
    f.close()

    f=open('shifttime.txt', 'r')
    shifttime=pickle.load(f)
                
    shiftpase = time.time()
    shiftavg=(shiftpase-shifttime)
                
    shiftavgpase=(c/shiftavg)*3600
    shiftavgpase=int(shiftavgpase)
    shiftbombpase=shiftavgpase

    if (shiftbombpase<1):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'                 
        mywin['shiftbombpase'].left='800'
        mywin['shiftbombpase'].top='700'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text=u'--'
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'
    if (1<=shiftbombpase<10):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
        mywin['shiftbombpase'].left='800'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text = u'%s' %(shiftbombpase)
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'
    if (10<=shiftbombpase<=33):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
        mywin['shiftbombpase'].left='775'
        mywin['shiftbombpase'].top='680'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text = u'%s' %(shiftbombpase)
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'
    if (34<=shiftbombpase<=99):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
        mywin['shiftbombpase'].left='775'
        mywin['shiftbombpase'].top='680'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text = u'%s' %(shiftbombpase)
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'
    if (99<shiftbombpase):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
        mywin['shiftbombpase'].left='780'
        mywin['shiftbombpase'].top='700'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text=u'--'
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'    




def click (evt):
    print 'click'
    winsound.PlaySound('bomb.wav', winsound.SND_FILENAME)

    

    f=open('data.txt', 'r')
    a=pickle.load(f)

    a=a+1
    #print a, "Bombs So Far At:", time.ctime()


         
    bombnum=a
    #mywin['count'].left = '860'
    if (a<9):
        mywin['count'].left = '860'
        mywin['count'].size = (0,0)
        mywin['count'].text = u'%s' %(bombnum)
        mywin['count'].transparent=False
        mywin['count'].transparent=True
        mywin['count'].bgcolor='transparent'
    if (9<a<100):
        mywin['count'].left = '790'
        mywin['count'].size = (0,0)
        mywin['count'].text = u'%s' %(bombnum)
        mywin['count'].transparent=False
        mywin['count'].transparent=True
        mywin['count'].bgcolor='transparent'
    if (99<a<1000):
        mywin['count'].left = '720'
        mywin['count'].size = (0,0)
        mywin['count'].text = u'%s' %(bombnum)
        mywin['count'].transparent=False
        mywin['count'].transparent=True
        mywin['count'].bgcolor='transparent'
    if (999<a):
        mywin['count'].left = '660'
        mywin['count'].size = (0,0)
        mywin['count'].text = u'%s' %(bombnum)
        mywin['count'].transparent=False
        mywin['count'].transparent=True
        mywin['count'].bgcolor='transparent'


                
    f=open('data.txt', 'w')
    pickle.dump(a, f)
    f.close()


    mywin['statusbar'].text = u"???? ?????? ?????? ????: %s" % (time.ctime())

    f=open('pase.txt', 'r')
    b=pickle.load(f)
    b=b+1


    f=open('startime.txt', 'r')
    startime=pickle.load(f)
                
    pase = time.time()
    avg=(pase-startime)
                
    #print "time passed: ", avg
    avgpase=(b/avg)*3600
    #print b
    #print "bomb pase: ", avgpase

    avgpase=int(avgpase)
    bombpase=avgpase
    print bombpase
    if (bombpase<1):
        mywin['bombpase'].fgcolor=u'#FFFFFF'                 
        mywin['bombpase'].left='800'
        mywin['bombpase'].top='500'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text=u'--'
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'
    if (1<=bombpase<10):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='800'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text = u'%s' %(bombpase)
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'
    if (10<=bombpase<=33):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='775'
        mywin['bombpase'].top='480'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text = u'%s' %(bombpase)
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'
    if (34<=bombpase<=99):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='775'
        mywin['bombpase'].top='480'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text = u'%s' %(bombpase)
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'
    if (99<bombpase):
        mywin['bombpase'].fgcolor=u'#FFFFFF'
        mywin['bombpase'].left='780'
        mywin['bombpase'].top='500'
        mywin['bombpase'].size = (0,0)
        mywin['bombpase'].text=u'--'
        mywin['bombpase'].transparent=False
        mywin['bombpase'].transparent=True
        mywin['bombpase'].bgcolor='transparent'
    f=open('pase.txt', 'w')
    pickle.dump(b, f)
    f.close()


    f=open('shiftpase.txt', 'r')
    c=pickle.load(f)
    c=c+1


    f=open('shifttime.txt', 'r')
    shifttime=pickle.load(f)
                
    shiftpase = time.time()
    shiftavg=(shiftpase-shifttime)
                
    #print "time passed: ", shiftavg
    shiftavgpase=(c/shiftavg)*3600
    #print c
    #print "bomb pase: ", shiftavgpase

    shiftavgpase=int(shiftavgpase)
    shiftbombpase=shiftavgpase
    print shiftbombpase
    if (shiftbombpase<1):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
        mywin['shiftbombpase'].left='800'
        mywin['shiftbombpase'].top='700'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text=u'--'
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'
    if (1<=shiftbombpase<10):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
        mywin['shiftbombpase'].left='800'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text = u'%s' %(shiftbombpase)
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'
    if (10<=shiftbombpase<=33):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
        mywin['shiftbombpase'].left='775'
        mywin['shiftbombpase'].top='680'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text = u'%s' %(shiftbombpase)
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'
    if (34<=shiftbombpase<=99):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
        mywin['shiftbombpase'].left='775'
        mywin['shiftbombpase'].top='680'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text = u'%s' %(shiftbombpase)
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'
    if (99<shiftbombpase):
        mywin['shiftbombpase'].fgcolor=u'#FFFFFF'
        mywin['shiftbombpase'].left='780'
        mywin['shiftbombpase'].top='700'
        mywin['shiftbombpase'].size = (0,0)
        mywin['shiftbombpase'].text=u'--'
        mywin['shiftbombpase'].transparent=False
        mywin['shiftbombpase'].transparent=True
        mywin['shiftbombpase'].bgcolor='transparent'
    f=open('shiftpase.txt', 'w')
    pickle.dump(c, f)
    f.close()

    

    
def Exit (evt):
    sys.exit()


# --- gui2py designer generated code starts ---

gui.Window(name='mywin', title=u'bomb counter', resizable=False, 
           height='1010px', left='0', top='0', width='1920px', 
           bgcolor=u'#E0E0E0', image='bomb full.bmp', tiled=False, maximize_box=False, border='none', caption=False, resizabe=False,
           srtay_on_top=True, tool_window=True,  )
#onmousedown=click

gui.StatusBar(name='statusbar', parent='mywin',)


gui.Label(name='factory', left='1100', transparent=True, sizer_border=1, top='70', width='100', 
          font={'style': 'bold', 'size': 80, 'family': 'sans serif', 'face': u'David'}, 
          parent='mywin', text=u':???? ?????', fgcolor=u'#FFFFFF', )
gui.Label(name='bombtype', left='400', transparent=True, sizer_border=1, top='70', width='0', 
          font={'style': 'bold', 'size': 80, 'family': 'sans serif', 'face': u'David'}, 
          parent='mywin', text=bombtype, fgcolor=u'#FFFFFF', )


gui.Label(name='count', left='860', bgcolor='transparent',  transparent=True, sizer_border=1, top='200', width='66', 
          font={'style': 'bold', 'size': 225, 'family': 'sans serif', 'face': u'David'}, 
          parent='mywin', text=bombnum, fgcolor=u'#FFFFFF',  )


gui.Label(name='made', left='1200', bgcolor='transparent', transparent=True, sizer_border=1, top='250', width='66', 
          font={'style': 'bold', 'size': 175, 'family': 'sans serif', 'face': u'David'}, 
          parent='mywin', text=u'??????',fgcolor=u'#FFFFFF',  )
gui.Label(name='bombs', left='115', transparent=True, sizer_border=1, top='250', width='66', 
          font={'style': 'bold', 'size': 175, 'family': 'sans serif', 'face': u'David'}, 
          parent='mywin', text=u'?????',fgcolor=u'#FFFFFF',  )




gui.Label(name='bombpase', left='800', bgcolor='transparent', fgcolor=u'#FFFFFF', transparent=True, sizer_border=1, top='480', width='66', 
          font={'style': 'bold', 'size': 150, 'family': 'sans serif', 'face': u'David'}, 
          parent='mywin', text=bombpase,  )


gui.Label(name='ryth', left='950', bgcolor='transparent', transparent=True, sizer_border=1, top='525', width='66', 
          font={'style': 'bold', 'size': 100, 'family': 'sans serif', 'face': u'David'}, 
          parent='mywin', text=u':??? ????? ?????',  fgcolor=u'#FFFFFF',)
gui.Label(name='hour', left='125', transparent=True, sizer_border=1, top='600', width='66', 
          font={'style': 'bold', 'size': 100, 'family': 'sans serif', 'face': u'David'}, 
          parent='mywin', text=u'????? ????', fgcolor=u'#FFFFFF', )


gui.Label(name='shiftbombpase', left='800', bgcolor='transparent', fgcolor=u'#FFFFFF', transparent=True, sizer_border=1, top='680', width='66', 
          font={'style': 'bold', 'size': 150, 'family': 'sans serif', 'face': u'David'}, 
          parent='mywin', text=bombpase,  )


gui.Label(name='shiftryth', left='950', bgcolor='transparent', transparent=True, sizer_border=1, top='725', width='66', 
          font={'style': 'bold', 'size': 100, 'family': 'sans serif', 'face': u'David'}, 
          parent='mywin', text=u':??? ?????',  fgcolor=u'#FFFFFF',)

gui.Button(label=u'????? ?????', name='zeroshift', left='225', top='775', 
           fgcolor=u'#000000', parent='mywin', visible=True, )

gui.Button(label=u'???? ????', name='addbombb', left='25', top='775', 
           fgcolor=u'#000000', parent='mywin', visible=True, )

gui.Button(label=u'??? ????', name='removebombb', left='125', top='775', 
           fgcolor=u'#000000', parent='mywin', visible=True, )








gui.MenuBar(name='menubar', parent='mywin', )
gui.Menu(name='menu', label=u'????????', parent='mywin.menubar',left='400', )
gui.MenuItem(help=u'??? ????', id=120, name='bombtype', label=u'??? ????', parent='mywin.menubar.menu', )
gui.MenuItem(help=u'???? ??? ??????', id=125, name='menu_edit_count', label=u'???? ??? ??????', parent='mywin.menubar.menu', )
gui.MenuItem(help=u'????? ????', id=126, name='zero', label=u'????? ????', parent='mywin.menubar.menu', )
gui.MenuItem(help=u'????? ?? ???', id=127, name='zeroavg', label=u'????? ?? ???', parent='mywin.menubar.menu', )




gui.Menu(name='countfix', label=u'????? ????', parent='mywin.menubar',left='800', )
gui.MenuItem(help=u'???? ????', id=130, name='addbomb', label=u'???? ????', parent='mywin.menubar.countfix', )
gui.MenuItem(help=u'??? ????', id=131, name='removebomb', label=u'??? ????', parent='mywin.menubar.countfix', )





gui.MenuItemSeparator(id=142, name='menuitemseparator_130', parent='mywin.menubar.menu', )
gui.MenuItem(help=u'?????', id=143, name='exit', label=u'?????', parent='mywin.menubar.menu', )


gui.Label(name='factype', left='50', transparent=True, sizer_border=1, top='150', width='66', 
          font={'style': 'bold', 'size': 20, 'family': 'sans serif', 'face': u'David'}, 
          parent='mywin', text=u':??? ????', visible=False,  )
gui.RadioButton(name='baradplada', label=u'??? ????', left='50px', top='200px', 
                parent='mywin', visible=False, transparent=True, )
gui.RadioButton(name='barad had', label=u'??? ??', left='50px', top='220px', 
                parent='mywin', visible=False, transparent=True, )
gui.RadioButton(name='barad kaved', label=u'??? ???', left='50px', top='240px', 
                parent='mywin', visible=False, transparent=True, )
gui.RadioButton(name='zarit', label=u'?????', left='50px', top='260px', 
                parent='mywin', visible=False, transparent=True, )


gui.Label(name='initi', left='425', transparent=True, sizer_border=1, top='350', width='66', 
          font={'style': 'bold', 'size': 100, 'family': 'sans serif', 'face': u'David'}, 
          parent='mywin', text=u':???? ????? ?? ???', visible=False,  )

gui.TextBox(name='edit_count', border='none', transparent=True, height='100', 
            left='800', top='500', width='250', fgcolor=u'#000000', visible=False,
            font={'size': 100, 'family': 'sans serif', 'face': u'David'}, 
            helptext=u'', parent='mywin', )

gui.Button(label=u'????', name='load', left='935', top='625', 
           fgcolor=u'#000000', parent='mywin', visible=False, )
gui.Button(label=u'???', name='cans', left='825', top='625', 
           fgcolor=u'#000000', parent='mywin', visible=False, )


 
# --- gui2py designer generated code ends ---


mywin = gui.get("mywin")

mywin.onload = load
mywin['menubar']['menu']['exit'].onclick = Exit
mywin['menubar']['menu']['zero'].onclick = zero
mywin['menubar']['menu']['zeroavg'].onclick = zeroavg
mywin['menubar']['menu']['bombtype'].onclick = bombt
mywin['menubar']['menu']['menu_edit_count'].onclick = menu_edit_count



mywin['menubar']['countfix']['addbomb'].onclick = addbomb
mywin['menubar']['countfix']['removebomb'].onclick = removebomb



mywin['barad had'].onclick = baradhad
mywin['barad kaved'].onclick = baradkaved
mywin['zarit'].onclick = zarit
mywin['baradplada'].onclick = baradplada


mywin['load'].onclick = count_load
mywin['cans'].onclick = cans

mywin['zeroshift'].onclick = zeroshift
mywin['addbombb'].onclick = addbomb
mywin['removebombb'].onclick = removebomb





if __name__ == "__main__":
    
    print 'lets begin'

    

    thread.start_new_thread(logicloop, (5,))
    #thread.start_new_thread(counter, (5,))
   
    
 
    mywin.show()
    mywin.title = u"???? ????? ????? ?????"
    mywin['statusbar'].text = u"????? ????? ????: %s" % (time.ctime()) 

  
    
    gui.main_loop()




