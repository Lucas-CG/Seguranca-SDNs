#!/usr/bin/python
import time
 
"""
Script created by VND - Visual Network Description (SDN version)
"""
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, IVSSwitch, UserSwitch
from mininet.link import Link, TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
 
def topology():
 
    "Create a network."
    net = Mininet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )
 
    print "*** Creating nodes"
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/8' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.0.2/8' )
    h3 = net.addHost( 'h3', mac='00:00:00:00:00:03', ip='10.0.0.3/8' )
    s1 = net.addSwitch( 's1', listenPort=6673, mac='00:00:00:00:00:04' )
    s2 = net.addSwitch( 's2', listenPort=6673, mac='00:00:00:00:00:05' )
    c0 = net.addController ( 'c0' )
    print "*** Creating links"
    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s2, s1)
    net.addLink(s2, h3)
    net.addLink(s2, c0)
 
    print "*** Starting network"
    net.build()
    # use the following command to capture the openflow-related packts. Because the controller will open 6633 for communicating with switches. Then save the captured packets in the mylog file.
    s1.start( [c0] )
    h1.cmdPrint("ping 10.0.0.3 -c 3")
 
    print "*** Running CLI"
    #CLI( net )
    h1.cmdPrint("ping 10.0.0.2 -c 3")
    c0.cmd("pkill tcpdump")
 
    print "*** Stopping network"
    net.stop()
 
if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
