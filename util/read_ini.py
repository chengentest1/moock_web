import configparser
import os


class ReadIni(object):
    def __init__(self,file_name=None,node=None):
        self.file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if file_name==None:
            file_name=os.path.join(self.file_path,'cofig','LocalElement.ini')
            # file_name='C:\\Users\\cheng\\PycharmProjects\\moock_web\\cofig\\LocalElement.ini'
        if node==None:
            self.node="RegisterElement"
        else:
            self.node=node
        self.cf=self.load_ini(file_name)

    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf
    def get_value(self,key):
        data=self.cf.get(self.node,key)
        return data
if __name__ == '__main__':
    read_ini=ReadIni()
    print(read_ini.get_value('test_mk'))