import csv
import os

from APIs.Hosts.HostCreate import HostCreate
from APIs.conn import connob
from Utils.VM import VM
from Utils.myLogger import getMyLogger
from settings import DATA_DIR

csvlogger = getMyLogger("mapper.log", "[PARSER]")


class MapVm:
    __Type = set()
    hc = HostCreate(connob)

    def __init__(self, csvfile_path):
        self.filepath = csvfile_path
        self.__pasrseCsvFile()

    def __pasrseCsvFile(self):
        cnt = 0
        with open(self.filepath, 'r', encoding="utf-8") as f1_csv:
            csv_reader = csv.reader(f1_csv)
            ### Header
            print(next(csv_reader))
            # for each host in csv file run this
            for line in csv_reader:
                print("===" * 50)
                print(line)
                self.parseLine(line)
                print("===" * 50)
                cnt += 1
                if cnt == 10: break

    @classmethod
    def parseLine(cls,tupleLine: list):
        hostname, ip = tupleLine[1], tupleLine[2]
        groupLine, templateLine = tupleLine[3], tupleLine[4]
        tags, macros = tupleLine[5], tupleLine[6]
        vmob = VM(hostname, ip, groupLine, templateLine, tags, macros)
        if vmob.invalid:
            return
        else:
            # print(vmob)
            cls.hc.addHostWithDefaultPSK(vmob.hostname,vmob.ip,vmob.idList,vmob.tags_macros)
            # print(cls.hc)
            pass

if __name__ == '__main__':
    csv_file_path = os.path.join(DATA_DIR, "SampleData1.csv")
    m = MapVm(csv_file_path)
