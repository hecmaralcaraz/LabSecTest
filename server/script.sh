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
echo "mysql-server-5.6 mysql-server/root_password password ubuntu" | debconf-set-selections
echo "mysql-server-5.6 mysql-server/root_password_again password ubuntu" | debconf-set-selections
apt install mysql-server
mysql -u root -pubuntu -e "create user 'hector'@'%' identified by 'hector';"
GRANT ALL PRIVILEGES ON *.* TO hector@'%';
FLUSH PRIVILEGES;

#FTP service
apt-get install -y vsftpd
mkdir -p /ftp/anonymous/data
chown ftp:ftp /ftp/anonymous/data
cp /vagrant/services/ftp/vsftpd.conf /etc/vsftpd.conf
cp /vagrant/services/ftp/vsftpd.userlist /etc/vsftpd.userlist
service vsftpd restart


#Mail service
echo "postfix postfix/mailname string sectesting.com" | debconf-set-selections
echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-set-selections
apt install -y postfix
DEBIAN_FRONTEND=noninteractive apt install -y courier-imap
apt install -y mailutils
cp /vagrant/services/mail/postfix/* /etc/postfix/
