from APIs.conn import connob
import json
from pyzabbix import ZabbixAPIException


class TemplateDetails:
    def __init__(self, conn):
        self.conn = conn
        self.method = "template.get"

    def getAllTemplates(self):
        params = {"output": ["status", "name", "description"]}
        try:
            response = self.conn.do_request(self.method, params)
            # print(json.dumps(response['result'],indent=1))
            return response['result']
        except ZabbixAPIException as e:
            print(e)
            return []

    def getUserCreatedTemplate(self, onlyIds=False):
        params = {
            "output": ["templateid", 'name'],
            "selectMacros": ["macro", "value"]
        }
        if onlyIds:
            params = {
                "output": ["templateid"],
            }
            response = self.conn.do_request(self.method, params)
            userCreated = list(filter(lambda group: int(group['templateid']) > 10330, response['result']))
            return [id["templateid"] for id in userCreated]
        else:
            response = self.conn.do_request(self.method, params)
            userCreated = list(filter(lambda group: int(group['templateid']) > 10330, response['result']))
            # print(json.dumps(userCreated,indent=1))
        return userCreated

    def getTemplateDetails(self, tid=0, tname=""):
        params = {
            "output": ["host", "status", "templateid", "description"],
            "selectItems": ['name', 'type', 'description', 'history', 'status', 'delay', "type", "key_", "value_type"],
            "selectMacros": ['macro', 'value'],
        }
        if tname != "":
            params['search'] = {"name": tname}
            # params['search'] = {"host": tname}
        else:
            params['templateids'] = tid

        response = self.conn.do_request(self.method, params)

        if not response['result']: return []
        # print(json.dumps(userCreated,indent=1))
        return response['result'][0]

    def getMACROSListRelatedToTemplate(self, tid=0, tname=""):
        params = {
            "output": ['templateid', 'name'],
            "selectMacros": ["macro", 'value'],
        }
        if tname != "":
            params['search'] = {"name": tname}
            # params['search'] = {"host": tname}
        else:
            params['templateids'] = tid
        response = self.conn.do_request(self.method, params)

        if response['result'] == [] : return []
        # print(json.dumps(userCreated,indent=1))
        return response['result'][0]['macros']

    def getItemListRelatedToTemplate(self, tid=0, tname=""):
        params = {
            "output": ['templateid', 'name'],
            "selectItems": ['name', 'type', 'description', 'history',"trends",'status', 'delay', "type", "key_", "value_type","itemid"],
            # "selectItems": "extend"
        }
        if tname != "":
            params['search'] = {"name": tname}
            # params['search'] = {"host": tname}
        else:
            params['templateids'] = tid
        response = self.conn.do_request(self.method, params)

        if response['result'] == [] : return []
        # print(json.dumps(userCreated,indent=1))
        return response['result'][0]['items']

    def getTriggersRelatedToTemplates(self, tid=0, tname=""):
        params = {
            "output": ['templateid', 'name'],
            "selectTriggers": ['triggerid', 'expression', 'description', 'priority',"comments"],
            # "selectTriggers": "extend"
        }
        if tname != "":
            params['search'] = {"name": tname}
            # params['search'] = {"host": tname}
        else:
            params['templateids'] = tid
        response = self.conn.do_request(self.method, params)

        if response['result'] == [] : return []
        # print(json.dumps(userCreated,indent=1))
        return response['result'][0]['triggers']

    def getHostsRelatedToTemplates(self, tid=0, tname=""):
        params = {
            "output": ['templateid', 'name'],
            "selectHosts": ['hostid', 'host', 'available', 'name',"error"],
            # "selectHosts": "extend"
        }
        if tname != "":
            params['search'] = {"name": tname}
            # params['search'] = {"host": tname}
        else:
            params['templateids'] = tid
        response = self.conn.do_request(self.method, params)

        if response['result'] == [] : return []
        # print(json.dumps(userCreated,indent=1))
        return response['result'][0]['hosts']

    def getTemplateName(self,tid):
        params = {
            "output": ['name'],
            'templateids': tid
            # "selectHosts": "extend"
        }
        response = self.conn.do_request(self.method, params)
        if response['result'] == [] : return None

        return response['result'][0]['name']

    def getTemplateId(self,tname):
        params = {
            "output": ['templateid'],
            'search': {"name":tname}
            # "selectHosts": "extend"
        }
        response = self.conn.do_request(self.method, params)
        if response['result'] == [] : return None

        return response['result'][0]['templateid']

    def getItemCount(self, tid=0, tname=""):
        params = {
            "output": ['templateid', 'name'],
            "selectItems": "count"
        }
        if tname != "":
            params['search'] = {"name": tname}
            # params['search'] = {"host": tname}
        else:
            params['templateids'] = tid
        response = self.conn.do_request(self.method, params)

        if response['result'] == [] : return 0
        # print(json.dumps(userCreated,indent=1))
        return response['result'][0]['items']

if __name__ == '__main__':
    td = TemplateDetails(connob)
    # test_tmp_id = 10330
    test_tmp_id = 10001
    test_tmp_name = "TEMPLATE_1 Tomcat_Process_Monitorin"
    # print(json.dumps(td.getAllTemplates(),indent=1))

    # print(json.dumps(td.getUserCreatedTemplate(),indent=1))
    print(json.dumps(td.getUserCreatedTemplate(True), indent=1))

    # print(json.dumps(td.getTemplateDetails(test_tmp_id), indent=1))
    # print(json.dumps(td.getTemplateDetails(tname=test_tmp_name), indent=1))

    # print(json.dumps(td.getMACROSListRelatedToTemplate(test_tmp_id), indent=1))
    # print(json.dumps(td.getMACROSListRelatedToTemplate(tname=test_tmp_name), indent=1))

    # print(json.dumps(td.getItemListRelatedToTemplate(test_tmp_id), indent=1))
    # print(json.dumps(td.getItemListRelatedToTemplate(tname=test_tmp_name), indent=1))

    # print(json.dumps(td.getTriggersRelatedToTemplates(test_tmp_id), indent=1))
    # print(json.dumps(td.getTriggersRelatedToTemplates(tname=test_tmp_name), indent=1))

    # print(json.dumps(td.getHostsRelatedToTemplates(test_tmp_id), indent=1))
    # print(json.dumps(td.getHostsRelatedToTemplates(tname="Linux"), indent=1))

    # print(td.getTemplateName(10331))
    # print(td.getTemplateName(123344134))

    # print(td.getTemplateId("linux"))
    # print(td.getTemplateId("weqwe"))

    # print(td.getItemCount(test_tmp_id))
    # print(td.getItemCount(234))
    # print(td.getItemCount(tname="Linux"))
    # print(td.getItemCount(tname="wceff"))

