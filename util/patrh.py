import os
# file_path=os.path.dirname(__file__)
file_path1=os.path.abspath(__file__)
file_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file1=os.path.join(file_path,'cofig','LocalElement.ini')
print(file1)