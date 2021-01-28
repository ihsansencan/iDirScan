#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import argparse
import sys

print('\033[93m'+"""
########################################
#       +-+-+-+-+-+-+-+-+-+-+-+-+      #
#       |*|*|i|D|i|r|S|c|a|n|*|*|      #
#       +-+-+-+-+-+-+-+-+-+-+-+-+      #
#   github.com/ihsansencan/iDirScan    #
#             @IhsanSencan             #
########################################
"""+'\x1b[0m')

arg = argparse.ArgumentParser()
arg.add_argument("-s", "--site", required=True, type=str, metavar="site", help="Enter the site address.")
arg.add_argument("-l", "--list", required=True, type=str, metavar="file", help="Enter the file path.")

args = vars(arg.parse_args())

def iDirScan():
    count =0
    dosya = open(args["list"], "r", encoding="latin-1")
    listem = dosya.read()
    with open(args["list"], "r", encoding="latin-1") as f:
        print(f"In total\033[91m\033[1m",f.read().count("\n"),"\033[0mtrying will be done.")
        print(25*"*")
    dosya.close()
    try:
        for i in listem.split("\n"):
            url = "http://"+args["site"]+"/"+str(i)
            sonuc = requests.get(url=url)

            if not "404" in str(sonuc.status_code):
                print(f"\033[32m[{count}] {url} \033[0m(Code:{sonuc.status_code}|Size:{len(sonuc.content)})")
            else:
                sys.stdout.write("Trying: "+str(count)+"\r")
                sys.stdout.flush()
                count+=1
    except requests.exceptions.RequestException:
        print("\033[91m\033[1mCould not connect to the site !\033[0m : "+args["site"])
try:
    iDirScan()
except FileNotFoundError:
    print("\033[91m\033[1mNo such file found !\033[0m : "+args["list"])
    print('Usage : python3 '+__file__.split('/')[-1:][0]+' -s localhost -l common.txt')