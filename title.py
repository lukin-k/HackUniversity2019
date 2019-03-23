from mininet.node import Controller
from mininet.log import setLogLevel,info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import OVSKernelAP
from mn_wifi.cli import CLI_wifi


def topology():
	net=Mininet_wifi(controller=Controller,accessPoint = OVSKernelAP)
	info("***Creating nodes\n")
	ap1=net.addAccessPoint('ap1',ssid='ssid-ap1',mode='g',channel='1',position='10,30,0',range='20')
	ap2=net.addAccessPoint('ap2',ssid='ssid-ap2',mode='g',channel='6',position='50,30,0',range='20')
	ap3=net.addAccessPoint('ap3',ssid='ssid-ap3',mode='g',channel='3',position='10,60,0',range='30')
	ap4=net.addAccessPoint('ap4',ssid='ssid-ap4',mode='g',channel='4',position='20,5,0',range='10')
	sta1=net.addStation('sta1',mac='00:00:00:00:00:01',ip='10.0.0.1/8',position='10,20,0',range='20')
	sta2=net.addStation('sta2',mac='00:00:00:00:00:02',ip='10.0.0.2/8',position='50,20,0',range='20')
	c1=net.addController('c1',controller=Controller)
	info("***Configuring wifi nodes")
	net.configureWifiNodes()
	net.plotGraph(max_x=80,max_y=80)
	info("***Enable association control (AP)\n")
	net.setAssociationCtrl('ssf')
	info("creating links and associatios\n")
	net.addLink(ap1,ap2)
	net.addLink(ap1,ap3)
	net.addLink(ap1,ap4)
	net.addLink(ap2,ap3)
	net.addLink(ap2,ap4)
	net.addLink(ap3,ap4)

	net.addLink(ap1,sta1)
	net.addLink(ap2,sta2)

	info("***Startig network")
	net.build()
	c1.start()
	ap1.start([c1])
	ap2.start([c1])
	ap3.start([c1])
	ap4.start([c1])
	info("running CLI\n")
	CLI_wifi(net)
	info("***Stopping network\n")
	net.stop()

if __name__=='__main__':
	setLogLevel('info')
	topology()


	