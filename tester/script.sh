sudo echo "auto eth1" >> /etc/network/interfaces
sudo echo "iface eth1 inet dhcp" >> /etc/network/interfaces
mkdir -p /home/vagrant/tutorials/1collectInformation
mkdir -p /root/tutorials/1collectInformation
apt install -y nmap
