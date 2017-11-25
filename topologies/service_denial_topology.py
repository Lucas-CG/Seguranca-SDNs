#-*-coding: utf-8-*-
from mininet.topo import Topo

class ServiceDenialTopology( Topo ):
    """Service denial topology example. 
    Essa topologia não define controlador sendo necessário abrir um terminal e executar controller ptcp:"""

    def __init__( self ):
        "Service denial topology."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1')
        host2 = self.addHost( 'h2')
        host3 = self.addHost( 'h3')
        host4 = self.addHost( 'h4')
        host5 = self.addHost( 'h5')
        host6 = self.addHost( 'h6')
        switch = self.addSwitch('s1')

        # Add links
        self.addLink(host1, switch)
        self.addLink(host2, switch)
        self.addLink(host3, switch)
        self.addLink(host4, switch)
        self.addLink(host5, switch)
        self.addLink(host6, switch)


topos = { 'service-denial-topology': ( lambda: ServiceDenialTopology() ) }
