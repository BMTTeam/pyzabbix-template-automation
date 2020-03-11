import os
print(os.getcwd())
ROOT_DIR = "C:/Projects/ZabbixAutomate/"
# print(ROOT_DIR)
LOG_DIR = os.path.join(ROOT_DIR,"Logs/")
PROPERTIES_DIR = os.path.join(ROOT_DIR,"Properties/")
DATA_DIR = os.path.join(ROOT_DIR,"Data/")
# print(PROPERTIES_DIR)
print(DATA_DIR)