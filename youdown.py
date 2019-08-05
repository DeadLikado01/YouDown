#!/usr/bin/python
#-*- coding: UTF-8 -*-
# DOWNLOAD VIDEOS OF YOUTUBE FREE
# CREATE BY : SR BERNS
# SAMUEL RAMIREZ
# REAL SOCIETY
# __________________
from os import system
system('clear')
print("""\033[1;95m
        __  __         ______     __
        \ \/ /__  __ _/_  __/_ __/ /  ___
         \  / _ \/ // // / / // / _ \/ -_)
         /_/\___/\_,_//_/  \_,_/_.__/\__/
             ___                  __                __
            / _ \___ _    _____  / /  ___  ___ ____/ /
           / // / _ \ |/|/ / _ \/ /__/ _ \/ _ `/ _  /
          /____/\___/__,__/_//_/____/\___/\_,_/\_,_/
  \033[1;37;32mBy Samuel Ramirez\033[96m R341 S0C137Y\033[1;32m

    YOUTUBE DOWNLOAD VIDEOS  BY \033[1;46;43;41;36;32;32;35mSR BERNS\033[0m-\033[1;34m
              \033[0m """)
try:
    print "\033[1;32mEXAMPLE URL : https://youtu.be/NeaSokjhz4s "
    url = raw_input("\033[1;35mURL :: ")
    audio = raw_input("AUDIO format :: ")
    print "\033[1;32mDescargando Archivo\033[0m"
    system('youtube-dl --netrc --merge-output-format=mp4 --audio-format=%s --download-archive="youdown.mp4"  %s'% (audio, url))
    print "\033[1;36mARCHIVO DESCARGADO\033[0m"
except KeyboardInterrupt as a:
    print "\033[1;46;43m[\033[1;31m!\033[1;46;43m]\033[0m\033[1;32m CTRL KEYBOARD !!"
except exceptions.ConnectionError as a:
    print "\033[1;35mError en la Coneccion !!\033[0m"
except ERROR as a:
    print "ERROR IN THE CONECTION"
try:
    print "Exit or Return"
    s = raw_input("E/R :: ")
    if s == 'E' or s == 'e':
        print("Exit ....")
        print("Good Bye")
        exit()
    if s == 'R' or s == 'r':
        system('python2 you')
    print "Buscar Videos Y/N"
    y = raw_input("Yes Or Not Y/N :")
    if y == 'Y' or y == 'y':
        print "Intrododuce el nombre del video que intentas buscar"
        video = raw_input("Name Of Video :")
        print "Iniciando Busqueda de %s"% video
        system('youtube-dl ytsearch:"%s"'% (video))
except KeyboardInterrupt as a:
    print "\033[1;46;43m[\033[1;31m!\033[1;46;43m]\033[0m\033[1;32m CTRL KEYBOARD !!"
