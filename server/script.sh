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

#MYSQL service

#FTP service
apt-get install -y vsftpd
mkdir -p /ftp/anonymous/data
chown ftp:ftp /ftp/anonymous/data
cp /vagrant/services/ftp/vsftpd.conf /etc/vsftpd.conf
cp /vagrant/services/ftp/vsftpd.userlist /etc/vsftpd.userlist
service vsftpd restart

