from mininet.node import Controller
from mininet.log import setLogLevel,info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import OVSKernelAP
from mn_wifi.cli import CLI_wifi


def topology():
	net=Mininet_wifi(controller=Controller,accessPoint=OVSKernelAP)
	info("***Creatingnodes\n")
	ap1=net.addAccessPoint('ap1',ssid='ssid−ap1',mode='g',channel='1',
	osition='10,30,0',range='20')
	ap2=net.addAccessPoint('ap2',ssid='ssid−ap2',mode='g',channel='6',
	osition='50,30,0',range='20')
	sta1=net.addStation('sta1',mac='00:00:00:00:00:01',ip='10.0.0.1/8',
	osition='10,20,0')
	sta2=net.addStation('sta2',mac='00:00:00:00:00:02',ip='10.0.0.2/8',
	osition='50,20,0')
	c1=net.addController('c1',controller=Controller)
	info"***Configuringwifinodes"
	net.configureWifiNodes()
	net.plotGraph(max_x=60,max_y=60)
	info("***Enablingassociationcontrol(AP)\n")
	net.associationControl('ssf')
	info("***Creatinglinksandassociations\n")
	net.addLink(ap1,ap2)
	net.addLink(ap1,sta1)
	net.addLink(ap2,sta2)
	info("***Startingnetwork\n")
	net.build()
	c1.start()
	ap1.start([c1])
	ap2.start([c1])
	info("***RunningCLI\n")
	CLI_wifi(net)
	info("***Stoppingnetwork\n")
	net.stop()

if__name__=='__main__':
	setLogLevel('info')
	topology()