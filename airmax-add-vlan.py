#!/usr/bin/env python 
#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <Chris Brown> wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If you think this stuff is worth is 
# worth it, please buy me a beer in return.
# ----------------------------------------------------------------------------
#
import sys
import pexpect
import string



#Varibles for use in logging into and adding VLANs the AirMax AP
Target=str("<IP address of target device>")
username=str("<username>")
password=str("<password>")
newvlan=int("vlan number to add")




#creates necesary varables to maake the vlans on the AP work
strvlan=(str(newvlan))
vlannumber=str('0'+strvlan)


#logs into the AirMax AP and adds the specficed vlan
print("logging into the AirMax AP")
child = pexpect.spawn ("ssh "+Target)
child.expect ('password:') 
child.sendline (username) 
#child.interact() #uncomment this is you want to pass the ssh connection through to your CLI
#this adds the vlan to eth0
child.expect ('#')
child.sendline('echo "vlan.'newvlan'.devname=eth0" >> /tmp/system.cfg')
child.expect ('#')
child.sendline('echo "vlan.'newvlan'.id='newvlan'" >> /tmp/system.cfg')
child.expect ('#')
child.sendline('echo "vlan.'newvlan'.status=enabled" >> /tmp/system.cfg') 
child.expect ('#')
child.sendline('echo "netconf.'newvlan'.devname=eth0.'newvlan'" >> /tmp/system.cfg')
child.expect ('#')
child.sendline('echo "netconf.'newvlan'.up=enabled" >> /tmp/system.cfg')
child.expect ('#')
child.sendline('echo "netconf.'newvlan'.status=enabled" >> /tmp/system.cfg')
#this adds the vlan to ath0
child.expect ('#')
child.sendline('echo "vlan.'vlannumber'.devname=eth0" >> /tmp/system.cfg')
child.expect ('#')
child.sendline('echo "vlan.'vlannumber'.id='vlannumber'" >> /tmp/system.cfg')
child.expect ('#')
child.sendline('echo "vlan.'vlannumber'.status=enabled" >> /tmp/system.cfg') 
child.expect ('#')
child.sendline('echo "netconf.'vlannumber'.devname=eth0.'vlannumber'" >> /tmp/system.cfg')
child.expect ('#')
child.sendline('echo "netconf.'vlannumber'.up=enabled" >> /tmp/system.cfg')
child.expect ('#')
child.sendline('echo "netconf.'vlannumber'.status=enabled" >> /tmp/system.cfg')
#
child.expect ('#')
child.sendline('sed -i 's/vlan.status=disabled/vlan.status=enabled/g' /tmp/system.cfg')
child.expect ('#')
child.sendline('saveand reboot')
print (child.before) #prints the last child call
child.expect(pexpect.EOF, timeout=20)




print("Success!")
sys.exit()