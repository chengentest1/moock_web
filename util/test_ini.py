from util.read_ini import ReadIni

file=ReadIni(file_name=None,node='Auto_service')
t=file.get_value('Search_input')
print(t)