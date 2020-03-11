HostDetails class Methods : 

 	- 	getAllHostDetails(self)
 	- 	getAllHosts(self, onlyIp=False, onlyId=False, onlyName=False)
 	- 	getHostDetail(self, hostid=0, hostname="", ip="")
 	- 	getAssociatedHostGroupIdList(self, hostid=0, hostname="", ip="")
 	- 	getAssociateTemplateIdList(self, hostid=0, hostname="", ip="")
 	- 	getAssociatedMacrosList(self, hostid=0, hostname="", ip="")
 	- 	getAssociatedTagList(self, hostid=0, hostname="", ip="")
 	- 	getAssociatedInterfaceIdList(self, hostid=0, hostname="", ip="")
 	- 	getAllHostWithStatus(self, available=2, onlyIp=False)
 	- 	getAllHostWithJMX(self, available=2, onlyIp=False)
 	- 	getIdOfHost(self, hostname: str = "", ip: str = "")
 	- 	getIpOfHost(self, hostname: str = "", hostid="")
 	- 	getNameOfHost(self, hostid: str = "", ip: str = "")

_________________________________________________________________________________________________

    testip = '192.2.11.97'
    testhostid = 10327

    hd.getAllHostDetails()

    hd.getHostDetail(hostid=testhostid)
    hd.getHostDetail(hostname="el")
    hd.getHostDetail(ip=testip)

    hd.getAllHosts(onlyIp=True)
    hd.getAllHosts(onlyName=True)
    hd.getAllHosts(onlyId=True)
    hd.getAllHosts()

    hd.getAssociatedHostGroupIdList(hostname="el")
    hd.getAssociatedHostGroupIdList(hostid=testhostid)
    hd.getAssociatedHostGroupIdList(ip=testip)

    hd.getAssociatedMacrosList(hostid=testhostid)
    hd.getAssociatedMacrosList(hostname="l")
    hd.getAssociatedMacrosList(ip=testip)

    hd.getAssociatedTagList(hostid=testhostid)
    hd.getAssociatedTagList(hostname="l")
    hd.getAssociatedTagList(ip=testip)

    hd.getAssociateTemplateIdList(hostid=testhostid)
    hd.getAssociateTemplateIdList(hostname="l")
    hd.getAssociateTemplateIdList(ip=testip)

    hd.getAssociatedInterfaceIdList(hostid=testhostid)
    hd.getAssociatedInterfaceIdList(hostname="l")
    hd.getAssociatedInterfaceIdList(ip=testip)

    hd.getAllHostWithStatus(onlyIp=True)
    hd.getAllHostWithStatus()
    hd.getAllHostWithStatus(2,onlyIp=True)
    hd.getAllHostWithStatus(1,onlyIp=True)

    hd.getAllHostWithJMX()
    hd.getAllHostWithJMX(1)
    hd.getAllHostWithJMX(onlyIp=True)
    hd.getAllHostWithJMX(2,onlyIp=True)
    hd.getAllHostWithJMX(1,onlyIp=True)

    hd.getIdOfHost(hostname="logstash")
    hd.getIdOfHost(ip=testip)
    hd.getIdOfHost(ip="1234")

    hd.getIpOfHost(hostname="logstash")
    hd.getIpOfHost(hostid=testhostid)
    hd.getIpOfHost(hostname="1234")

    hd.getNameOfHost(ip=testip)
    hd.getNameOfHost(hostid=testhostid)
    hd.getNameOfHost(ip="1234")) 