import os, json
from Utils.utilfun import checkFileExist, removeQuotes
from settings import PROPERTIES_DIR
from configparser import ConfigParser

config_file = os.path.join(PROPERTIES_DIR, "demoConfiguration.ini")
parser = None

GROUP_SECTION = 'groups'
TEMPLATE_SECTION = 'template'
MACROS_SECTION = 'macros'
TAGS_SECTION = 'tags'

if checkFileExist(config_file):
    parser = ConfigParser()
    parser.read(config_file)


def getGroupIds(key):
    key = key.upper()
    if parser:
        if GROUP_SECTION in parser:
            return json.loads(parser[GROUP_SECTION].get(key, fallback="[]"))
    return []


def getTemplateIds(key):
    key = key.upper()
    if parser:
        if TEMPLATE_SECTION in parser:
            return json.loads(parser[TEMPLATE_SECTION].get(key, fallback="[]"))
    return []


def getTagDict(key):
    key = key.lower()
    if parser:
        if TAGS_SECTION in parser:
            commStr = parser[TAGS_SECTION].get(key, fallback="")
            if commStr:
                tagkey, value = commStr.split(",")
                return {tagkey: value}
    return {}


def getMacDict(key):
    key = key.lower()
    if parser:
        if MACROS_SECTION in parser:
            commStr = parser[MACROS_SECTION].get(key, fallback="")
            if commStr:
                mackey, value = commStr.split(",")
                return {mackey: value}
    return {}


if __name__ == '__main__':
    # print(getGroupIds("HG"))
    # print(getTemplateIds("liNux"))
    # print(getTemplateIds("APACHE"))
    # print(getTagDict("insta"))
    # print(getMacDict("insta"))
    # print(getMacDict("ipath"))
    pass
