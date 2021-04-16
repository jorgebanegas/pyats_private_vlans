""" Copyright (c) 2021 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied. 
"""

# Create a testbed for the DevNet Always On NX-OS Sandbox
from genie.testbed import load
import config

device_details = {'devices': {config.hostname: {
   'protocol': 'ssh',
   'ip': config.ip,
   'port': '22',
   'username': config.username,
   'password': config.password,
   'os': 'iosxe'}
   }
}

vlan = str(200) 
testbed = load(device_details)

# Connect to the switch and create variable called device
device = testbed.devices['sidious']
device.connect(learn_hostname=True)


# Using genie.configure to configure vlans

# vtp mode
device.configure("vtp mode transparent")

# Create new vlan
device.configure("vlan " + vlan)

# Create new Vlan object
device.configure("vlan 210 \n private-vlan isolated")

device.configure("vlan 211 \n private-vlan community")

device.configure("vlan " + vlan + "\n private-vlan association 210-211")

# Build and send the configuration to devices
output = device.build_config(apply=True)

print(output)

# Disconnect from the device
device.disconnect()
