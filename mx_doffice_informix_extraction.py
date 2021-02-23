import jaydebeapi, sys
import base64 
import pandas as pd 
#Enter the values for you database connection
dsn_database2 = "cms"            # e.g. "BLUDB"
dsn_hostname2 = "148.250.233.183" # e.g.: "hostname.site.com"
dsn_port2 = "50000"                # e.g. "50000"
dsn_uid2 = "ecommerc"        # e.g. "dash104434"
dsn_pwd = "V2FsbWFydDIwMjE="       # e.g. "7dBZ3jWt9xN6$o0JiX!m"
ifxserver = "cms_net"

#Decode Password
dsn_pwd2 = base64.decodebytes(dsn_pwd.encode()).decode()
#Connection string
connection_string2='jdbc:informix-sqli://'+dsn_hostname2+':'+dsn_port2+'/'+dsn_database2+':INFORMIXSERVER='+ifxserver+';user='+dsn_uid2+';password='+dsn_pwd2+";"
if (sys.version_info >= (3,0)):
    conn = jaydebeapi.connect("com.informix.jdbc.IfxDriver", connection_string2, [dsn_uid2, dsn_pwd2],jars="C:\\Users\\vn0tzya\\Documents\\Codes\\drivers\\ifxjdbc-3.50.JC3.jar")
curs = conn.cursor()
#/u/users/appaorta/AORTA/jars/informix/ifxjdbc-3.50.JC3.jar

#Set Query filters
qry= "select first 10 * from cms:haglog where row_date = TO_DATE('2020-10-01','%Y-%m-%d')"
curs.execute(qry)
results = curs.fetchall()
print(type(results))
#df = pd.DataFrame(results)
#print(df)
curs.close()
conn.close()


