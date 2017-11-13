from mininet.net import Mininet
from mininet.cli import CLI

import topoMain

def ddosSim():
	topo = topoMain.ddosSimTopo(2,4)
	network = Mininet(topo)
		
	print "**** starting the network"
	network.start()
	target = network.getNodeByName('h0')
	print target.IP()
	target.cmd('python victimNode.py {} &'.format(target.IP()))
	for host in network.hosts:
		if host.name != target.name:
			print "starting attacker node"
			host.cmd('python attackerNode.py {} 12000 1 &'.format(target.IP()))
	CLI(network)
		
	network.stop()

	
ddosSim()		  		
