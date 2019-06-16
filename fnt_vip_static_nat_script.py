#title
headl = "Generate Fortigate VIP/Static-NAT configuration"
count_headl = len(headl)
print('*'*int(count_headl),'\n')
print(headl,'\n')
print('*'*int(count_headl),'\n\n\n')

#Give a name to NAT rule
vip_name = input("Name for VIP-Static rule:\t")

#Give external and internal IP addresses
ext_ip = input('\nEnter external/public ip: ')
int_ip = input('\nEnter internal/private ip: ')

#Define external interface. Default is "any".
extintf = input('\nEnter external interface (Default is "any"):  ')
if extintf == "":
    extintf = 'any'
else:
    extintf = extintf

#Command to configure NAT
commd = ('\nedit %s\nset extip %s\nset extintf %s\nset mappedip %s-%s\nnext\nend' % (vip_name,ext_ip,extintf,int_ip,int_ip))

print ('\nconfig firewall vip\n',commd)

