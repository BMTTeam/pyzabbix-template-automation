from APIs.conn import connob
import json
from pyzabbix import ZabbixAPIException


class HostUpdate:

    def __init__(self, connob):
        self.conn = connob
        self.method = "host.update"
        # print(self.conn)

    def addHostGroupsToHosts(self, hostidList: list, groupidList: list):
        method = "host.massadd"
        hosts = [{"hostid": hid} for hid in hostidList]
        # templates = [{"templateid": tid} for tid in templateidList]
        groups = [{"groupid": gid} for gid in groupidList]
        params = {
            "hosts": hosts,
            "groups": groups
        }

        try:
            result = self.conn.do_request(method, params)
            return True
        except ZabbixAPIException as ze:
            print(ze)
            return False

        except Exception as e:
            print(e)
            return False

    # Even there is one Hostid or Template ID is not exist it will not add this template
    def addTemplatesToHosts(self, hostidList: list, templateidList: list):
        method = "host.massadd"
        hosts = [{"hostid": hid} for hid in hostidList]
        templates = [{"templateid": tid} for tid in templateidList]
        params = {
            "hosts": hosts,
            "templates": templates
        }

        try:
            result = self.conn.do_request(method, params)
            return True
        except ZabbixAPIException as ze:
            # print(ze)
            return False

        except Exception as e:
            # print(e)
            return False

    # It will not add any Macros even if any one of Macros in Given List is already Exists in that Host
    def addNewMacrosToHosts(self, hostidList: list, macDictList: list):
        """
        :param hostidList: All Hosid in list should be exists
        :param macDictList:
            dicList = [{"HIGH":12},{"Key":"Value"} ]
        :return:
        """
        method = "host.massadd"

        def toMacros(macdict):
            for key, value in macdict.items(): return {"macro": "{$" + key + "}", "value": value}

        macros = list(map(toMacros, macDictList))
        hosts = [{"hostid": hid} for hid in hostidList]
        params = {
            "hosts": hosts,
            "macros": macros
        }

        try:
            result = self.conn.do_request(method, params)
            return True
        except ZabbixAPIException as ze:
            # print(ze)
            return False

        except Exception as e:
            # print(e)
            return False

    # All Template Id and Group Id and Hostid should be exists even of one Id is not exists then it will
    # It is valid if we given [] list it will add other parameters
    def addTemplate_HGS_Macros_ToHosts(self, hostidList: list, templateidList: list = [], groupidList: list = [],
                                       macDicList=[]):
        method = "host.massadd"

        hosts = [{"hostid": hid} for hid in hostidList]
        templates = [{"templateid": tid} for tid in templateidList]
        groups = [{"groupid": gid} for gid in groupidList]

        def toMacros(macdict):
            for key, value in macdict.items(): return {"macro": "{$" + key + "}", "value": value}

        macros = list(map(toMacros, macDicList))

        params = {
            "hosts": hosts,
            "templates": templates,
            "groups": groups,
            "macros": macros
        }

        try:
            result = self.conn.do_request(method, params)
            return True
        except ZabbixAPIException as ze:
            # print(ze)
            return False

        except Exception as e:
            # print(e)
            return False

    def addJmxInterfaceToHost(self, hostidList: list, ip: str, port):
        method = "host.massadd"
        hosts = [{"hostid": hid} for hid in hostidList]
        params = {
            "hosts": hosts,
            "interfaces": [
                {
                    "ip": ip, "port": port, "type": "4",
                    "main": "1", "useip": "1", "dns": ""
                }
            ]
        }

        try:
            result = self.conn.do_request(method, params)
            return True
        except ZabbixAPIException as ze:
            # print(ze)
            return False

        except Exception as e:
            # print(e)
            return False

    # If We try to remove all Groups then it is not possible and it will be return False without removing any group
    # It is okay if List contain groups which are not exists it will only remove only group in list which are exists
    def removeGroupsFromHosts(self, hostidList: list, groupidList: list):
        method = "host.massremove"
        params = {
            "hostids": hostidList,
            "groupids": groupidList
        }
        try:
            print(json.dumps(params, indent=1))
            response = self.conn.do_request(method, params)
            # print(response['result'])
            return True
        except ZabbixAPIException as e:
            print(e)
            return False

    # unlink the Templates from host if that template exists . if not exists still return True
    def removeTemplatesFromHosts(self, hostidList: list, templateidList: list):

        method = "host.massremove"
        params = {
            "hostids": hostidList,
            "templateids": templateidList
        }
        try:
            # print(json.dumps(params,indent=1))
            response = self.conn.do_request(method, params)
            # print(response['result'])
            return True
        except ZabbixAPIException as e:
            print(e)
            return False

    # unlink the Templates from host if that template exists . if not exists still return True
    def removeAndClearTemplatesFromHosts(self, hostidList: list, templateidList: list):
        method = "host.massremove"
        params = {
            "hostids": hostidList,
            "templateids_clear": templateidList
        }
        try:
            # print(json.dumps(params,indent=1))
            response = self.conn.do_request(method, params)
            # print(response['result'])
            return True
        except ZabbixAPIException as e:
            print(e)
            return False

    # $If any of the Groups Does not exist will not do anything and return False
    def removeJMXInterfaceFromHosts(self, hostidList: list, macroKeys: list):
        """
        :param macroKeys:  It is List of Macros key List it should be like in following format
            dicList = ["HIGH","LOW","NAME"]
            - It will delete if Given Templates contain any one of the Macros Key
            - It will not delete of if All Macros in list are not present in Hosts
        :return: Return True if we SuccessFully removed the Macros from given Hosts else False
        """
        method = "host.massremove"
        macros = ["{$" + key + "}" for key in macroKeys]
        params = {
            "hostids": hostidList,
            "macros": macros
        }
        try:
            # print(json.dumps(params,indent=1))
            response = self.conn.do_request(method, params)
            # print(response['result'])
            return True
        except ZabbixAPIException as e:
            print(e)
            return False

    # If any of the Macros Key Does not exist will not do anything and return False
    def removeMacroFromHosts(self, hostidList: list, macroKeys: list):
        """
        :param macroKeys:  It is List of Macros key List it should be like in following format
            dicList = ["HIGH","LOW","NAME"]
            - It will delete if Given Templates contain any one of the Macros Key
            - It will not delete of if All Macros in list are not present in Hosts
        :return: Return True if we SuccessFully removed the Macros from given Hosts else False
        """
        method = "host.massremove"
        macros = ["{$" + key + "}" for key in macroKeys]
        params = {
            "hostids": hostidList,
            "macros": macros
        }
        try:
            # print(json.dumps(params,indent=1))
            response = self.conn.do_request(method, params)
            # print(response['result'])
            return True
        except ZabbixAPIException as e:
            print(e)
            return False

    def removeTemplate_HGS_Macros_ToHosts(self, hostidList: list, templateidList: list = [], groupidList: list = [],
                                          macKeys=[]):
        method = "host.massremove"
        macros = ["{$" + key + "}" for key in macKeys]
        params = {
            "hostids": hostidList,
            "templateids": templateidList,
            "groupids": groupidList,
        }
        if macros:
            params['macros'] = macros
        try:
            result = self.conn.do_request(method, params)
            return True
        except ZabbixAPIException as ze:
            # print(ze)
            return False

        except Exception as e:
            # print(e)
            return False

    def removeJmxInterfaceToHost(self, hostidList: list, ip: str, port):
        method = "host.massremove"
        hosts = [{"hostid": hid} for hid in hostidList]
        params = {
            "hosts": hosts,
            "interfaces": [
                {
                    "ip": ip, "port": port, "type": "4",
                    "main": "1", "useip": "1", "dns": ""
                }
            ]
        }

        try:
            result = self.conn.do_request(method, params)
            return True
        except ZabbixAPIException as ze:
            # print(ze)
            return False

        except Exception as e:
            # print(e)
            return False

    # All macros that are not listed in the request will be removed.
    def updateMacrosOfHost(self, hostid: int, macDictList: list):
        """
        :param hostidList: All Hosid in list should be exists
        :param macDictList:
            dicList = [{"HIGH":12},{"Key":"Value"} ]
        :return:
        """
        method = "host.update"

        def toMacros(macdict):
            for key, value in macdict.items(): return {"macro": "{$" + key + "}", "value": value}

        macros = list(map(toMacros, macDictList))
        params = {
            "hostid": hostid,
            "macros": macros
        }

        try:
            result = self.conn.do_request(method, params)
            return True
        except ZabbixAPIException as ze:
            print(ze)
            return False

        except Exception as e:
            # print(e)
            return False


if __name__ == '__main__':
    hu = HostUpdate(connob)
    testip = '10.43.11.197'
    testhostid = [10343]

    groupList = [16, 18]
    test_tmp_ids = [10335]
    test_host_id = [10325]

    tmpList = [10336, 10338, 10335, 10334]
    test_hostIdList = ['10325', '10327', '10330']

    # print(hu.addHostGroupsToHosts(testhostid,[1,2]))  # Still True
    # print(hu.addHostGroupsToHosts(testhostid,groupList))  # Will add Hostgroup

    # print(hu.addTemplatesToHosts(testhostid,[1,2]))  #  False Because this Templaet does not exists
    # print(hu.addTemplatesToHosts(testhostid, test_tmp_ids))  # Will add Template even if already present return True

    dicList = [{"HIGH": 12}, {"TES1": 56}, {"TEST2": 45}]
    # print(hu.addNewMacrosToHosts(testhostid,dicList))

    macList = ["TES1", "TEST2", "HIGH"]
    # print(hu.removeMacroFromHosts(testhostid,macList))

    # print(hu.addTemplate_HGS_Macros_ToHosts(testhostid, test_tmp_ids, groupList))
    # print(hu.addTemplate_HGS_Macros_ToHosts(testhostid, test_tmp_ids, groupList,dicList))
    # print(hu.addTemplate_HGS_Macros_ToHosts(testhostid, [], groupList,dicList))
    # print(hu.addTemplate_HGS_Macros_ToHosts(testhostid, test_tmp_ids, [],dicList))
    # print(hu.addTemplate_HGS_Macros_ToHosts(testhostid, [], [],dicList))

    # print(hu.removeTemplate_HGS_Macros_ToHosts(testhostid, test_tmp_ids))

    # print(hu.removeGroupsFromHosts(testhostid,[1,2]))  # Return True
    # print(hu.removeGroupsFromHosts(testhostid,groupList)) # Return True

    # print(hu.removeTemplatesFromHosts(testhostid,[122313]))  # True
    # print(hu.removeTemplatesFromHosts(testhostid,test_tmp_ids))  # True

    # print(hu.addJmxInterfaceToHost(testhostid,testip,9000))
    # print(hu.removeJmxInterfaceToHost(testhostid,testip,9000))

    dicList = [{"ZSA": 142}, {"TEST2": 25}]
    # All macros that are not listed in the request will be removed.
    # print(hu.updateMacrosOfHost(10343,dicList))
