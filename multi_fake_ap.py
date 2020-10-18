import os
import sys
os.system("clear")
import pyfiglet
print (chr(27)+"[36m")
banner =  pyfiglet.figlet_format("Multi Fake AP ")
print (banner)
print ("          Author : Rahat Khan Tusar(RKT)")
print ("          Github : https;//github.com/r3k4t")
from  scapy.all import *
from  threading import Thread
from  faker import Faker

resp =input("""\nPlease,select your option :
           1.Wireless Acess Points(APs) 802.11 ===> 2
           2.Wireless Acess Points(APs) 802.11 ===> 4
           3.Wireless Acess Points(APs) 802.11 ===> 5
           4.Wireless Acess Points(APs) 802.11 ===> 10\n """)
print ("You have selected option :",resp)

if resp == '1':

  def send_beacon(ssid,mac,infinite=True):
        dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=mac, addr3=mac)
        # ESS+privacy to appear as secured on some devices
        beacon = Dot11Beacon(cap="ESS+privacy")
        essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
        frame = RadioTap()/dot11/beacon/essid
        sendp(frame, inter=0.1, loop=1, iface=iface, verbose=0)


  if __name__ == "__main__":
        # number of access points
        rkt_ap = 2


        interface = input("Enter interface(Example:wlp2s0,wlan0,enp0s3 etc) : ")
        os.system("sudo airmon-ng start {}".format(interface))
        iface = input("Enter interface(Example:wlp2s0mon,wlan0mon,enp0s3mon etc) : ")
         
        # generate random SSIDs and MACs
        faker = Faker()
        ssids_macs = [ (faker.name(), faker.mac_address()) for i in range(rkt_ap) ]
        for ssid, mac in ssids_macs:
             Thread(target=send_beacon, args=(ssid, mac)).start()
             

elif resp == '2':
           
  def send_beacon(ssid,mac,infinite=True):
        dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=mac, addr3=mac)
        # ESS+privacy to appear as secured on some devices
        beacon = Dot11Beacon(cap="ESS+privacy")
        essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
        frame = RadioTap()/dot11/beacon/essid
        sendp(frame, inter=0.1, loop=1, iface=iface, verbose=0)


  if __name__ == "__main__":
        # number of access points
        rkt_ap = 4


        interface = input("Enter interface(Example:wlp2s0,wlan0,enp0s3 etc) : ")
        os.system("sudo airmon-ng start {}".format(interface))
        iface = input("Enter interface(Example:wlp2s0mon,wlan0mon,enp0s3mon etc) : ")



        # generate random SSIDs and MACs
        faker = Faker()
        ssids_macs = [ (faker.name(), faker.mac_address()) for i in range(rkt_ap) ]
        for ssid, mac in ssids_macs:
             Thread(target=send_beacon, args=(ssid, mac)).start()




elif resp == '3':


  def send_beacon(ssid,mac,infinite=True):
        dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=mac, addr3=mac)
        # ESS+privacy to appear as secured on some devices
        beacon = Dot11Beacon(cap="ESS+privacy")
        essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
        frame = RadioTap()/dot11/beacon/essid
        sendp(frame, inter=0.1, loop=1, iface=iface, verbose=0)


  if __name__ == "__main__":
        # number of access points
        rkt_ap = 5
        

        interface = input("Enter interface(Example:wlp2s0,wlan0,enp0s3 etc) : ")
        os.system("sudo airmon-ng start {}".format(interface))
        iface = input("Enter interface(Example:wlp2s0mon,wlan0mon,enp0s3mon etc) : ")

        # generate random SSIDs and MACs
        faker = Faker()
        ssids_macs = [ (faker.name(), faker.mac_address()) for i in range(rkt_ap) ]
        for ssid, mac in ssids_macs:
             Thread(target=send_beacon, args=(ssid, mac)).start()

elif resp == '4':
       

  def send_beacon(ssid,mac,infinite=True):
        dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=mac, addr3=mac)        
        beacon = Dot11Beacon(cap="ESS+privacy")
        essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
        frame = RadioTap()/dot11/beacon/essid
        sendp(frame, inter=0.1, loop=1, iface=iface, verbose=0)


  if __name__ == "__main__":
        # number of access points
        rkt_ap = 10
        

        interface = input("Enter interface(Example:wlp2s0,wlan0,enp0s3 etc) : ")
        os.system("sudo airmon-ng start {}".format(interface))
        iface = input("Enter interface(Example:wlp2s0mon,wlan0mon,enp0s3mon etc) : ")


        # generate random SSIDs and MACs
        faker = Faker()
        ssids_macs = [ (faker.name(), faker.mac_address()) for i in range(rkt_ap) ]
        for ssid, mac in ssids_macs:
             Thread(target=send_beacon, args=(ssid, mac)).start()




