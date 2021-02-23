#!/usr/bin/python
import argparse
import sys
import os
from datainformix import dataInformix
#hadoop fs -copyFromLocal localpath hdfspath

def getListhlog(args):
    sql_query = "SELECT * FROM {} where row_date = '{}'".format(args.table,args.date)
    try:
        db = dataInformix()
        listData = db.query(sql_query)
        db.close()
        return listData
    except(Exception) as error:
        print("Error: " ,error)
        db.close()
        
def createFile(args,listDF):
    ...

def loadHadoop(args):
    ...

def main():
    #python3 main_with_parameters.py -t cms.hlog -p hdfs://hacluster/user/load -d 2021-02-13 -f hlog.csv 
    parser = argparse.ArgumentParser(description="Post indexing tasks")
    parser.add_argument('--table','-t',type=str,required=True,default='sysdate',help="Name of the extract table")
    parser.add_argument('--tfile','-f',type=str,required=True,default='sysdate',help="Name of temp file to be loaded to HDFS")
    parser.add_argument('--hpath','-p',type=str,required=True,default='sysdate',help="Hadoop path")
    parser.add_argument('--date','-d',type=str,required=True,default='sysdate',help="Process date YYYY-MM-DD")
    args= parser.parse_args()
    pathname = os.getcwd()
    print(getListhlog(args)) 
try:
    main()
except KeyboardInterrupt:
    sys.exit(1)
