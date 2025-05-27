
"""
Custom Mininet topology script for question 2:

   h5
    |
   s2--s1--h1
  / |  \
 h2 s5  s3--h6
   /  \     \-h7
  h3   h4     \-h8

- MAC addresses standardized
- Manual (remote) controller
"""
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def customTopo():
    """Create the custom topology."""
    net = Mininet(controller=RemoteController, link=TCLink)

    info('*** Adding controller\n')
    net.addController('c0', controller=RemoteController,
                      ip='127.0.0.1', port=6653)

    info('*** Adding switches\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s5 = net.addSwitch('s5')

    info('*** Adding hosts\n')
    h1 = net.addHost('h1', mac='00:00:00:00:00:01', ip='10.0.0.1/24')
    h2 = net.addHost('h2', mac='00:00:00:00:00:02', ip='10.0.0.2/24')
    h3 = net.addHost('h3', mac='00:00:00:00:00:03', ip='10.0.0.3/24')
    h4 = net.addHost('h4', mac='00:00:00:00:00:04', ip='10.0.0.4/24')
    h5 = net.addHost('h5', mac='00:00:00:00:00:05', ip='10.0.0.5/24')
    h6 = net.addHost('h6', mac='00:00:00:00:00:06', ip='10.0.0.6/24')
    h7 = net.addHost('h7', mac='00:00:00:00:00:07', ip='10.0.0.7/24')
    h8 = net.addHost('h8', mac='00:00:00:00:00:08', ip='10.0.0.8/24')

    info('*** Creating links\n')
    net.addLink(s1, s2)
    net.addLink(s1, h1)
    net.addLink(s2, h2)
    net.addLink(s2, h5)
    net.addLink(s2, s5)
    net.addLink(s5, h3)
    net.addLink(s5, h4)
    net.addLink(s2, s3)
    net.addLink(s3, h6)
    net.addLink(s3, h7)
    net.addLink(s3, h8)

    info('*** Starting network\n')
    net.start()

    info('*** Running CLI\n')
    CLI(net)

    info('*** Stopping network\n')
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    customTopo()
