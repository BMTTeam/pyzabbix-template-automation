1) HostUpdate(connob) : 
	
	- addHostGroupsToHosts(self, hostidList: list, groupidList: list)
	- addTemplatesToHosts(self, hostidList: list, templateidList: list)
	- addNewMacrosToHosts(self, hostidList: list, macDictList: list)
	- addTemplate_HGS_Macros_ToHosts(self, hostidList: list, templateidList: list = [], groupidList: list = []
	- addJmxInterfaceToHost(self, hostidList: list, ip: str, port)

	- removeGroupsFromHosts(self, hostidList: list, groupidList: list)
	- removeTemplatesFromHosts(self, hostidList: list, templateidList: list)
	- removeAndClearTemplatesFromHosts(self, hostidList: list, templateidList: list)
	- removeJMXInterfaceFromHosts(self, hostidList: list, macroKeys: list)
	- removeMacroFromHosts(self, hostidList: list, macroKeys: list)
	- removeTemplate_HGS_Macros_ToHosts(self, hostidList: list, templateidList: list = [], groupidList: list = []
	- removeJmxInterfaceToHost(self, hostidList: list, ip: str, port)
	- updateMacrosOfHost(self, hostid: int, macDictList: list)


-----------------------------------------------------------------------------------------------


	testip = '182.33.31.197'
	testhostid = [10343]

	groupList = [16, 18]
	test_tmp_ids = [10335]
	test_host_id = [10325]

	tmpList = [10336, 10338, 10335, 10334]
	test_hostIdList = ['10325', '10327', '10330']

	hu.addHostGroupsToHosts(testhostid,[1,2])
	hu.addHostGroupsToHosts(testhostid,groupList)

	hu.addTemplatesToHosts(testhostid,[1,2])
	hu.addTemplatesToHosts(testhostid, test_tmp_ids)

	dicList = [{"HIGH": 12}, {"TES1": 56}, {"TEST2": 45}]
	hu.addNewMacrosToHosts(testhostid,dicList)

	macList = ["TES1", "TEST2", "HIGH"]
	hu.removeMacroFromHosts(testhostid,macList

	hu.addTemplate_HGS_Macros_ToHosts(testhostid, test_tmp_ids, groupList)
	hu.addTemplate_HGS_Macros_ToHosts(testhostid, test_tmp_ids, groupList,dicList)
	hu.addTemplate_HGS_Macros_ToHosts(testhostid, [], groupList,dicList)
	hu.addTemplate_HGS_Macros_ToHosts(testhostid, test_tmp_ids, [],dicList)
	hu.addTemplate_HGS_Macros_ToHosts(testhostid, [], [],dicList)

	hu.removeTemplate_HGS_Macros_ToHosts(testhostid, test_tmp_ids

	hu.removeGroupsFromHosts(testhostid,[1,2])) 
	hu.removeGroupsFromHosts(testhostid,groupList))

	hu.removeTemplatesFromHosts(testhostid,[122313])) 
	hu.removeTemplatesFromHosts(testhostid,test_tmp_ids)) 

	hu.addJmxInterfaceToHost(testhostid,testip,9000)
	hu.removeJmxInterfaceToHost(testhostid,testip,9000)

	dicList = [{"ZSA": 142}, {"TEST2": 25}]	
	# All macros that are not listed in the request will be removed.
	hu.updateMacrosOfHost(10343,dicList)
