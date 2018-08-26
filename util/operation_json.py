import json
class OperationJson:
    def __init__(self):
        self.data=self.read_json()
    #读取json文件
    def read_json(self):
        with open('../data_resource/login.json') as fp:
            data=json.load(fp)
            return data
    def get_data(self,id):
        return self.data[id]
if __name__=="__main__":
    f=OperationJson()
    i=f.get_data('login')
    print(i)
    # h=f.read_json()['login']
    # print(h)