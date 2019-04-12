sudo apt update -y
#DNS service
apt install -y bind9
sudo cp /vagrant/services/dns/bind/* /etc/bind/
sudo cp /vagrant/services/dns/resolv.conf /etc/resolv.conf
sudo service bind9 restart
#DHCP service
sudo apt install -y isc-dhcp-server
sudo cp /vagrant/services/dhcp/dhcpd.conf /etc/dhcp/dhcpd.conf
sudo service isc-dhcp-server restart
