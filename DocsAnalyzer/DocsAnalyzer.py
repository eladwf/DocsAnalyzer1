import  rtfobj
import sys
from os import getenv
import sqlite3
import SqlHandler

def main():
    data= open(sys.argv[1],"rb").read()
    #validate args
    ##if args is valid, init SQL and parse rtf file:
    sqlhanlder= SqlHandler.SqlHandler("address/db")
    rtfp = rtfobj.RtfParser(data)
    rtfp.parse()
    #parser checks all relevant cwords by sending parameters to server and checking if they are in the normal range
    #return alert if "suspicious" cword found, else ok 


if __name__ == "__main__":
    main()
