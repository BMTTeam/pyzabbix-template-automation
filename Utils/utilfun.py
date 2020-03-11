from os.path import exists
import re


def checkFileExist(filepath):
    if exists(filepath):
        return True
    else:
        return False


def isValidIp(ip):
    regex = "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    result = re.search(regex, ip)
    if result is None:
        return False
    else:
        return True


def removeQuotes(value):
    """  This method remove leading , trailing space and quotes """
    return value.strip("' ")


def stringEmpty(line):
    """ Return True if string is Empty else False """
    if line.strip(): return False
    return True


def checkPatternPresent(string, pattern):
    """ Provide Main String and pattern to be matched return True if Pattern Found else False """
    result = re.search(pattern, string, re.IGNORECASE)
    # If given pattern is not found in string
    if result is None:
        return False
    return True


def checkValidStr(value):
    """ If Give Data is Equal to NA or Empty or -    """
    if value.upper().strip() == "NA" or stringEmpty(value) or value.strip() == "-":
        return False
    else:
        return True

