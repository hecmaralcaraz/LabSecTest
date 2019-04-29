sudo apt update -y

#MYSQL service
echo "mysql-server-5.6 mysql-server/root_password password ubuntu" | debconf-set-selections
echo "mysql-server-5.6 mysql-server/root_password_again password ubuntu" | debconf-set-selections
apt install -y mysql-server
mysql -u root -pubuntu -e "create user 'hector'@'%' identified by 'hector'"
mysql -u root -pubuntu -e "GRANT ALL PRIVILEGES ON *.* TO hector@'%'"
mysql -u root -pubuntu -e "FLUSH PRIVILEGES"
cp /vagrant/services/mysql/my.cnf /etc/mysql/my.cnf
