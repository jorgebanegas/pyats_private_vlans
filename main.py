from netmiko import ConnectHandler
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

device = {
    'device_type': 'cisco_xe',
    'host':   '172.28.104.67',
    'username': 'netadmin',
    'password': 'Gesw213!',
    "fast_cli": True,
}


vlan_number = 200

command_set1 = ["vtp mode transparent"]
command_set2 = ["vlan 210","private-vlan isolated"]
command_set3 = ["vlan 211","private-vlan community"]
command_set4 = ["vlan " + str(vlan_number),"private-vlan association 210-211"]


net_connect = ConnectHandler(**device,default_enter = '\r\n')


vlan_response = net_connect.send_config_set(['vlan ' + str(vlan_number)],cmd_verify=False)

output = net_connect.send_command('show vlan')
print (output)

command_set1_resp = net_connect.send_config_set(command_set1)
print (command_set1_resp)
command_set2_resp = net_connect.send_config_set(command_set2)
print (command_set2_resp)
command_set3_resp = net_connect.send_config_set(command_set3)
print (command_set3_resp)
command_set4_resp = net_connect.send_config_set(command_set4)
print (command_set4_resp)
#output += net_connect.save_config()


output = net_connect.send_command('show vlan')
print (output)

output = net_connect.send_command('show run')
print (output)  