from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from scapy.all import IP, UDP, TCP, ICMP, Raw, send



def setup_network():
    # Initialize Mininet
    net = Mininet(controller=Controller, link=TCLink)

    # Add components
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    s1 = net.addSwitch('s1')
    c0 = net.addController('c0')

    net.addLink(h1, s1)
    net.addLink(h2, s1)

    # Start the network
    net.start()
    
    # Deploy detection tool
    h1.cmd('python3 ../src/main.py &')  # Start tool on h1

    # Simulate traffic
    traffic_output = h2.cmd('python3 traffic_simulation.py')
    print("Traffic Output:", traffic_output)

    # Open CLI for further inspection
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    setup_network()
