
#Display header

headl = "Fortigate network address object"

count_headl = len(headl)

print('*'*int(count_headl),'\n')

print(headl,"\n")

print('*'*int(count_headl),'\n\n\n')


#Create list of IP addresses and add suffix /32 to IPaddresses.
#Put all list of IP addresses in one text file for creating address object.
#Provide that file path when asked in script

def cr_addr_list():
    file1 = input('Enter file name:')
    print('File is ',file1)
    file_open = open(file1, 'r')
    file_read_list = file_open.read().split()
    addr_list=[]
    for ele in file_read_list:
        ele = ele+'/32'
        addr_list.append(ele)
    return addr_list

#Create address object configuration statement
def addr_obj(addr):
	ad_obj = ('edit %s\nset subnet %s\nnext' %(addr,addr))
	return ad_obj


addr1 = cr_addr_list()
print(addr1)

for ob in addr1:
	aq = addr_obj(ob)
	print(aq)


