sudo apt update -y

#Mail service
echo "postfix postfix/mailname string sectesting.com" | debconf-set-selections
echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-set-selections
apt install -y postfix
DEBIAN_FRONTEND=noninteractive apt install -y courier-imap
apt install -y mailutils
cp -R /vagrant/services/mail/postfix/* /etc/postfix/
