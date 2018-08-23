import os
file_name = os.listdir('C:\\000\\mmbk\\2018-05-08')
for temp in file_name:
    num = temp.rfind('_')#找到最右边]的下标
    print(temp)
#    new_name = temp[num+1:]
#    os.rename('C:\\000\\mmbk\\'+temp,'C:\\000\\mmbk\\'+new_name)
