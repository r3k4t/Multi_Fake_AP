<h2>Multi Fake AP</h2>

<h4>Author : RKT</h4>

### Descripton ###

![1](https://user-images.githubusercontent.com/69615463/96358957-aafdf200-112a-11eb-9338-0997394c28a5.png)



This program can create multiple wifi fake APs(Access points).This tool name is Multi_Fake_AP script.A Multi_Fake_AP has 4 options.Select your option and enter your linux interface.In this time,program is running.Fun with multi_fake_ap python script.


### Python Faker module(Concept) ###

python3
<br>
Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
<br>
[GCC 8.3.0] on linux
<br>
Type "help", "copyright", "credits" or "license" for more information
<br>
>>> from faker import Faker
<br>
>>> faker = Faker()
<br>
>>> rkt_ap = 5
<br>
>>> iface =" wlp2s0mon"
<br>
>>> ssids_macs = [(faker.name(),faker.mac_address()) for i in range(rkt_ap)]
<br>
>>> print (ssids_macs)
<br>
[('Sarah Shah', '74:98:97:48:86:56'), ('Anthony Lopez', '4d:fe:ec:24:ca:2e'), ('Kenneth Patel', '30:88:fa:12:b6:52'), ('Henry Middleton', 'fa:76:df:04:bb:ff'), ('Roberto Peterson', 'b3:05:2a:79:40:07')]

### Installation  ###

We need to install aircrack-ng on our system.Open a terminal type and type the following command :

<ul>
<li>sudo apt install aircrack-ng</li>
</ul>

#### Tested On ###

<ul>
<li>Ubuntu</li>
<li>Kali Linux</li>
<li>Linuxmint</li>
<li>Parrot Os</li>
</ul>


### Setup ###

<ul>
<li>sudo pip3 install requirements.txt</li>
</ul> 

### Terminal Command ###

<ul>
<li>git clone https://github.com/r3k4t/Multi_Fake_AP.git</li>
<li>cd   Multi_Fake_AP          </li>
<li>sudo python3  multi_fake_ap.py</li>
</ul>

### Screentshots ###

![Screenshot at 2020-10-17 08-06-32](https://user-images.githubusercontent.com/69615463/96358971-bf41ef00-112a-11eb-8f4d-1748acafd74b.png)

Next

![Screenshot at 2020-10-17 08-07-01](https://user-images.githubusercontent.com/69615463/96358979-d5e84600-112a-11eb-977f-33ae70921acb.png)

Next

![Screenshot at 2020-10-17 08-07-12](https://user-images.githubusercontent.com/69615463/96358991-0a5c0200-112b-11eb-8e2c-f5643e578052.png)


Next

![Screenshot at 2020-10-17 08-07-24](https://user-images.githubusercontent.com/69615463/96358996-219aef80-112b-11eb-91e6-3a0c3a163465.png)

Next

Android pic


