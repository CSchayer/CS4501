from mininet.topo import Topo

class ddosSimTopo(Topo):
   def build(self,depth=1,fanout=2):
		self.hostNum=0
		self.switchNum=0
		
		self.addTree(depth,fanout)
	
   
   def addTree(self, depth, fanout):
	if depth > 0:
		node = self.addSwitch('s%s' % self.switchNum)
		self.switchNum += 1
		self.value = 0
		
		if depth - 1 > 0:
			self.value = 2
		else:
			self.value = fanout
		
		for i in range(self.value):
			child = self.addTree(depth-1,fanout)
			self.addLink(node,child)
	else:
		node = self.addHost('h%s'% self.hostNum)
		self.hostNum+=1
	return node 
	
	
	
