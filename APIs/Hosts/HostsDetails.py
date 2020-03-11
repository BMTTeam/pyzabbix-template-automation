from APIs.conn import connob
import json


class HostDetails:

    def __init__(self, connob):
        self.conn = connob
        self.method = "host.get"
        # print(self.conn)

    def getAllHostDetails(self):
        """
            Return All Host with value provided in params dictionary
            :return [{host1},{host2}]
        """
        params = {
            "output": ["name", "hostid", "status", "available",
                       "error", "jmx_error", "jmx_available", "host", "tags"],
            "selectGroups": ['groupid', 'name'],
            "selectMacros": ["macro", "value"],
            "selectTags": ["tag", "value"],
            "selectInterfaces": ['interfaceid', 'ip', 'port'],
            "selectParentTemplates": ['templateid', 'name'],
        }
        response = self.conn.do_request(self.method, params)
        # print(json.dumps(response['result'], indent=1))
        return response['result']

    def getAllHosts(self, onlyIp=False, onlyId=False, onlyName=False):
        """
            Return All HostGroups with value provided in params dictionary
            :return [{host1},{host2}]
        """
        resultList = []
        params = {}
        if onlyId:
            params['output'] = ["hostid"]
            response = self.conn.do_request(self.method, params)
            if response['result']:
                resultList = [host['hostid'] for host in response['result']]

        elif onlyName:
            params['output'] = ["name"]
            response = self.conn.do_request(self.method, params)
            if response['result']:
                resultList = [host['name'] for host in response['result']]

        elif onlyIp:
            params = {
                "output": ["hostid"],
                "selectInterfaces": ['ip'],
                "limitSelects": 1
            }
            response = self.conn.do_request(self.method, params)
            if response['result']:
                resultList = [host['interfaces'][0]['ip'] for host in response['result']]

        else:
            params = {
                "output": ["name", "hostid", "host"],
                "selectInterfaces": ['ip'],
                "limitSelects": 1
            }
            response = self.conn.do_request(self.method, params)

            def removeInterface(vm):
                vm['ip'] = vm['interfaces'][0]['ip']
                del vm['interfaces']
                return vm

            resultList = list(map(removeInterface, response['result']))

        return resultList

    def getHostDetail(self, hostid=0, hostname="", ip=""):
        """
             :param hostname: given hostname regex pattern
             :return: IT will give important detail of host with provided pattern . return only first matched host
        """
        params = {
            "output": ["name", "hostid", "status", "available",
                       "error", "jmx_error", "jmx_available", "host", "tags"],
            "selectGroups": ['groupid', 'name'],
            "selectMacros": ["macro", "value"],
            "selectTags": ["tag", "value"],
            "selectInterfaces": ['interfaceid', 'ip', 'port'],
            "selectParentTemplates": ['templateid', 'name'],
        }
        if hostname != "":
            params['search'] = {"name": hostname}
        elif ip != "":
            params['search'] = {"ip": ip}
        else:
            params['hostids'] = [hostid]

        response = self.conn.do_request(self.method, params)
        if response['result'] == []:
            # print(response)
            return []
        else:
            # print(json.dumps(response['result'], indent=1))
            return response['result'][0]

    def getAssociatedHostGroupIdList(self, hostid=0, hostname="", ip=""):
        params = {
            "output": ["name", "hostid"],
            "selectGroups": ["groupid"],
        }
        if hostname != "":
            params['search'] = {"name": hostname}
        elif ip != "":
            params['search'] = {"ip": ip}
        else:
            params['hostids'] = [hostid]

        response = self.conn.do_request(self.method, params)
        if response['result'] == []:
            return []
        else:
            # print(json.dumps(response['result'], indent=1))
            groupIdlist = [int(group['groupid']) for group in response['result'][0]['groups']]
            # print(groupIdlist)
            return groupIdlist

    def getAssociateTemplateIdList(self, hostid=0, hostname="", ip=""):
        params = {
            "output": ["name", "hostid"],
            "selectParentTemplates": ["templateid", "name"],
        }
        if hostname != "":
            params['search'] = {"name": hostname}
        elif ip != "":
            params['search'] = {"ip": ip}
        else:
            params['hostids'] = [hostid]

        response = self.conn.do_request(self.method, params)
        if response['result'] == []:
            return []
        else:
            # print(json.dumps(response['result'], indent=1))
            templateIdList = [int(group['templateid']) for group in response['result'][0]['parentTemplates']]
            # print(templateIdist)
            return templateIdList

    def getAssociatedMacrosList(self, hostid=0, hostname="", ip=""):
        """
        :return: List of Macros associated with given Hostid or Hostname
        [ { use/bin : {$PATH} }   ,  {}    ,   {}  ]
        """
        params = {
            "output": ["name", "hostid"],
            "selectMacros": ["macro", "value"],
        }
        if hostname != "":
            params['search'] = {"name": hostname}
        elif ip != "":
            params['search'] = {"ip": ip}
        else:
            params['hostids'] = [hostid]

        response = self.conn.do_request(self.method, params)
        if response['result'] == []:
            return []
        else:
            # print(json.dumps(response['result'], indent=1))
            return response['result'][0]['macros']

    def getAssociatedTagList(self, hostid=0, hostname="", ip=""):
        """
        :return: List of Macros associated with given Hostid or Hostname
        [{'tag': 'tomcat_type', 'value': 'hardened_tomcat'}]
        """
        params = {
            "output": ["name", "hostid"],
            "selectTags": ["tag", "value"],
        }
        if hostname != "":
            params['search'] = {"name": hostname}
        elif ip != "":
            params['search'] = {"ip": ip}
        else:
            params['hostids'] = [hostid]

        response = self.conn.do_request(self.method, params)
        if response['result'] == []:
            return []
        else:
            # print(json.dumps(response['result'], indent=1))
            return response['result'][0]['tags']

    def getAssociatedInterfaceIdList(self, hostid=0, hostname="", ip=""):
        """
        :return: List of Interface detail associated with given Hostid or Hostname
        [{'interfaceid': '22', 'ip': '192.1.1.1', 'port': '9000', 'type': '4', 'main': '1', 'useip': '1', 'dns': ''} , {} ]
        """
        params = {
            "output": ["name", "hostid"],
            "selectInterfaces": ["interfaceid", "ip", "port", "type", "main", "useip", "dns"],
        }
        if hostname != "":
            params['search'] = {"name": hostname}
        elif ip != "":
            params['search'] = {"ip": ip}
        else:
            params['hostids'] = [hostid]

        response = self.conn.do_request(self.method, params)
        if not response['result']:
            return []
        else:
            # print(json.dumps(response['result'], indent=1))
            return response['result'][0]['interfaces']

    def getAllHostWithStatus(self, available=2, onlyIp=False):
        """
                "available" : "0"   -> UnKnown
                "available" : "1"   -> Successfully connected
                "available" : "2"   -> There is error in connecting
                :return => List of Ips if onlyIp=True else list of all host with available = given availability
        """
        available = str(available)
        # limitselects will give only one interface
        params = {
            "output": ["name", "hostid", "error", "available", "ip"],
            "selectInterfaces": ["ip"],
            "limitSelects": 1
        }
        response = self.conn.do_request(self.method, params)
        if response['result'] == []:
            return []
        else:
            unavailables = list(filter(lambda vm: vm['available'] == available, response['result']))

            def removeInterface(vm):
                if onlyIp:
                    vm = vm['interfaces'][0]['ip']
                    return vm
                vm['ip'] = vm['interfaces'][0]['ip']
                del vm['interfaces']
                return vm

            unavailables = list(map(removeInterface, unavailables))
            # print(json.dumps(unavailables, indent=1))
        return unavailables

    def getAllHostWithJMX(self, available=2, onlyIp=False):
        """
                "available" : "0"   -> Unknown
                "available" : "1"   -> available . Successfully monitoring
                "available" : "2"   -> Unavailable .  There is error in connecting
                :return => List of Ips if onlyIp=True else list of all host with available = given availability
        """
        available = str(available)
        # limitselects will give only one interface
        params = {
            "output": ["name", "hostid", "jmx_error", "jmx_available", "ip"],
            "selectInterfaces": ["ip"],
            "limitSelects": 1
        }
        response = self.conn.do_request(self.method, params)
        if response['result'] == []:
            return []
        else:
            unavailables = list(filter(lambda vm: vm['jmx_available'] == available, response['result']))

            def removeInterface(vm):
                if onlyIp:
                    vm = vm['interfaces'][0]['ip']
                    return vm
                vm['ip'] = vm['interfaces'][0]['ip']
                del vm['interfaces']
                return vm

            unavailables = list(map(removeInterface, unavailables))
            # print(json.dumps(unavailables, indent=1))
        return unavailables

    def getIdOfHost(self, hostname: str = "", ip: str = ""):
        """
        :return: int
        """
        params = {"output": ["hostid"],}
        if hostname != "":
            params['search'] = {"name": hostname}
        elif ip != "":
            params['search'] = {"ip": ip}

        response = self.conn.do_request(self.method, params)
        if not response['result']:
            return []
        else:
            # print(json.dumps(response['result'], indent=1))
            return response['result'][0]['hostid']

    def getIpOfHost(self, hostname: str = "", hostid=""):
        """
        :return: int
        """
        params = {
            "output": ["hostid",],
            "selectInterfaces": ["ip"],
            "limitSelects": 1
        }
        if hostname != "":
            params['search'] = {"name": hostname}
        elif hostid != "":
            params['hostids'] = [hostid]

        response = self.conn.do_request(self.method, params)
        if not response['result']:
            return []
        else:
            # print(json.dumps(response['result'], indent=1))
            return response['result'][0]['interfaces'][0]['ip']

    def getNameOfHost(self, hostid: str = "", ip: str = ""):
        """
        :return: int
        """
        params = {"output": ["name"],}
        if hostid != "":
            params['hostids'] = [hostid]
        elif ip != "":
            params['search'] = {"ip": ip}

        response = self.conn.do_request(self.method, params)
        if not response['result']:
            return []
        else:
            # print(json.dumps(response['result'], indent=1))
            return response['result'][0]['name']
if __name__ == '__main__':
    hd = HostDetails(connob)
    testip = '10.43.11.97'
    testhostid = 10327
    hd.getAllHostDetails()

    # print(json.dumps(hd.getAllHostDetails(),indent=1))

    # print(hd.getHostDetail(hostid=testhostid))
    # print(hd.getHostDetail(hostname="el"))
    # print(hd.getHostDetail(ip=testip))

    # print(hd.getAllHosts(onlyIp=True))
    # print(hd.getAllHosts(onlyName=True))
    # print(hd.getAllHosts(onlyId=True))
    # print(json.dumps(hd.getAllHosts(),indent=1))

    # print(hd.getAssociatedHostGroupIdList(hostname="el"))
    # print(hd.getAssociatedHostGroupIdList(hostid=testhostid))
    # print(hd.getAssociatedHostGroupIdList(ip=testip))

    # print(hd.getAssociatedMacrosList(hostid=testhostid))
    # print(hd.getAssociatedMacrosList(hostname="l"))
    # print(hd.getAssociatedMacrosList(ip=testip))

    # print(hd.getAssociatedTagList(hostid=testhostid))
    # print(hd.getAssociatedTagList(hostname="l"))
    # print(hd.getAssociatedTagList(ip=testip))

    # print(hd.getAssociateTemplateIdList(hostid=testhostid))
    # print(hd.getAssociateTemplateIdList(hostname="l"))
    # print(hd.getAssociateTemplateIdList(ip=testip))

    # print(hd.getAssociatedInterfaceIdList(hostid=testhostid))
    # print(hd.getAssociatedInterfaceIdList(hostname="l"))
    # print(hd.getAssociatedInterfaceIdList(ip=testip))

    # print(hd.getAllHostWithStatus(onlyIp=True))
    # print(hd.getAllHostWithStatus())
    print(json.dumps(hd.getAllHostWithStatus(),indent=2))
    # print(hd.getAllHostWithStatus(2,onlyIp=True))
    # print(hd.getAllHostWithStatus(1,onlyIp=True))

    # print(hd.getAllHostWithJMX())
    # print(hd.getAllHostWithJMX(1))
    # print(hd.getAllHostWithJMX(onlyIp=True))
    # print(hd.getAllHostWithJMX(2,onlyIp=True))
    # print(hd.getAllHostWithJMX(1,onlyIp=True))

    # print(hd.getIdOfHost(hostname="logstash"))
    # print(hd.getIdOfHost(ip=testip))
    # print(hd.getIdOfHost(ip="1234"))

    # print(hd.getIpOfHost(hostname="logstash"))
    # print(hd.getIpOfHost(hostid=testhostid))
    # print(hd.getIpOfHost(hostname="1234"))

    # print(hd.getNameOfHost(ip=testip))
    # print(hd.getNameOfHost(hostid=testhostid))
    # print(hd.getNameOfHost(ip="1234"))

