from Utils.utilfun import *
from Utils.getConfigs import getGroupIds, getMacDict, getTagDict, getTemplateIds


class VM(object):
    """ Host will contain information related to VM like ip,grupids,templateid,
        Host("G1","ubuntu_1921",'191.23,12,12','ntp,https,elk')
        hostname   : String  => Hostname of the VM
        ip         : String  => Ip of the VM
        group_str : String  => Command(',') Separated String
        temp_str : String  => Command(',') Separated String
        tag_str : String  => Command(',') Separated String
        mac_str : String  => Command(',') Separated String
    """
    @property
    def idList(self):
        dicList = {}
        if self._template_ids :
            dicList["tids"] = self._template_ids

        if self._hostgroup_ids :
            dicList["gids"] = self._hostgroup_ids

        return dicList

    @property
    def tags_macros(self):
        dicList = {}
        if self._tagsDict :
            dicList["tags"] = self._tagsDict

        if self._macrosDict :
            dicList["macros"] = self._macrosDict

        return dicList


    @property
    def macrosDict(self):
        return self._macrosDict

    @property
    def tagsDict(self):
        return self._tagsDict

    @property
    def template_ids(self):
        return self._template_ids

    @property
    def hostgroup_ids(self):
        return self._hostgroup_ids

    @property
    def ip(self):
        return self._ip

    @property
    def hostname(self):
        return self._hostname

    def __init__(self, hostname, ip, group_str="", temp_str="", tag_str="", mac_Str=""):
        self.hostname = hostname
        self.ip = ip
        self.hostgroup_ids = group_str
        self.template_ids = temp_str
        self.tagsDict = tag_str
        self.macrosDict = mac_Str

        self.invalid = False

    @hostname.setter
    def hostname(self, value):
        if checkValidStr(value):
            self._hostname = removeQuotes(value)
        else:
            self.invalid = True
            self._hostname = "NA"

    @ip.setter
    def ip(self, value):
        if checkValidStr(value):
            self._ip = removeQuotes(value)
        else:
            self.invalid = True
            self._ip = "NA"

    @hostgroup_ids.setter
    def hostgroup_ids(self, value):
        self._hostgroup_ids = []
        if checkValidStr(value):
            value = removeQuotes(value)
            # print(value)
            for key in value.split(","):
                self._hostgroup_ids += getGroupIds(key)

    @template_ids.setter
    def template_ids(self, value):
        self._template_ids = []
        if checkValidStr(value):
            value = removeQuotes(value)
            # print(value)
            for key in value.split(","):
                self._template_ids += getTemplateIds(key)

    @tagsDict.setter
    def tagsDict(self, value):
        self._tagsDict = {}
        if checkValidStr(value):
            value = removeQuotes(value)
            for tag in value.split(","):
                self._tagsDict = getTagDict(tag)

    @macrosDict.setter
    def macrosDict(self, value):
        self._macrosDict = []
        if checkValidStr(value):
            value = removeQuotes(value)
            for macros in value.split(","):
                self._macrosDict.append(getMacDict(macros))

    def __str__(self):
        return f'{self._hostname} - {self.ip} - {self.hostgroup_ids} - {self.template_ids} - {self.tagsDict} - {self.macrosDict} '


if __name__ == '__main__':
    # v = VM("asd", "1023.123",'INSPROD,PROD', 'APACHE', 'insta,paytm', 'ipath')
    v = VM(" ", " ", 'INSPROD,PROD,wrong', 'APACHE', 'insta,paytm', 'ipath')
    print(v)
