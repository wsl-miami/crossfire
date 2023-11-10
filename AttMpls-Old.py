#!/usr/bin/python

"""
Custom topology for Mininet, generated by GraphML-Topo-to-Mininet-Network-Generator.
"""

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import time

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/12',
                   autoSetMacs = True
                 )

    info( '[1;36m*** Adding controller[0m\n')

    c0 = net.addController(name='c0',
                        controller=RemoteController,
                        ip='127.0.0.1',
                        protocol='tcp',
                        port=6633)

    info( '[1;36m*** Add switches[0m\n')

    NY54 = net.addSwitch('s1', cls=OVSKernelSwitch, dpid='0000000000000001')
    CMBR = net.addSwitch('s2', cls=OVSKernelSwitch, dpid='0000000000000002')
    CHCG = net.addSwitch('s3', cls=OVSKernelSwitch, dpid='0000000000000003')
    CLEV = net.addSwitch('s4', cls=OVSKernelSwitch, dpid='0000000000000004')
    RLGH = net.addSwitch('s5', cls=OVSKernelSwitch, dpid='0000000000000005')
    ATLN = net.addSwitch('s6', cls=OVSKernelSwitch, dpid='0000000000000006')
    PHLA = net.addSwitch('s7', cls=OVSKernelSwitch, dpid='0000000000000007')
    WASH = net.addSwitch('s8', cls=OVSKernelSwitch, dpid='0000000000000008')
    NSVL = net.addSwitch('s9', cls=OVSKernelSwitch, dpid='0000000000000009')
    STLS = net.addSwitch('s10', cls=OVSKernelSwitch, dpid='0000000000000010')
    NWOR = net.addSwitch('s11', cls=OVSKernelSwitch, dpid='0000000000000011')
    HSTN = net.addSwitch('s12', cls=OVSKernelSwitch, dpid='0000000000000012')
    SNAN = net.addSwitch('s13', cls=OVSKernelSwitch, dpid='0000000000000013')
    DLLS = net.addSwitch('s14', cls=OVSKernelSwitch, dpid='0000000000000014')
    ORLD = net.addSwitch('s15', cls=OVSKernelSwitch, dpid='0000000000000015')
    DNVR = net.addSwitch('s16', cls=OVSKernelSwitch, dpid='0000000000000016')
    KSCY = net.addSwitch('s17', cls=OVSKernelSwitch, dpid='0000000000000017')
    SNFN = net.addSwitch('s18', cls=OVSKernelSwitch, dpid='0000000000000018')
    SCRM = net.addSwitch('s19', cls=OVSKernelSwitch, dpid='0000000000000019')
    PTLD = net.addSwitch('s20', cls=OVSKernelSwitch, dpid='0000000000000020')
    STTL = net.addSwitch('s21', cls=OVSKernelSwitch, dpid='0000000000000021')
    SLKC = net.addSwitch('s22', cls=OVSKernelSwitch, dpid='0000000000000022')
    LA03 = net.addSwitch('s23', cls=OVSKernelSwitch, dpid='0000000000000023')
    SNDG = net.addSwitch('s24', cls=OVSKernelSwitch, dpid='0000000000000024')
    PHNX = net.addSwitch('s25', cls=OVSKernelSwitch, dpid='0000000000000025')

    info( '[1;36m*** Add hosts[0m\n')

    NY54_host = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    CMBR_host = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    CHCG_host = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    CLEV_host = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    RLGH_host = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    ATLN_host = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    PHLA_host = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    WASH_host = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    NSVL_host = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    STLS_host = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    NWOR_host = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    HSTN_host = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    SNAN_host = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    DLLS_host = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    ORLD_host = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    DNVR_host = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
    KSCY_host = net.addHost('h17', cls=Host, ip='10.0.0.17', defaultRoute=None)
    SNFN_host = net.addHost('h18', cls=Host, ip='10.0.0.18', defaultRoute=None)
    SCRM_host = net.addHost('h19', cls=Host, ip='10.0.0.19', defaultRoute=None)
    PTLD_host = net.addHost('h20', cls=Host, ip='10.0.0.20', defaultRoute=None)
    STTL_host = net.addHost('h21', cls=Host, ip='10.0.0.21', defaultRoute=None)
    SLKC_host = net.addHost('h22', cls=Host, ip='10.0.0.22', defaultRoute=None)
    LA03_host = net.addHost('h23', cls=Host, ip='10.0.0.23', defaultRoute=None)
    SNDG_host = net.addHost('h24', cls=Host, ip='10.0.0.24', defaultRoute=None)
    PHNX_host = net.addHost('h25', cls=Host, ip='10.0.0.25', defaultRoute=None)

    info( '[1;36m*** Add links[0m\n')

    local_link = {'bw':1000.0, 'delay':'0ms'}
    net.addLink(NY54, NY54_host, cls=TCLink, **local_link)
    net.addLink(CMBR, CMBR_host, cls=TCLink, **local_link)
    net.addLink(CHCG, CHCG_host, cls=TCLink, **local_link)
    net.addLink(CLEV, CLEV_host, cls=TCLink, **local_link)
    net.addLink(RLGH, RLGH_host, cls=TCLink, **local_link)
    net.addLink(ATLN, ATLN_host, cls=TCLink, **local_link)
    net.addLink(PHLA, PHLA_host, cls=TCLink, **local_link)
    net.addLink(WASH, WASH_host, cls=TCLink, **local_link)
    net.addLink(NSVL, NSVL_host, cls=TCLink, **local_link)
    net.addLink(STLS, STLS_host, cls=TCLink, **local_link)
    net.addLink(NWOR, NWOR_host, cls=TCLink, **local_link)
    net.addLink(HSTN, HSTN_host, cls=TCLink, **local_link)
    net.addLink(SNAN, SNAN_host, cls=TCLink, **local_link)
    net.addLink(DLLS, DLLS_host, cls=TCLink, **local_link)
    net.addLink(ORLD, ORLD_host, cls=TCLink, **local_link)
    net.addLink(DNVR, DNVR_host, cls=TCLink, **local_link)
    net.addLink(KSCY, KSCY_host, cls=TCLink, **local_link)
    net.addLink(SNFN, SNFN_host, cls=TCLink, **local_link)
    net.addLink(SCRM, SCRM_host, cls=TCLink, **local_link)
    net.addLink(PTLD, PTLD_host, cls=TCLink, **local_link)
    net.addLink(STTL, STTL_host, cls=TCLink, **local_link)
    net.addLink(SLKC, SLKC_host, cls=TCLink, **local_link)
    net.addLink(LA03, LA03_host, cls=TCLink, **local_link)
    net.addLink(SNDG, SNDG_host, cls=TCLink, **local_link)
    net.addLink(PHNX, PHNX_host, cls=TCLink, **local_link)

    CityLink1 = {'bw':1000.0, 'delay':'1.5443ms'}
    net.addLink(NY54, CMBR, cls=TCLink, **CityLink1)
    CityLink2 = {'bw':128.0, 'delay':'5.8229ms'}
    net.addLink(NY54, CHCG, cls=TCLink, **CityLink2)
    CityLink3 = {'bw':1000.0, 'delay':'0.6589ms'}
    net.addLink(NY54, PHLA, cls=TCLink, **CityLink3)
    CityLink4 = {'bw':128.0, 'delay':'1.6693ms'}
    net.addLink(NY54, WASH, cls=TCLink, **CityLink4)
    CityLink5 = {'bw':1000.0, 'delay':'2.2029ms'}
    net.addLink(CMBR, PHLA, cls=TCLink, **CityLink5)
    CityLink6 = {'bw':128.0, 'delay':'2.5206ms'}
    net.addLink(CHCG, CLEV, cls=TCLink, **CityLink6)
    CityLink7 = {'bw':128.0, 'delay':'5.4345ms'}
    net.addLink(CHCG, PHLA, cls=TCLink, **CityLink7)
    CityLink8 = {'bw':128.0, 'delay':'2.1268ms'}
    net.addLink(CHCG, STLS, cls=TCLink, **CityLink8)
    CityLink9 = {'bw':1000.0, 'delay':'7.4976ms'}
    net.addLink(CHCG, DNVR, cls=TCLink, **CityLink9)
    CityLink10 = {'bw':1000.0, 'delay':'3.3724ms'}
    net.addLink(CHCG, KSCY, cls=TCLink, **CityLink10)
    CityLink11 = {'bw':128.0, 'delay':'15.1611ms'}
    net.addLink(CHCG, SNFN, cls=TCLink, **CityLink11)
    CityLink12 = {'bw':1000.0, 'delay':'14.1715ms'}
    net.addLink(CHCG, STTL, cls=TCLink, **CityLink12)
    CityLink13 = {'bw':1000.0, 'delay':'10.2741ms'}
    net.addLink(CHCG, SLKC, cls=TCLink, **CityLink13)
    CityLink14 = {'bw':1000.0, 'delay':'3.7536ms'}
    net.addLink(CLEV, NSVL, cls=TCLink, **CityLink14)
    CityLink15 = {'bw':1000.0, 'delay':'4.0169ms'}
    net.addLink(CLEV, STLS, cls=TCLink, **CityLink15)
    CityLink16 = {'bw':128.0, 'delay':'2.9296ms'}
    net.addLink(CLEV, PHLA, cls=TCLink, **CityLink16)
    CityLink17 = {'bw':1000.0, 'delay':'2.9029ms'}
    net.addLink(RLGH, ATLN, cls=TCLink, **CityLink17)
    CityLink18 = {'bw':1000.0, 'delay':'1.9058ms'}
    net.addLink(RLGH, WASH, cls=TCLink, **CityLink18)
    CityLink19 = {'bw':128.0, 'delay':'4.431ms'}
    net.addLink(ATLN, WASH, cls=TCLink, **CityLink19)
    CityLink20 = {'bw':1000.0, 'delay':'1.7597ms'}
    net.addLink(ATLN, NSVL, cls=TCLink, **CityLink20)
    CityLink21 = {'bw':128.0, 'delay':'3.8218ms'}
    net.addLink(ATLN, STLS, cls=TCLink, **CityLink21)
    CityLink22 = {'bw':128.0, 'delay':'5.8893ms'}
    net.addLink(ATLN, DLLS, cls=TCLink, **CityLink22)
    CityLink23 = {'bw':128.0, 'delay':'3.2839ms'}
    net.addLink(ATLN, ORLD, cls=TCLink, **CityLink23)
    CityLink24 = {'bw':128.0, 'delay':'1.0124ms'}
    net.addLink(PHLA, WASH, cls=TCLink, **CityLink24)
    CityLink25 = {'bw':1000.0, 'delay':'2.0692ms'}
    net.addLink(NSVL, STLS, cls=TCLink, **CityLink25)
    CityLink26 = {'bw':1000.0, 'delay':'5.0416ms'}
    net.addLink(NSVL, DLLS, cls=TCLink, **CityLink26)
    CityLink27 = {'bw':128.0, 'delay':'4.4809ms'}
    net.addLink(STLS, DLLS, cls=TCLink, **CityLink27)
    CityLink28 = {'bw':1000.0, 'delay':'1.9679ms'}
    net.addLink(STLS, KSCY, cls=TCLink, **CityLink28)
    CityLink29 = {'bw':1000.0, 'delay':'12.9717ms'}
    net.addLink(STLS, LA03, cls=TCLink, **CityLink29)
    CityLink30 = {'bw':1000.0, 'delay':'2.5936ms'}
    net.addLink(NWOR, HSTN, cls=TCLink, **CityLink30)
    CityLink31 = {'bw':1000.0, 'delay':'3.6187ms'}
    net.addLink(NWOR, DLLS, cls=TCLink, **CityLink31)
    CityLink32 = {'bw':1000.0, 'delay':'4.3603ms'}
    net.addLink(NWOR, ORLD, cls=TCLink, **CityLink32)
    CityLink33 = {'bw':1000.0, 'delay':'1.55ms'}
    net.addLink(HSTN, SNAN, cls=TCLink, **CityLink33)
    CityLink34 = {'bw':128.0, 'delay':'1.8432ms'}
    net.addLink(HSTN, DLLS, cls=TCLink, **CityLink34)
    CityLink35 = {'bw':128.0, 'delay':'6.9315ms'}
    net.addLink(HSTN, ORLD, cls=TCLink, **CityLink35)
    CityLink36 = {'bw':1000.0, 'delay':'6.9246ms'}
    net.addLink(SNAN, PHNX, cls=TCLink, **CityLink36)
    CityLink37 = {'bw':1000.0, 'delay':'2.066ms'}
    net.addLink(SNAN, DLLS, cls=TCLink, **CityLink37)
    CityLink38 = {'bw':1000.0, 'delay':'5.4113ms'}
    net.addLink(DLLS, DNVR, cls=TCLink, **CityLink38)
    CityLink39 = {'bw':1000.0, 'delay':'3.7135ms'}
    net.addLink(DLLS, KSCY, cls=TCLink, **CityLink39)
    CityLink40 = {'bw':1000.0, 'delay':'12.1057ms'}
    net.addLink(DLLS, SNFN, cls=TCLink, **CityLink40)
    CityLink41 = {'bw':128.0, 'delay':'10.1178ms'}
    net.addLink(DLLS, LA03, cls=TCLink, **CityLink41)
    CityLink42 = {'bw':1000.0, 'delay':'4.532ms'}
    net.addLink(DNVR, KSCY, cls=TCLink, **CityLink42)
    CityLink43 = {'bw':1000.0, 'delay':'7.7497ms'}
    net.addLink(DNVR, SNFN, cls=TCLink, **CityLink43)
    CityLink44 = {'bw':1000.0, 'delay':'3.0332ms'}
    net.addLink(DNVR, SLKC, cls=TCLink, **CityLink44)
    CityLink45 = {'bw':1000.0, 'delay':'12.2752ms'}
    net.addLink(KSCY, SNFN, cls=TCLink, **CityLink45)
    CityLink46 = {'bw':1000.0, 'delay':'0.6137ms'}
    net.addLink(SNFN, SCRM, cls=TCLink, **CityLink46)
    CityLink47 = {'bw':1000.0, 'delay':'4.3798ms'}
    net.addLink(SNFN, PTLD, cls=TCLink, **CityLink47)
    CityLink48 = {'bw':1000.0, 'delay':'5.5555ms'}
    net.addLink(SNFN, STTL, cls=TCLink, **CityLink48)
    CityLink49 = {'bw':1000.0, 'delay':'4.9013ms'}
    net.addLink(SNFN, SLKC, cls=TCLink, **CityLink49)
    CityLink50 = {'bw':128.0, 'delay':'2.8414ms'}
    net.addLink(SNFN, LA03, cls=TCLink, **CityLink50)
    CityLink51 = {'bw':1000.0, 'delay':'4.352ms'}
    net.addLink(SCRM, SLKC, cls=TCLink, **CityLink51)
    CityLink52 = {'bw':1000.0, 'delay':'1.1845ms'}
    net.addLink(PTLD, STTL, cls=TCLink, **CityLink52)
    CityLink53 = {'bw':1000.0, 'delay':'4.7405ms'}
    net.addLink(SLKC, LA03, cls=TCLink, **CityLink53)
    CityLink54 = {'bw':1000.0, 'delay':'0.9129ms'}
    net.addLink(LA03, SNDG, cls=TCLink, **CityLink54)
    CityLink55 = {'bw':1000.0, 'delay':'2.9183ms'}
    net.addLink(LA03, PHNX, cls=TCLink, **CityLink55)
    CityLink56 = {'bw':1000.0, 'delay':'2.9183ms'}
    net.addLink(LA03, PHNX, cls=TCLink, **CityLink56)
    CityLink57 = {'bw':1000.0, 'delay':'2.4419ms'}
    net.addLink(SNDG, PHNX, cls=TCLink, **CityLink57)

    info( '\n[1;36m*** Starting network[0m\n')

    net.build()
    info( '[1;36m*** Starting controllers[0m\n')

    for controller in net.controllers:
        controller.start()

    info( '[1;36m*** Starting switches[0m\n')

    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('s4').start([c0])
    net.get('s5').start([c0])
    net.get('s6').start([c0])
    net.get('s7').start([c0])
    net.get('s8').start([c0])
    net.get('s9').start([c0])
    net.get('s10').start([c0])
    net.get('s11').start([c0])
    net.get('s12').start([c0])
    net.get('s13').start([c0])
    net.get('s14').start([c0])
    net.get('s15').start([c0])
    net.get('s16').start([c0])
    net.get('s17').start([c0])
    net.get('s18').start([c0])
    net.get('s19').start([c0])
    net.get('s20').start([c0])
    net.get('s21').start([c0])
    net.get('s22').start([c0])
    net.get('s23').start([c0])
    net.get('s24').start([c0])
    net.get('s25').start([c0])

    info( '\n[1;36m*** Post configure switches and hosts[0m\n')

    NY54.cmd('ifconfig s1 10.0.8.1')
    CMBR.cmd('ifconfig s2 10.0.8.2')
    CHCG.cmd('ifconfig s3 10.0.8.3')
    CLEV.cmd('ifconfig s4 10.0.8.4')
    RLGH.cmd('ifconfig s5 10.0.8.5')
    ATLN.cmd('ifconfig s6 10.0.8.6')
    PHLA.cmd('ifconfig s7 10.0.8.7')
    WASH.cmd('ifconfig s8 10.0.8.8')
    NSVL.cmd('ifconfig s9 10.0.8.9')
    STLS.cmd('ifconfig s10 10.0.8.10')
    NWOR.cmd('ifconfig s11 10.0.8.11')
    HSTN.cmd('ifconfig s12 10.0.8.12')
    SNAN.cmd('ifconfig s13 10.0.8.13')
    DLLS.cmd('ifconfig s14 10.0.8.14')
    ORLD.cmd('ifconfig s15 10.0.8.15')
    DNVR.cmd('ifconfig s16 10.0.8.16')
    KSCY.cmd('ifconfig s17 10.0.8.17')
    SNFN.cmd('ifconfig s18 10.0.8.18')
    SCRM.cmd('ifconfig s19 10.0.8.19')
    PTLD.cmd('ifconfig s20 10.0.8.20')
    STTL.cmd('ifconfig s21 10.0.8.21')
    SLKC.cmd('ifconfig s22 10.0.8.22')
    LA03.cmd('ifconfig s23 10.0.8.23')
    SNDG.cmd('ifconfig s24 10.0.8.24')
    PHNX.cmd('ifconfig s25 10.0.8.25')

    info( '[1;36m*** Wait while enabling STP to OpenvSwitch[0m\n')
    info( '[1;33m*** Expected time: 0.5 min 30 sec[0m\n')
    NY54.cmd('ovs-vsctl set bridge s1 rstp_enable=true')
    CMBR.cmd('ovs-vsctl set bridge s2 rstp_enable=true')
    CHCG.cmd('ovs-vsctl set bridge s3 rstp_enable=true')
    CLEV.cmd('ovs-vsctl set bridge s4 rstp_enable=true')
    RLGH.cmd('ovs-vsctl set bridge s5 rstp_enable=true')
    ATLN.cmd('ovs-vsctl set bridge s6 rstp_enable=true')
    PHLA.cmd('ovs-vsctl set bridge s7 rstp_enable=true')
    WASH.cmd('ovs-vsctl set bridge s8 rstp_enable=true')
    NSVL.cmd('ovs-vsctl set bridge s9 rstp_enable=true')
    STLS.cmd('ovs-vsctl set bridge s10 rstp_enable=true')
    NWOR.cmd('ovs-vsctl set bridge s11 rstp_enable=true')
    HSTN.cmd('ovs-vsctl set bridge s12 rstp_enable=true')
    SNAN.cmd('ovs-vsctl set bridge s13 rstp_enable=true')
    DLLS.cmd('ovs-vsctl set bridge s14 rstp_enable=true')
    ORLD.cmd('ovs-vsctl set bridge s15 rstp_enable=true')
    DNVR.cmd('ovs-vsctl set bridge s16 rstp_enable=true')
    KSCY.cmd('ovs-vsctl set bridge s17 rstp_enable=true')
    SNFN.cmd('ovs-vsctl set bridge s18 rstp_enable=true')
    SCRM.cmd('ovs-vsctl set bridge s19 rstp_enable=true')
    PTLD.cmd('ovs-vsctl set bridge s20 rstp_enable=true')
    STTL.cmd('ovs-vsctl set bridge s21 rstp_enable=true')
    SLKC.cmd('ovs-vsctl set bridge s22 rstp_enable=true')
    LA03.cmd('ovs-vsctl set bridge s23 rstp_enable=true')
    SNDG.cmd('ovs-vsctl set bridge s24 rstp_enable=true')
    PHNX.cmd('ovs-vsctl set bridge s25 rstp_enable=true')

    time.sleep(30)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
