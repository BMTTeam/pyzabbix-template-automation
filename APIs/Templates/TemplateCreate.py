from APIs.conn import connob
import json
from pyzabbix import ZabbixAPIException


class TemplateCreate:
    def __init__(self, conn):
        self.conn = conn
        self.method = "template.create"

    def createTemplate(self, tname, gidList=[2], macDict={}):
        macros = [{"macro": "{$" + key + "}", "value": value, "description": "Desc " + str(value)} for key, value in
                  macDict.items()]
        groups = [{"groupid": gid} for gid in gidList]
        params = {
            "host": tname,
            'macros': macros,
            "groups": groups,
        }
        try:
            response = self.conn.do_request(self.method, params)
            # print(json.dumps(response['result'],indent=1))
            return True
        except ZabbixAPIException as e:
            # print(e)
            return False

    def deleteTemplate(self,tids:list):
        """

        :param tids: List of All template ids If even template id is invalid or not exist then will return False
        :return: True If successfully delete templates else False
        """
        params = tids
        try:
            response = self.conn.do_request("template.delete", params)
            # print(json.dumps(response['result'],indent=1))
            return True
        except ZabbixAPIException as e:
            # print(e)
            return False

if __name__ == '__main__':
    tc = TemplateCreate(connob)
    tmpIds = [10338]
    # tc.createTemplate("Test Template 2",[2,123],{"LOW":10,"HIGH":43})
    # print(tc.createTemplate("Test Template 4", [2], {"LOW": 10, "HIGH": 43}))
    print(tc.deleteTemplate(tmpIds))