1. Get HostGroup Details 
    * getAllHostGroups
    * getUserCreatedHostGroups(self)
    * getUsedHostGroups(self)
    * getHostAssociatedHG(self, groupid=2, groupname="", onlyHids=False)
    * getTemplateAssociatedHG(self, groupid=2, groupname="", onlyTempids=False)
    
    -------------------------------------------------------------------------------------------------
        hgd = HostGroupsDetails(connob)
        - getAllHostGroups()
        - getUserCreatedHostGroups()
        - getUsedHostGroups()
        
        - getHostAssociatedHG()
        - getHostAssociatedHG(onlyHids=True)
        - getHostAssociatedHG(groupname="Linux")
        
        - getTemplateAssociatedHG()
        - getTemplateAssociatedHG(onlyTempids=True)
        - getTemplateAssociatedHG(groupname="Linux")

_____________________________________________________________________________________________________

2. Create and Delete Hostgroups  :   

    - hgc = HostGroupCreate(connob)
    - hgc.createGroup("C3_SIT2")
    - hgc.deleteGroup([20])
_____________________________________________________________________________________________________

3. Update Hostgroups : 
     
     - hgu = HostGroupUpdate(connob)
     - def renameHostGroup(self,gid,newname)
_____________________________________________________________________________________________________
