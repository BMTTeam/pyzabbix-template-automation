from Utils.utilfun import checkFileExist
from configparser import ConfigParser
from pyzabbix import ZabbixAPI
import os
from Utils.myLogger import getMyLogger
from settings import  PROPERTIES_DIR
#######----------------------------------------------------------###########
conn_logger = getMyLogger("connections.log","zabb_connection ->")
#######----------------------------------------------------------###########
filepath = os.path.join(PROPERTIES_DIR,"credentials.ini")


def getInformation(conn):
    print("Version : ", conn.api_version())
    print("Authenication : ", conn.auth)
    print("Url : ", conn.url)

def getconnection():
    # check if file properties file exists or not . If Exist then only move forward
    if checkFileExist(filepath):
        parser = ConfigParser()
        parser.read(filepath)

        if 'user' in parser['credentials']:
            username = parser['credentials'].get('user')
            # As we get the value with quote around we have to strip them from string
            username = username.strip("'")  # 'vegtio' to vegtio
        if 'password' in parser['credentials']:
            password = (parser['credentials']['password']).strip("'")
        if 'url' in parser['credentials']:
            url = (parser['credentials']['url']).strip("'")

        try:
            # zapi = ZabbixAPI(url=url, user=username, password=password)
            zapi = ZabbixAPI(server=url)
            zapi.login(user=username , password=password)
            conn_logger.info(" Successfully connected to Zabbix Master " + parser['credentials'].get('env'))
            return zapi

        except BaseException as e:
            # print(e)
            conn_logger.exception(e)
            return False

    else:
        print(" properties File does not exists ")
        return False


connob = getconnection()
# logging.info(connob)

if __name__ == '__main__':
    if connob:
        print("Successfully connected")
        getInformation(connob)

    else:
        print(connob)
        print(" Failed to connect !!! ")