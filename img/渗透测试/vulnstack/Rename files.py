import os,re

path = "G:/Security/Blogs/Where_put_hexo/source/img/渗透测试/vulnstack"

for i in range(50):
	old_name = input("旧名称：")
	new_name = input("新名称：")
	os.rename(os.path.join(path,old_name+".png"),os.path.join(path,new_name+".png"))
	i += 1