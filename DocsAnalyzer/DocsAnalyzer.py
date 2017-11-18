import  rtfobj
import sys
from os import getenv
import MySQLdb
import sql

def main():
    data= open(r"C:\Users\Elad\Documents\DocsAnalyzer\d.rtf","rb").read()
    #validate args
    ##if args is valid, init SQL and parse rtf file:
    sqlhand= sql.SqlHandler()
    sqlhand.insert(1,2)
    rtfp = rtfobj.RtfParser(data)
    rtfp.parse()
    #parser checks all relevant cwords by sending parameters to server and checking if they are in the normal range
    #return alert if "suspicious" cword found, else ok 


if __name__ == "__main__":
    main()
