from APIs.conn import connob
import json
from pyzabbix import ZabbixAPIException
class HostGroupUpdate:

    def __init__(self, connob):
        self.conn = connob
        self.method = "hostgroup.update"

    def renameHostGroup(self,gid,newname):
        params = {
            "groupid":gid,
            "name":newname
        }
        try :
            response = self.conn.do_request(self.method,params)
            # print(json.dumps(response,indent=1))
            return True
        except ZabbixAPIException as e :
            print(e.args[0])
            return False
        except Exception as e :
            return  False


if __name__ == '__main__':
    hgu = HostGroupUpdate(connob)
    hgu.renameHostGroup(18,"C3_UAT")