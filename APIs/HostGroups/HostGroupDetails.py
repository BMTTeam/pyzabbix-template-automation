from APIs.conn import connob
import json
from pyzabbix import ZabbixAPIException
class HostGroupsDetails:
    def __init__(self,conn):
        self.conn = conn
        self.method = "hostgroup.get"

    def getAllHostGroups(self):
        params = {
            "output" : ["groupid",'name',"internal"]
        }
        response = self.conn.do_request(self.method,params)
        # print(json.dumps(response['result'],indent=1))
        return response['result']

    def getUserCreatedHostGroups(self):
        params = {
            "output" : ["groupid",'name']
        }
        response = self.conn.do_request(self.method,params)
        userCreated = list(filter(lambda group: int(group['groupid']) > 14 ,response['result']))
        # print(json.dumps(userCreated,indent=1))
        return userCreated

    def getUsedHostGroups(self):
        """Return only host groups that contain hosts."""
        params = {
            "output" : ["groupid",'name',"real_hosts"],
            "real_hosts": "extend"
        }
        response = self.conn.do_request(self.method,params)
        print(json.dumps(response['result'],indent=1))
        return response['result']

    def getHostAssociatedHG(self, groupid=2, groupname="", onlyHids=False):
        params = {
            "output" : ["groupid",'name',"real_hosts"],
            "selectHosts":["name","id"],
        }
        if groupname!="":
            params['search'] = {"name":groupname}
        else:
            params['groupids'] = [groupid]

        response = self.conn.do_request(self.method,params)

        if response['result']==[]: return []

        if onlyHids:
           return [ host["hostid"] for host in response["result"][0]["hosts"] ]
        # print(json.dumps(response['result'],indent=1))
        return response['result'][0]['hosts']

    def getTemplateAssociatedHG(self, groupid=2, groupname="", onlyTempids=False):

        params = {
            "output" : ["groupid",'name',"real_hosts"],
            "selectTemplates":["name","templateid"],
        }
        if groupname!="":
            params['search'] = {"name":groupname}
        else:
            params['groupids'] = [groupid]

        response = self.conn.do_request(self.method,params)

        if response['result']==[]: return []

        if onlyTempids:
           return [ host["templateid"] for host in response["result"][0]["templates"] ]
        # print(json.dumps(response['result'],indent=1))
        return response['result'][0]['templates']

if __name__ == '__main__':
    hgd = HostGroupsDetails(connob)
    # print(hgd.getAllHostGroups())
    # print(hgd.getUserCreatedHostGroups())
    # print(hgd.getUsedHostGroups())

    # print(hgd.getHostAssociatedHG())
    # print(hgd.getHostAssociatedHG(onlyHids=True))
    # print(hgd.getHostAssociatedHG(groupname="Linux"))

    # print(hgd.getTemplateAssociatedHG())
    # print(hgd.getTemplateAssociatedHG(onlyTempids=True))
    # print(hgd.getTemplateAssociatedHG(groupname="Linux"))

