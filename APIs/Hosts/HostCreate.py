from APIs.conn import connob
import json
from pyzabbix import ZabbixAPIException
from Utils.myLogger import getMyLogger
hc_logger = getMyLogger("host.log","host ->")
class HostCreate:

    def __init__(self, connob):
        self.conn = connob
        self.method = "host.create"
        self.agentPort = 10050
        self.defaultPSK = "03ea041ef83a678a123e42a5944aaf390c863a6789ee0987dd21ee31770ff786"
        self.defaultPSKIdentity = "PSK 003"

    @staticmethod
    def __getGroupTemplateIdList(idList):
        groupidList = idList.get('gids', [2])
        templateidList = idList.get('tids', [10001])
        groups = [{"groupid": gid} for gid in groupidList]
        templates = [{"templateid": tid} for tid in templateidList]

        return groups, templates

    @staticmethod
    def __get_Tag_Macro_List(tags_macros):
        def toMacros(macdict):
            for key, value in macdict.items(): return {"macro": "{$" + key + "}", "value": value}

        tagDict = tags_macros.get('tags', {"Method": "API"})
        macDictList = tags_macros.get('macros', {})

        tags = [{"tag": tagKey, "value": tagValue} for tagKey, tagValue in tagDict.items()]
        macros = list(map(toMacros, macDictList))

        return tags, macros

    @staticmethod
    def __getJmxInterface(ip, port):
        jmxinterface = {
            "ip": ip, "port": port, "type": "4",
            "main": "1", "useip": "1", "dns": ""
        }
        return jmxinterface

    @staticmethod
    def __getHostInterface(ip, port):
        interface = {
            "type": 1, "main": 1, "useip": 1,
            "ip": ip, "dns": "", "port": port
        }
        return interface

    # # Note : If you are giving HostGroupId or TemplateIds They must have to  exists otherwise we will not able to
    # add new Host
    def addHostWithoutPSK(self, hostname: str, ip: str, idList: object = {}, tags_macros: object = {},
                          jmxPort=False) -> int:
        """
        :param hostname: "centos_localhost"
        :param ip: "192.168.23.12"
        :param idList:  This variable will have keys like below which have value as List of respective ids
                {
                    'gids':[2],
                    'tids':[10001]
                }
                If you don't provide  gids or tids it will take above as by default
                gids => 2 is for Linux Server group
                tids => 10001 for Template Linux os  by zabbix agent
        :param tags_macros:
            { '
                tags': {"Method":"API"},
                "macros":{}
            },
            macros = [{"HIGH":12},{"Key":"Value"} ]
            macros = [{"HIGH":12}]
         :param jmxPort :
            If you enable JMX monitoring you can specify port of JMX else By default it will not add JMX interface
        :return: iF Host added to Server successfully then True else False
        """
        hostname = hostname
        ip = ip
        groups, templates = self.__getGroupTemplateIdList(idList)
        tags, macros = self.__get_Tag_Macro_List(tags_macros)

        paramater = {
            "host": hostname,
            "groups": groups,
            "templates": templates,
            "tags": tags,
            "macros": macros
        }
        if jmxPort:
            paramater['interfaces'] = [self.__getHostInterface(ip, self.agentPort), self.__getJmxInterface(ip, jmxPort)]
        else:
            paramater['interfaces'] = [self.__getHostInterface(ip, self.agentPort)]
        try:
            result = self.conn.do_request(self.method, paramater)
            # print(json.dumps(paramater, indent=3))
            msg = f' New Vm {hostname} added with IP {ip} | with templateid {",".join(map(str, templates))} '
            msg += f' and group id {",".join(map(str, groups))} | tags  {tags} and {macros}-{result["result"]["hostids"]}'
            # print(msg)
            hc_logger.info(msg)
            return result['result']['hostids'][0]
        except ZabbixAPIException as ze:
            # print(ze)
            hc_logger.warning(f'Cannot able to add VM with ip {ip} and Hostname {hostname} ')
            hc_logger.exception(ze)
            return False

        except Exception as e:
            print(e)
            return False

    def addHostWithDefaultPSK(self, hostname: str, ip: str, idList: object = {}, tags_macros: object = {},
                              jmxPort=False) -> int:
        """
        :param hostname: "centos_localhost"
        :param ip: "192.168.23.12"
        :param idList:  This variable will have keys like below which have value as List of respective ids
                {
                    'gids':[2],
                    'tids':[10001]
                }
                If you don't provide  gids or tids it will take above as by default
                gids => 2 is for Linux Server group
                tids => 10001 for Template Linux os  by zabbix agent
        :param tags_macros:
            { '
                tags': {"Method":"API"},
                "macros":{}
            },
            macros = [{"HIGH":12},{"Key":"Value"} ]
            macros = [{"HIGH":12}]
         :param jmxPort :
            If you enable JMX monitoring you can specify port of JMX else By default it will not add JMX interface
        :return: iF Host added to Server successfully then True else False
        """
        hostname = hostname
        ip = ip
        groups, templates = self.__getGroupTemplateIdList(idList)
        tags, macros = self.__get_Tag_Macro_List(tags_macros)

        paramater = {
            "host": hostname,
            "groups": groups,
            "templates": templates,
            "tags": tags,
            "macros": macros,
            "tls_connect": 2,
            "tls_accept": 2,
            "tls_psk_identity": self.defaultPSKIdentity,
            "tls_psk": self.defaultPSKIdentity

        }
        if jmxPort:
            paramater['interfaces'] = [self.__getHostInterface(ip, self.agentPort), self.__getJmxInterface(ip, jmxPort)]
        else:
            paramater['interfaces'] = [self.__getHostInterface(ip, self.agentPort)]
        try:
            # print(json.dumps(paramater, indent=3))

            # result = self.conn.do_request(self.method, paramater)

            msg = f' New Vm {hostname} added with IP {ip} | with templateid {",".join(map(str, templates))} '
            # msg += f' and group id {",".join(map(str, groups))} | tags  {tags} and {macros}-{result["result"]["hostids"]}'
            # print(msg)
            hc_logger.info(msg)
            # return result['result']['hostids'][0]

        except ZabbixAPIException as ze:
            print(ze)
            hc_logger.warning(f'Cannot able to add VM with ip {ip} and Hostname {hostname} ')
            hc_logger.exception(ze)

            return False

        except Exception as e:
            print(e)
            return False

    def addHostWithPSK(self, hostname, ip, idList={}, tags_macros={}, jmxPort=False, pskData={}):
        """
            :param hostname: "centos_localhost"
            :param ip: "192.168.23.12"
            :param idList:  This variable will have keys like below which have value as List of respective ids
                    {
                        'gids':[2],
                        'tids':[10001]
                    }
                    If you don't provide  gids or tids it will take above as by default
                    gids => 2 is for Linux Server group
                    tids => 10001 for Template Linux os  by zabbix agent
            :param tags_macros:
                { '
                    tags': {"Method":"API"},
                    "macros":{}
                },
                macros = [{"HIGH":12},{"Key":"Value"} ]
                macros = [{"HIGH":12}]
             :param jmxPort :
                If you enable JMX monitoring you can specify port of JMX else By default it will not add JMX interface
             :param pskData :
                {
                    "identity" : "PSK 004"
                    "psk" : "03ea041ef83a678a123e42a5944aaf390c863a6789ee0987dd21ee31770ff786"
                }
            :return: iF Host added to Server successfully then True else False
            """
        hostname = hostname
        ip = ip
        groups, templates = self.__getGroupTemplateIdList(idList)
        tags, macros = self.__get_Tag_Macro_List(tags_macros)
        psk_identity = pskData.get('identity', "PSK 001")
        psk = pskData.get('psk', "03ea041ef83a678a123e42a5944aaf390c863a6789ee0987dd21ee31770ff786")
        paramater = {
            "host": hostname,
            "groups": groups,
            "templates": templates,
            "tags": tags,
            "macros": macros,
            "tls_connect": 2,
            "tls_accept": 2,
            "tls_psk_identity": psk_identity,
            "tls_psk": psk

        }
        if jmxPort:
            paramater['interfaces'] = [self.__getHostInterface(ip, self.agentPort), self.__getJmxInterface(ip, jmxPort)]
        else:
            paramater['interfaces'] = [self.__getHostInterface(ip, self.agentPort)]
        try:
            # print(json.dumps(paramater, indent=3))
            result = self.conn.do_request(self.method, paramater)
            msg = f' New Vm {hostname} added with IP {ip} | with templateid {",".join(map(str, templates))} '
            msg += f' and group id {",".join(map(str, groups))} | tags  {tags} and {macros}-{result["result"]["hostids"]}'
            # print(msg)
            hc_logger.info(msg)
            return result['result']['hostids'][0]
        except ZabbixAPIException as ze:
            print(ze)
            hc_logger.warning(f'Cannot able to add VM with ip {ip} and Hostname {hostname} ')
            hc_logger.exception(ze)

            return False

        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    hc = HostCreate(connob)
    testip = '10.43.11.21'
    testHostname = "Centos_Zabbix2"
    test_psk = "03ea041ef83a678a123e42a5944aaf390c863a6789ee0987dd21ee31770ff786"
    test_identity = "PSK 001"
    print(hc.addHostWithoutPSK(testHostname, testip))
    # print(hc.addHostWithDefaultPSK(testHostname, testip))
    # print(hc.addHostWithPSK(testHostname, testip, pskData={"identity": test_identity, "psk": test_psk}))

    # hc.addHostWithoutPSK(testHostname,testip,jmxPort=23)

    ##################################################################

    # hc.addHostWithoutPSK(testHostname, testip, idList={
    #     "gids": [1, 2, 3],
    #     "tids": [3, 4, 5]
    # })

    ##################################################################

    # hc.addHostWithoutPSK(testHostname, testip, tags_macros={
    #     'macros': [{"HIGH": 12}, {"Key": "Value"}]
    # })

    ##################################################################

    # hc.addHostWithoutPSK(testHostname, testip, tags_macros={
    #     'macros': [{"HIGH": 12}, {"Key": "Value"}]
    #     "tags" : {"type":"normalVM"}
    # })

    ##################################################################

    # hc.addHostWithoutPSK(testHostname, testip,
    #     tags_macros={
    #         'macros': [{"HIGH": 12}, {"Key": "Value"}],
    #         "tags" : {"type":"normalVM"}
    #     },
    #     idList={
    #         "gids": [1, 2, 3],
    #         "tids": [3, 4, 5]
    #     }
    # )

    ##################################################################

    # hc.addHostWithoutPSK(testHostname, testip,
    #     tags_macros={
    #         'macros': [{"HIGH": 12}, {"Key": "Value"}],
    #         "tags" : {"type":"normalVM"}
    #     },
    #     idList={
    #         "gids": [1, 2, 3],
    #         "tids": [3, 4, 5]
    #     }
    # )

    ##################################################################
    # hc.addHostWithoutPSK(testHostname, testip,
    #     {
    #         'macros': [{"HIGH": 12}, {"Key": "Value"}],
    #         "tags" : {"type":"normalVM"}
    #     },
    #     {
    #         "gids": [1, 2, 3],
    #         "tids": [3, 4, 5]
    #     }
    # )

    ##################################################################

    # hc.addHostWithoutPSK(testHostname, testip,
    #      {
    #          "gids": [1, 2, 3],
    #          "tids": [3, 4, 5]
    #      },
    #     {
    #         'macros': [{"HIGH": 12}, {"Key": "Value"}],
    #         "tags" : {"type":"normalVM"}
    #     },
    # )
