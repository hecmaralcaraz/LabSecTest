sudo echo "auto eth1" >> /etc/network/interfaces
sudo echo "iface eth1 inet dhcp" >> /etc/network/interfaces
useradd -p $(openssl passwd laia) -d /home/laia -m -s /bin/bash laia
apt install mysql-server
