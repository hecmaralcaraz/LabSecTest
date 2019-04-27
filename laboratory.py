#!/usr/bin/python3.6
# Hèctor Martínez
# 05/04/2019

import os

# Variables

type_env = int(0)


# Funtions
def requirments():
    '''show/install the requirments to use this laboratory'''
    os.system("clear")
    print('\n')
    print('REQUIRMENTS:\n') 
    print('--> VirtualBox >= 5.2')
    print('--> Vagrant >= 2.2.4')
    print('--> Zenity')
    print('--> Python >= 3')
    print('--> Shell bash\n')
    input("Press ENTER to continue...") 

def welcome():
    '''text of welcome'''
    os.system("clear")
    print('\n')
    print ('Welcome to security laboratory!')
    print ('With this program you can learn and practice penetration tests.\n')
    print ('ENVIRONMENT: ')
    print()
    print(' -------------------------------------')
    print('|                                     |')
    print('|   ---------             ---------   |')
    print('|  |         |           |         |  |')
    print('|  | Server  | <-------> | Client  |  |')
    print('|  |         |           |         |  |')
    print('|   ---------             ---------   |')
    print('|              ---------              |')
    print('|             |         |             |')
    print('|             |  Tester |             |')
    print('|             |  (You)  |             |')
    print('|              ---------              |')
    print('|                                     |')
    print(' -------------------------------------') 
    print()
    print('In this laboratory you will work as if you were a malicious employee of a company. You work with the Virutal machine "Tester".')
    print('Inside the MV tester you have a little tutorials and instructions to practice. This type of pentesting is called "gray box", since you have part of the system information.\n') 
    print('After the installation to acces the MV tester you need type "vagrant ssh" in the console shell.\n')   
    input("Press ENTER to continue...")

def check_two_options():
    '''Check two options'''
    y = bool(0)
    option = int(0)
    while y == 0:
        option = input("select an option (1|2) \n>")
        if option == '1':
            return 1
            y = 1
        elif option == '2':
            return 2
            y = 1
        print('\nPlease type 1 or 2')

def environment():
    '''Select the environment'''
    print("\n")
    print('You can select the environment (defualt or personalized).')
    print('If you select "Defualt" this program create a environment with the services and configurations by default.')
    print('If you select "Personalized" you can chose all server services you want.\n')
    print("Choose the environment:")
    print("1) Default")
    print("2) Personalized")  
    return check_two_options()

def generate_MV(path,hostname,network):
    '''Generate/write Vagrantfile with vagrant configurations'''
    try:
        file = open(path + 'Vagrantfile', "w")
    except FileNotFoundError:
        print("File 'Vagrantfile' doesn't exist")

    file.write('Vagrant.configure("2") do |config|' + os.linesep)
    file.write('    config.vm.box = "debian/jessie64"' + os.linesep)  # system of the virtual machine
    file.write('    config.vm.hostname = "' + hostname + '"' + os.linesep)  # hostname of the virtual machine 
    
    # 1 = ip server, 2 = ip client
    if network == '1':  # IP static
        file.write('    config.vm.network "private_network", ip: "192.168.0.13",' + os.linesep)
        file.write('    virtualbox__intnet: "sectesting"' + os.linesep)
    elif network == '2':  # IP with DHCP
        file.write('    config.vm.network "private_network", ip: "192.168.0.10",' + os.linesep)
        file.write('    virtualbox__intnet: "sectesting",' + os.linesep)
        file.write('    auto_config: false' + os.linesep)


    file.write('    config.vm.provider "virtualbox" do |vb|' + os.linesep)
    file.write('        vb.memory = "1024"' + os.linesep)  # RAM of the virtual machine
    file.write('    end' + os.linesep)
    file.write('config.vm.provision "shell", path: "script.sh"' + os.linesep)    
    file.write('end')
    file.close()

def generate_environment():
    '''Generate the environment with Vagrant'''
    # Generate server
    path = 'server/'
    hostname = 'server.sectesting.com'
    network = '1'
    generate_MV(path,hostname,network)  # create Vagrantfile

    #Generate client
    path = 'client/'
    hostname = 'client.sectesting.com'
    network = '2'
    generate_MV(path,hostname,network)  # create Vagrantfile
    generate_conf_client()  # generate client configurations (script.sh)

    #Generate tester
    path = 'tester/'
    hostname = 'tester.sectesting.com'
    network = '2'
    generate_MV(path,hostname,network)  # create Vagrantfile
    generate_conf_tester()  # generate tester configurations (script.sh)

    os.system('touch server/script.sh')
    os.system('echo "sudo apt update -y" > server/script.sh')

def generate_conf_client():
    '''Generate client configuration(script.sh)'''
    os.system('touch client/script.sh')
    
    try:
        file = open('client/script.sh', "w")
    except FileNotFoundError:
        print("File 'Vagrantfile' doesn't exist")

    # network configuration
    file.write('sudo echo "auto eth1" >> /etc/network/interfaces' + os.linesep)
    file.write('sudo echo "iface eth1 inet dhcp" >> /etc/network/interfaces' + os.linesep)
    file.write('useradd -p $(openssl passwd laia) -d /home/laia -m -s /bin/bash laia' + os.linesep)
    file.write('apt install mysql-server' + os.linesep)
    file.close()

def generate_conf_tester():
    '''Generate tester configuration (script.sh)'''
    os.system('touch tester/script.sh')

    try:
        file = open('tester/script.sh', "w")
    except FileNotFoundError:
        print("File 'Vagrantfile' doesn't exist")

    # network configuration
    file.write('sudo echo "auto eth1" >> /etc/network/interfaces' + os.linesep)
    file.write('sudo echo "iface eth1 inet dhcp" >> /etc/network/interfaces' + os.linesep)
    file.close()

def services_by_default():
    '''Install all services and all configurations in server''' 
    #service_dns()
    #service_dhcp()
    service_mysql()
    #service_ftp()
    #service_mail()

def services_by_personalized():
    '''Install the services you want'''
    services = []
    option = int(0)
    os.system('clear')
    print('You have selected to install the services in a personalized way.') 
    print('You have two ways of doing it: \n')
    print('1) Graphical (recommended)')
    print('2) Text\n')
    option = check_two_options()
    if option == 1:
        service = sel_services_graphical()
    elif option == 2:
        service = sel_services_text()
    
    # install the services
    if 'DHCP' in service:
        service_dhcp()
    if 'DNS' in service:
        service_dns()
    if 'FTP' in service:
        service_ftp()
    if 'MYSQL' in service:
        service_mysql()
    if 'Mail' in services:
        service_mail()

def sel_services_graphical():
    '''Select services with graphics'''
    service = []
    # Open a graphic multiselect (services)
    os.system('zenity  --list  --text "Select all services you want" --checklist  --column "Select" --column "service" FALSE "DHCP" FALSE "DNS" FALSE "FTP" FALSE "Mail" --separator="\n" > .services.txt')
    
    # Add all lines in a list
    file = open(".services.txt")
    for line in file.readlines():
        service.append(line[:-1])

    return service


def sel_services_text():
    '''Select services with text'''
    option = str()
    service = ["","","","",""]
    lista = []
    count = int(0)
    print('\nPlease select all services you want:')
    print('1) DHCP')
    print('2) DNS')
    print('3) FTP')
    print('4) MYSQL')
    print('5) Mail')
    print('Type the number of services separated with " , "')
    print('Example: 1,2,3,4,5')
    option=(input('\n>'))

    # collet the services with numbers
    for i in range(0,len(option)):
        if option[i] == ',':
            count += 1
        service[count] = service[count] + option[i]
    print(service)

    # transform the numbers into services
    for x in range(0,len(service)):
        if service[x] == '1':
            lista.append('DHCP')
        if service[x] == '2':
            lista.append('DNS')
        if service[x] == '3':
            lista.append('FTP')
        if service[x] == '4':
            lista.append('MYSQL')
        if service[x] == '5': 
            lista.append('Mail')
    print(lista)

def service_dns():
    '''Install and configure dns service (bind)'''
    
    try:
        file = open('server/script.sh', "a")
    except FileNotFoundError:
        print("File server/script.sh doesn't exist")

    # add all necessary to script.sh file 
    file.write('\n#DNS service' + os.linesep)
    file.write('apt install -y bind9' + os.linesep)
    file.write('sudo cp /vagrant/services/dns/bind/* /etc/bind/' + os.linesep)
    file.write('sudo cp /vagrant/services/dns/resolv.conf /etc/resolv.conf' + os.linesep)
    file.write('sudo service bind9 restart' + os.linesep)
    file.close()

def service_dhcp():
    '''Install and configure dhcp service'''

    try:
        file = open('server/script.sh', "a")
    except FileNotFoundError:
        print("File server/script.sh doesn't exist")

    # add all necessary to script.sh file
    file.write('\n#DHCP service' + os.linesep)
    file.write('sudo apt install -y isc-dhcp-server' + os.linesep)
    file.write('sudo cp /vagrant/services/dhcp/dhcpd.conf /etc/dhcp/dhcpd.conf' + os.linesep)
    file.write('sudo service isc-dhcp-server restart' + os.linesep)
    file.close()

def service_mysql():
    '''Install and configure mysql'''

    try:
        file = open('server/script.sh', "a")
    except FileNotFoundError:
        print("File server/script.sh doesn't exist")

    file.write('\n#MYSQL service' + os.linesep)
    file.write('echo "mysql-server-5.6 mysql-server/root_password password ubuntu" | debconf-set-selections' + os.linesep)
    file.write('echo "mysql-server-5.6 mysql-server/root_password_again password ubuntu" | debconf-set-selections' + os.linesep)
    file.write('apt install -y mysql-server' + os.linesep)
    file.write('mysql -u root -pubuntu -e "create user \'hector\'@\'%\' identified by \'hector\'"' + os.linesep)
    file.write('mysql -u root -pubuntu -e "GRANT ALL PRIVILEGES ON *.* TO hector@\'%\'"' + os.linesep)
    file.write('mysql -u root -pubuntu -e "FLUSH PRIVILEGES"' + os.linesep)
    file.write('cp /vagrant/services/mysql/my.cnf /etc/mysql/my.cnf' + os.linesep)
    file.close()

def service_ftp():
    '''Install and configure ftp service'''

    try:
        file = open('server/script.sh', "a")
    except FileNotFoundError:
        print("File server/script.sh doesn't exist")

    file.write('\n#FTP service' + os.linesep)
    file.write('apt-get install -y vsftpd' + os.linesep)
    file.write('mkdir -p /ftp/anonymous/data' + os.linesep)
    file.write('chown ftp:ftp /ftp/anonymous/data' + os.linesep)
    file.write('cp /vagrant/services/ftp/vsftpd.conf /etc/vsftpd.conf' + os.linesep)
    file.write('cp /vagrant/services/ftp/vsftpd.userlist /etc/vsftpd.userlist' + os.linesep)
    file.write('service vsftpd restart' + os.linesep)
    file.write('' + os.linesep)

    file.close()

def service_mail():
    '''Install and configure mail (postfix, courier)'''

    try:
        file = open('server/script.sh', "a")
    except FileNotFoundError:
        print("File server/script.sh doesn't exist")

    file.write('\n#Mail service' + os.linesep)
    file.write('echo "postfix postfix/mailname string sectesting.com" | debconf-set-selections' + os.linesep)
    file.write('echo "postfix postfix/main_mailer_type string \'Internet Site\'" | debconf-set-selections' + os.linesep)
    file.write('apt install -y postfix' + os.linesep)
    file.write('DEBIAN_FRONTEND=noninteractive apt install -y courier-imap' + os.linesep)
    file.write('apt install -y mailutils' + os.linesep)
    file.write('cp -R /vagrant/services/mail/postfix/* /etc/postfix/' + os.linesep)
    file.close()

# Estructure

requirments()  # show/install the requirments to use this laboratory
welcome()  # welcome to learning
type_env = environment()  # select the environment
generate_environment()  # generate the environment that you have selected
if type_env == 1:
    services_by_default()  # install services by default
elif type_env == 2:
    services_by_personalized()  # install services personalized


