#!/bin/bash
#./pentafonsh.sh -a MyStorageAccount -s hdfs://hadoopfs/ -t adls://aldsfs/ -k bGludXhoaW50LmNvbQo=
# base64 -d "bGludXhoaW50LmNvbQo="
while getopts a:s:t:k: flag
do
    case "${flag}" in
        a) storageaccount=${OPTARG};;
        s) source=${OPTARG};;
        t) target=${OPTARG};;
        k) key=${OPTARG};;
    esac
done
#echo "Storage Account Name: $storageaccount";
#echo "Source file System: $source";
#echo "Target file System: $target";
#echo "Access Key: $key";
dkey=`echo -n $key | base64 --decode`
#echo "Dcripted key: $dkey"; 
export ACCOUNT=$storageaccount
export KEY=$dkey
export JARS="/u/users/"
echo "hadoop distcp -libjars $JARS \
      -D fs.abfss.impl=SABS \
      -D fs.Abstract \
      -D fd.azure.account.key.$ACCOUNT.dfs.core.windows.net=$KEY \
      -update \
      $source \
      $target"
sleep 10
exit 0