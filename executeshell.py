import argparse
import sys
import os
import subprocess

def executedistCP(args):
    cmd = "./pentafonsh.sh -a {} -s {} -t {} -k {}".format(args.adls,args.source,args.target,"bGludXhoaW50LmNvbQo=")
    popen = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
    lines_iterator = iter(popen.stdout.readline, b"")
    while popen.poll() is None:
        for line in lines_iterator:
            nline = line.rstrip()
            print(nline.decode("latin"), end = "\r\n",flush =True) # yield line

def main():
    #/pentafonsh.sh -a  -s  -t  -k bGludXhoaW50LmNvbQo=
    #python3 executeshell.py -a MyStorageAccount -s hdfs://hadoopfs/ -t adls://aldsfs/ 
    parser = argparse.ArgumentParser(description="Post indexing tasks")
    parser.add_argument('--adls','-a',type=str,required=True,default='default',help="Name of the storage account")
    parser.add_argument('--source','-s',type=str,required=True,default='sysdate',help="to HDFS")
    parser.add_argument('--target','-t',type=str,required=True,default='sysdate',help="Hadoop path")
    args= parser.parse_args()
    pathname = os.getcwd()
    print(executedistCP(args)) 
try:
    main()
except KeyboardInterrupt:
    sys.exit(1)