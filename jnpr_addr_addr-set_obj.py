
headl = "Generate Juniper SRX address and address-set objects configuration"

count_headl = len(headl)

print('*'*int(count_headl),'\n')

print("Generate Juniper SRX address and address-set objects configuration\n")

print('*'*int(count_headl),'\n\n\n')


#Put all IP addresses in one text file for creating address object.
#Provide the file path when asked in script.

def addr_list():
    file1 = input('Enter full path file name containing all IP addresess: ')
    print('File is ',file1)
    file_open = open(file1, 'r')
    file_read_list = file_open.read().split()
    addr_list=[]
    for ele in file_read_list:
       ele = ele+'/32'
       addr_list.append(ele)
    return addr_list


#address object
def jnpr_addr_obj(zone_name,addr):
	j_a_o = ('set security zones security-zone {} address-book address {} {}'.format(zone_name,addr,addr))
	return j_a_o


#address-set object
def jnpr_addr_set_obj(zone_name,adr_set,addr):
	j_a_o = ('set security zones security-zone {} address-book address-set {} address {}'.format(zone_name,adr_set,addr))
	return j_a_o


jnpr_addr = addr_list()
print(jnpr_addr)
zone_name=input('Enter zone name:')

for adr in jnpr_addr:
	jao = jnpr_addr_obj(zone_name,adr)
	print(jao)


var1 = ['yes','y','YES','Y','Yes']
ask_for_set = input("Do you want to create address-set (y/n):")
adr_set = input('Enter address-set name: ')
if ask_for_set in var1:
	print('This is your address-set')
	for addrs in jnpr_addr:
		ad_set = jnpr_addr_set_obj(zone_name,adr_set,addrs)
		print(ad_set)
else:
	print("Invalid input. Enter "yes/no")
	
		
    
