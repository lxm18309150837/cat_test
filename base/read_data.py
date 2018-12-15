import os

import yaml


class ReadData():
    def __init__(self,filename):
        self.filename = os.getcwd()+os.sep+"data"+os.sep+filename


    def raad_data(self):
        with open(self.filename,"r",encoding="utf-8")as f:
            return yaml.load(f)
#
# if __name__ == '__main__':
#     # print(ReadData().raad_data())
#     list=[]
#     datas = ReadData().raad_data().values()
#     print(datas)
#     for data in datas:
#
#         list.append((data.get("username"),data.get("password")))
#     print(list)
