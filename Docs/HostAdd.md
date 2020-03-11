1) Add New Host to zabbix master .
    #### def addHostWithoutPSK(self, hostname: str, ip: str, idList: object = {}, tags_macros: object = {},jmxPort=False)
     
        1) hostname: We can give any name you want but adviced to give which we have given in zabbix_agentd.conf file            
        2) ip: We have to give string which is valid IP   
        3) idList:  This variable will have keys like below which have value as List of respective ids
                    {"gids":[] , "tids":[]} 

        
        4) tags_macros: If you want to add Tags to you can add only one tag and have to pass like as example given
                        below . 
                        You can also any number of macros in the following format                                             

         
         5) jmxPort :
            If you enable JMX monitoring you can specify port of JMX else By default it will not add JMX interface
        
        :return: iF Host added to Server successfully then True else False
        ---------------------------------------------------------------
        Example Paramater : 
            - hostname: "centos_localhost"
            - ip:"192.168.23.12"
            - idList =
                {
                    'gids':[2],
                    'tids':[10001]
                }
                If you don't provide  gids or tids it will take above as by default
                gids => 2 is for Linux Server group
                tids => 10001 for Template Linux os  by zabbix agent
            - tags_macros = 
                
                { 
                    'tags': {"Method":"API"},
                    "macros":{}
                },
                macros = [{"HIGH":12},{"Key":"Value"} ]
                macros = [{"HIGH":12}]

_______________________________________________________________________________________________________

2)  This will add new Host with default PSK . you can change it by modifying changing variables in __init__() method
    ### def addHostWithDefaultPSK(self, hostname: str, ip: str, idList: object = {}, tags_macros: object = {},jmxPort=False)
_______________________________________________________________________________________________________

3)  This will add Host with psk values provided by us  
    ### def addHostWithPSK(self, hostname, ip, idList={}, tags_macros={}, jmxPort=False, pskData={}): 
_______________________________________________________________________________________________________

Example Method Calls : 

    hc.addHostWithoutPSK(testHostname, testip)
    hc.addHostWithDefaultPSK(testHostname, testip)
    hc.addHostWithPSK(testHostname, testip, pskData={"identity": test_identity, "psk": test_psk})

    hc.addHostWithoutPSK(testHostname,testip,jmxPort=23)

    ##################################################################

    hc.addHostWithoutPSK(testHostname, testip, idList={
        "gids": [1, 2, 3],
        "tids": [3, 4, 5]
    })

    ##################################################################

    hc.addHostWithoutPSK(testHostname, testip, tags_macros={
        'macros': [{"HIGH": 12}, {"Key": "Value"}]
    })

    ##################################################################

    hc.addHostWithoutPSK(testHostname, testip, tags_macros={
        'macros': [{"HIGH": 12}, {"Key": "Value"}]
        "tags" : {"type":"normalVM"}
    })

    ##################################################################

    hc.addHostWithoutPSK(testHostname, testip,
        tags_macros={
            'macros': [{"HIGH": 12}, {"Key": "Value"}],
            "tags" : {"type":"normalVM"}
        },
        idList={
            "gids": [1, 2, 3],
            "tids": [3, 4, 5]
        }
    )

    ##################################################################

    hc.addHostWithoutPSK(testHostname, testip,
        tags_macros={
            'macros': [{"HIGH": 12}, {"Key": "Value"}],
            "tags" : {"type":"normalVM"}
        },
        idList={
            "gids": [1, 2, 3],
            "tids": [3, 4, 5]
        }
    )

    ##################################################################
    hc.addHostWithoutPSK(testHostname, testip,
        {
            'macros': [{"HIGH": 12}, {"Key": "Value"}],
            "tags" : {"type":"normalVM"}
        },
        {
            "gids": [1, 2, 3],
            "tids": [3, 4, 5]
        }
    )

    ##################################################################

    hc.addHostWithoutPSK(testHostname, testip,
         {
             "gids": [1, 2, 3],
             "tids": [3, 4, 5]
         },
        {
            'macros': [{"HIGH": 12}, {"Key": "Value"}],
            "tags" : {"type":"normalVM"}
        },
    )
