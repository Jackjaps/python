#!/usr/bin/python
import argparse
import sys
import os
import jaydebeapi
#hadoop fs -copyFromLocal localpath hdfspath
def getListhlog(args):
    dsn_database = "postgres"
    dsn_hostname = "localhost"
    dsn_port = "5432"
    postgresql_user = 'admin'
    postgresql_pw = 'admin'
    postgresql_class = 'org.postgresql.Driver'
    try:
        postgresql_jdbc_path = os.path.join(r'/Users/jacobomunoz/Documents/ingenieria/drivers/postgresql-42.2.18.jar')
        postgresql_url = 'jdbc:postgresql://{}:{}/{}'.format(dsn_hostname,dsn_port,dsn_database)
        print(postgresql_url)
        print(postgresql_jdbc_path)
        conn = jaydebeapi.connect(postgresql_class, 
                    postgresql_url, 
                    [postgresql_user, postgresql_pw], 
                    postgresql_jdbc_path)
        sql_query = "SELECT * FROM cms.hlog"
        print(sql_query)
        curs = conn.cursor()
        curs.execute(sql_query)
        dl = curs.fetchall()
        print(dl)
    except (Exception) as error :
        if(conn):
            print("Error on selection ", error)
    finally: 
        #closing database connection.
        if(conn):
            #cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

def loadHadoop(args):
    ...

def main():
    #python3 main_with_perameters.py -t cms.hlog -f hlog.csv -p hdfs://hacluster/user/load
    parser = argparse.ArgumentParser(description="Post indexing tasks")
    parser.add_argument('--table','-t',type=str,required=True,default='sysdate',help="Name of the extract table")
    parser.add_argument('--tfile','-f',type=str,required=True,default='sysdatete',help="Name of temp file to be loaded to HDFS")
    parser.add_argument('--hpath','-p',type=str,required=True,default='sysdate',help="Hadoop path")
    args= parser.parse_args()
    pathname = os.getcwd()
    print(args.table)
    print(args.tfile)
    print(args.hpath)
    print(pathname)
    getListhlog(args)

try:
    main()
except KeyboardInterrupt:
    sys.exit(1)
