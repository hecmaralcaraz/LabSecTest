sudo apt update -y

#DNS service
apt install -y bind9
sudo cp /vagrant/services/dns/bind/* /etc/bind/
sudo cp /vagrant/services/dns/resolv.conf /etc/resolv.conf
sudo service bind9 restart

#Mail service
echo "postfix postfix/mailname string sectesting.com" | debconf-set-selections
echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-set-selections
apt install -y postfix
DEBIAN_FRONTEND=noninteractive apt install -y courier-imap
apt install -y mailutils
cp -R /vagrant/services/mail/postfix/* /etc/postfix/
