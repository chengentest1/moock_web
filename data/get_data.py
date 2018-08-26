from data import data_config
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson


class GetDate:
    def __init__(self):
        self.opera_excel = OperationExcel()
    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()
    #获取是否执行
    def get_is_run(self,row):
        flag=None
        col=int(data_config.get_run())
        run_model=self.opera_excel.get_cell_value(row,col)
        if run_model=='yes':
            flag=True
        else:
            flag=False
        return flag
    #是否携带header
    def is_header(self,row):
        col=int(data_config.get_header())
        header=self.opera_excel.get_cell_value(row,col)
        if header=='yes':
            return data_config.get_header_value()
        else:
            return None
    def get_request_method(self,row):
        col=int(data_config.get_request_way())
        request_method=self.opera_excel.get_cell_value(row,col)
        return request_method
    def get_request_url(self,row):
        col=int(data_config.get_url())
        url=self.opera_excel.get_cell_value(row,col)
        return url
    def get_request_data(self,row):
        col=int(data_config.get_data())
        data=self.opera_excel.get_cell_value(row,col)
        if data=='':
            return None
        return data
    def get_data_for_json(self,row):
        opera_json=OperationJson()
        request_data=opera_json.get_data(self.get_request_data(row))
        return request_data


    def get_expcet_data(self, row):
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

