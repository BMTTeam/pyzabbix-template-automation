from APIs.conn import connob
import json
from pyzabbix import ZabbixAPIException


class TemplateUpdate:
    def __init__(self, conn):
        self.conn = conn

    def addNewMacroToTemplates(self, tids, macDictList):
        """

        :param tids: It is List of Template Ids to Modify
        :param macDictList:  It is List of Macros Dict it should be like in following format
            dicList = [{"HIGH":12},{"Key":"Value"} ]
            It will not add any Macros even if any one of Macros in Given List is already Exists
        :return: Return True if we SuccessFully add the new Macros to give Template else False
        """
        method = "template.massadd"
        templates = [{"templateid": tid} for tid in tids]

        def toMacros(macdict):
            for key, value in macdict.items(): return {"macro": "{$" + key + "}", "value": value}

        macros = list(map(toMacros, macDictList))

        params = {
            "templates": templates,
            "macros": macros
        }
        try:
            response = self.conn.do_request(method, params)
            # print(json.dumps(response['result'],indent=1))
            return True
        except ZabbixAPIException as e:
            # print(e)
            return False

    def addNewGroupToTemplates(self, tids: list, groupidList: list):
        method = "template.massadd"
        templates = [{"templateid": tid} for tid in tids]
        groups = [{"groupid": gid} for gid in groupidList]

        params = {
            "templates": templates,
            "groups": groups
        }
        try:
            response = self.conn.do_request(method, params)
            print(json.dumps(response['result'], indent=1))
            return True
        except ZabbixAPIException as e:
            print(e)
            return False

    def addGroupAndMacroFromTemplates(self, tids, groupidList: list, macDictList: list):

        def toMacros(macdict):
            for key, value in macdict.items(): return {"macro": "{$" + key + "}", "value": value}

        method = "template.massadd"
        templates = [{"templateid": tid} for tid in tids]
        groups = [{"groupid": gid} for gid in groupidList]
        macros = list(map(toMacros, macDictList))

        params = {
            "templates": templates,
            "macros": macros,
            "groups": groups
        }
        try:
            response = self.conn.do_request(method, params)
            # print(json.dumps(response['result'],indent=1))
            return True
        except ZabbixAPIException as e:
            # print(e)
            return False

    def addTemplatesToHosts(self, templateidList: list, hostIdList: list):
        method = 'template.massadd'
        templates = [{"templateid": tid} for tid in templateidList]
        hosts = [{"hostid": hid} for hid in hostIdList]
        params = {
            "templates": templates,
            "hosts": hosts
        }
        try:
            response = self.conn.do_request(method, params)
            print(json.dumps(response['result'], indent=1))
            return True
        except ZabbixAPIException as e:
            print(e)
            return False

    def removeMacroFromTemplates(self, tids: list, macroKeys: list):
        """

        :param tids: It is List of Templated Ids to Modify
        :param macroKeys:  It is List of Macros key List it should be like in following format
            dicList = ["HIGH","LOW","NAME"]
            - It will delete if Given Templates contain any one of the Macros Key
            - It will not delete of if All Macros in list are not present in Template
        :return: Return True if we SuccessFully removed the Macros from given Template else False
        """
        method = "template.massremove"
        macros = ["{$" + key + "}" for key in macroKeys]

        params = {
            "templateids": tids,
            "macros": macros
        }
        try:
            response = self.conn.do_request(method, params)
            # print(json.dumps(response['result'],indent=1))
            return True
        except ZabbixAPIException as e:
            # print(e)
            return False

    def removeGroupFromTemplate(self, tids: list, groupidList: list):
        method = "template.massremove"
        params = {
            "templateids": tids,
            "groupids": groupidList
        }
        try:
            response = self.conn.do_request(method, params)
            # print(json.dumps(response['result'], indent=1))
            return True
        except ZabbixAPIException as e:
            # print(e)
            return False

    def renameTemplate(self, tid: int, visibleName, newName: str = ""):
        method = "template.update"
        if not newName:
            newName = visibleName
        params = {
            "templateid": tid,
            "name": visibleName,
            "host": newName
        }
        try:
            response = self.conn.do_request(method, params)
            # print(json.dumps(response['result'], indent=1))
            return True
        except ZabbixAPIException as e:
            # print(e)
            return False

    def removeTemplatesFromHosts(self, templateidList: list, hostIdList: list):
        method = 'template.massremove'
        params = {
            "templateids": templateidList,
            "hostids": hostIdList
        }
        try:
            response = self.conn.do_request(method, params)
            print(json.dumps(response['result'], indent=1))
            return True
        except ZabbixAPIException as e:
            print(e)
            return False


if __name__ == '__main__':
    tu = TemplateUpdate(connob)

    dicList = [{"HIGH": 12}, {"TES1": 56}, {"TEST2": 45}]
    groupList = [16, 18]
    test_tmp_ids = [10335]
    test_host_id = [10325]
    macList = ["TES1", "TEST2", "HIGH"]
    tmpList = [10336, 10338, 10335, 10334]
    test_hostIdList = ['10325', '10327', '10330']

    # print(tu.addNewMacroToTemplates(test_tmp_ids, dicList))

    # print(tu.addNewGroupToTemplates(test_tmp_ids, groupList))

    # print(tu.addGroupAndMacroFromTemplates(test_tmp_ids, groupList, dicList))

    # print(tu.removeMacroFromTemplates(test_tmp_ids, macList))

    # print(tu.removeGroupFromTemplate(test_tmp_ids, [18, 56]))

    # print(tu.renameTemplate(10335, "Test Rename Template"))

    # print(tu.addTemplatesToHosts(tmpList, test_hostIdList))

    # print(tu.removeTemplatesFromHosts(tmpList, test_hostIdList))
