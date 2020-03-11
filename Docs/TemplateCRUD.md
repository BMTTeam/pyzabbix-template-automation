A] Create and Delete Template : 

	 - createTemplate(self, tname, gidList=[2], macDict={})
	 - deleteTemplate(self,tids:list)

		tc = TemplateCreate(connob)
	    tmpIds = [10338]
	    tc.createTemplate("Test Template 2",[2,123],{"LOW":10,"HIGH":43})
	    tc.createTemplate("Test Template 4", [2], {"LOW": 10, "HIGH": 43})
	    tc.deleteTemplate(tmpIds)

___________________________________________________________________________________________________
    
B] Update Template :

	- addNewMacroToTemplates(self, tids, macDictList)
	- addNewGroupToTemplates(self, tids: list, groupidList: list)
	- addGroupAndMacroFromTemplates(self, tids, groupidList: list, macDictList: list)
	- addTemplatesToHosts(self, templateidList: list, hostIdList: list)

	- removeMacroFromTemplates(self, tids: list, macroKeys: list)
	- removeGroupFromTemplate(self, tids: list, groupidList: list)
	- renameTemplate(self, tid: int, visibleName, newName: str = "")
	- removeTemplatesFromHosts(self, templateidList: list, hostIdList: list)	

	____________________________________________________________________________________

		tu = TemplateUpdate(connob)

	    dicList = [{"HIGH": 12}, {"TES1": 56}, {"TEST2": 45}]
	    macList = ["TES1", "TEST2", "HIGH"]


	    tu.addNewMacroToTemplates([10335], dicList)

	    tu.addNewGroupToTemplates([10335], [16, 18])

	    tu.addGroupAndMacroFromTemplates([10335], [16, 18], dicList)

	    tu.removeMacroFromTemplates([10335], macList)

	    tu.removeGroupFromTemplate([10335], [18, 56])

	    tu.renameTemplate(10335, "Test Rename Template")

	    tu.addTemplatesToHosts(tmpList, ['10325', '10327', '10330'])

	    tu.removeTemplatesFromHosts(tmpList, ['10325', '10327', '10330'])

___________________________________________________________________________________________________


C] Get Detail about Template :

	- getAllTemplates(self)
    - getUserCreatedTemplate(self, onlyIds=False)
    - getTemplateDetails(self, tid=0, tname="")
    - getMACROSListRelatedToTemplate(self, tid=0, tname="")
    - getItemListRelatedToTemplate(self, tid=0, tname="")
    - getTriggersRelatedToTemplates(self, tid=0, tname="")
    - getHostsRelatedToTemplates(self, tid=0, tname="")
    - getTemplateName(self,tid)
    - getTemplateId(self,tname)
    - getItemCount(self, tid=0, tname="")

    --------------------------------------------------------------------------------

    td = TemplateDetails(connob)
    # test_tmp_id = 10330
    test_tmp_id = 10001
    test_tmp_name = "TEMPLATE_1 Tomcat_Process_Monitorin"
    
    td.getAllTemplates()

    td.getUserCreatedTemplate()
    td.getUserCreatedTemplate(True)

    td.getTemplateDetails(test_tmp_id)
    td.getTemplateDetails(tname=test_tmp_name)

    td.getMACROSListRelatedToTemplate(test_tmp_id)
    td.getMACROSListRelatedToTemplate(tname=test_tmp_name)

    td.getItemListRelatedToTemplate(test_tmp_id)
    td.getItemListRelatedToTemplate(tname=test_tmp_name)

    td.getTriggersRelatedToTemplates(test_tmp_id)
    td.getTriggersRelatedToTemplates(tname=test_tmp_name)

    td.getHostsRelatedToTemplates(test_tmp_id)
    td.getHostsRelatedToTemplates(tname="Linux")

    td.getTemplateName(10331)
    td.getTemplateName(123344134)

    td.getTemplateId("linux")
    td.getTemplateId("weqwe")

    td.getItemCount(test_tmp_id)
    td.getItemCount(234)
    td.getItemCount(tname="Linux")
    td.getItemCount(tname="wceff")


___________________________________________________________________________________________________    