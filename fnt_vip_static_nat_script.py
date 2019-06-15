
headl = "Generate Fortigate VIP/Static-NAT configuration"
count_headl = len(headl)
print('*'*int(count_headl),'\n')
print("Generate Fortigate VIP/Static-NAT configuration\n")
print('*'*int(count_headl),'\n\n\n')

vip_name = input("Name for VIP-Static rule:\t")

ext_ip = input('\nEnter external/public ip: ')
int_ip = input('\nEnter internal/private ip: ')

extintf = input('\nEnter external interface (Default is "any"):  ')
if extintf == "":
    extintf = 'any'
else:
    extintf = extintf

commd = ('\nedit %s\nset extip %s\nset extintf %s\nset mappedip %s-%s\nnext\nend' % (vip_name,ext_ip,extintf,int_ip,int_ip))
print ('\nconfig firewall vip\n',commd)


