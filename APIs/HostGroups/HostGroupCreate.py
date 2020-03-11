from APIs.conn import connob
import json
from pyzabbix import ZabbixAPIException
class HostGroupCreate:
    def __init__(self,conn):
        self.conn = conn
        self.method = "hostgroup.create"

    def createGroup(self,groupName):
        params = {"name":groupName}
        try:
            response = self.conn.do_request(self.method,params)
            print(json.dumps(response,indent=1))
            return True,response['result']['groupids']

        except ZabbixAPIException as e :
            print(e)
            return False

    def deleteGroup(self,gids):
        if type(gids) != list : return  False
        for gid in gids :
            if int(gid)<=14 : return False

        params = gids
        try:
            response = self.conn.do_request("hostgroup.delete",params)
            # print(json.dumps(response,indent=1))
            return True
        except ZabbixAPIException as e :
            # print(e)
            return False

if __name__ == '__main__':
    hgc = HostGroupCreate(connob)
    # hgc.createGroup("C3_SIT2")
    print(hgc.deleteGroup([20]))