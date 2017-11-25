from mininet.topo import Topo

class InformationLeakTopology( Topo ):
    """Information Leak topology example. 
    Essa topologia não define controlador sendo necessário abrir um terminal e executar controller ptcp:"""

    def __init__( self ):
        "Information leak topology."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1')
        host2 = self.addHost( 'h2')
        host3 = self.addHost('server')
        switch = self.addSwitch('s1')

        # Add links
        self.addLink(host1, switch)
        self.addLink(host2, switch)
        self.addLink(host3, switch)

topos = { 'information-leak-topology': ( lambda: InformationLeakTopology() ) }