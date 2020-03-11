from APIs.conn import connob
import json
from pyzabbix import ZabbixAPIException

class HostDelete:

    def __init__(self, connob):
        self.conn = connob
        self.method = "host.delete"

    def deleteHost(self,hids:list):
        paramater = hids
        try:
            result = self.conn.do_request(self.method, paramater)
            return True
        except ZabbixAPIException as ze:
            print(ze)
            return False
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    hd = HostDelete(connob)
    testhid = [103456]
    print(hd.deleteHost(testhid))
