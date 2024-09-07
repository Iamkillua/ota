import os
print("Script loaded")
os.chdir("/home/runner/work/ota/ota")
file_list=os.listdir("/home/runner/work/ota/ota/ota/devices")
dir_list=[]
for i in dir_list:
    j=i.replace(".json","")
    print(i)
    print(j)
    dir_list.append(j)

print(dir_list)
