#-*-coding: utf-8-*-
from mininet.topo import Topo

class TLSAbsenceTopology( Topo ):
    """TLS Absence Topology example. 
    Essa topologia não define controlador sendo necessário abrir um terminal e executar controller ptcp:"""

    def __init__( self ):
        "topology."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1')
        host2 = self.addHost( 'h2')
        host3 = self.addHost( 'h3')
        switch1 = self.addSwitch('s1')
	switch2 = self.addSwitch('s2')

        # Add links
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch2)
	self.addLink(switch2, switch1)

topos = { 'tls-absence-topology': ( lambda: TLSAbsenceTopology() ) }
