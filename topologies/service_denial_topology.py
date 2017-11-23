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
        switch = self.addSwitch('s1')

        # Add links
        self.addLink(host1, switch)
        self.addLink(host2, switch)

topos = { 'service-denial-topology': ( lambda: ServiceDenialTopology() ) }
