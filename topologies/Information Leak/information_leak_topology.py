#-*-coding: utf-8-*-
from mininet.topo import Topo

class InformationLeakTopology( Topo ):
    """Information Leak Topology example. 
    Essa topologia não define controlador sendo necessário abrir um terminal e executar controller ptcp:"""

    def __init__( self ):
        "topology."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
	host4 = self.addHost('h4')
        switch1 = self.addSwitch('s1')
	switch2 = self.addSwitch('s2')

        # Add links
        self.addLink(host1, switch1, delay='10ms')
        self.addLink(host2, switch1, delay='10ms')
        self.addLink(host3, switch1, delay='10ms')
	self.addLink(host4, switch2, delay='10ms')
	self.addLink(switch1, switch2, delay='10ms')

topos = { 'information-leak-topology': ( lambda: InformationLeakTopology() ) }
