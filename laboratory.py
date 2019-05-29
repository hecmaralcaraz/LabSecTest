#!/usr/bin/python3.6
# Hèctor Martínez Alcaraz
# github.com/hecmaralcaraz
# 28/05/2019

# This program type the vagrant config to create a environment to test pentesting.

import os
import subprocess

# Variables

type_env = int(0)
version_error = int(0)


# Functions to check

def check_version(cmd):
    '''Check the version of program'''
    global version_error

    x = subprocess.getstatusoutput(cmd)  # collect the code error

    if x[0] > 0:
        version_error = 1  # to check the requirements
        return "\033[1;31m"+"--> no ok"+'\033[0;m'
    elif x[0] == 0:
        return "\033[1;32m"+"--> ok"+'\033[0;m'

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
    
def check_services():
    '''Check if services by text is correct'''
    option = int(0)
    while True:
        option = input('\n>')
        if option.isnumeric(): # check is option is a number
            if "1" in option or "2" in option or "2" in option or "3" in option or "4" in option or "5" in option or "6" in option: # check if option contain 1|2|3|4|5
                return option 
            else:
                print('Not is correct, please type a number between 1 and 6.')
        else:
            print ("\nNot is correct, try again.")
            print('Type the number of services without separation')
            print('Example: 123456')


# Funtions

def requirments():
    '''show/install the requirments to use this laboratory'''
    os.system("clear")
    print('\n')
    print('Requirments to use this program:\n')
    print('--> VirtualBox', check_version('vboxmanage --version'))
    print('--> Vagrant' , check_version('vagrant --version'))
    print('--> Zenity', check_version('zenity --version'))
    print('--> Python >= 3', check_version('python3 --version'))
    
    if version_error == 1:  # if a requirement fails exit to program
        print ('\nPlease install all programs/dependencies required to use this program.\n')
        exit()
    
    input("\nPress ENTER to continue...") 

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
    input("Press ENTER to continue...")

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

def generate_MV(path,hostname,network,ram):
    '''Generate/write Vagrantfile with vagrant configurations'''
    ram = str(ram)
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
    file.write('        vb.memory = "' + ram + '"' + os.linesep)  # RAM of the virtual machine
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
    ram = 512
    generate_MV(path,hostname,network,ram)  # create Vagrantfile

    #Generate client
    path = 'client/'
    hostname = 'client.sectesting.com'
    network = '2'
    ram = 512
    generate_MV(path,hostname,network,ram)  # create Vagrantfile
    generate_conf_client()  # generate client configurations (script.sh)

    #Generate tester
    path = 'tester/'
    hostname = 'tester.sectesting.com'
    network = '2'
    ram = 1024
    generate_MV(path,hostname,network,ram)  # create Vagrantfile
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
    file.write('mkdir -p /home/vagrant/tutorials/1collectInformation' + os.linesep)
    file.write('mkdir -p /root/tutorials/1collectInformation' + os.linesep)
    file.write('apt install -y nmap' + os.linesep)
    file.close()

def generate_conf_server(type_env):
    '''Generate server configurations (script.sh)'''
    if type_env == 1:
        services_by_default()  # install services by default
    elif type_env == 2:
        services_by_personalized()  # install services personalized

def services_by_default():
    '''Install all services and all configurations in server''' 
    service_dns()
    service_dhcp()
    service_mysql()
    service_ftp()
    service_mail()
    service_apache()

def services_by_personalized():
    '''Install the services you want'''
    service = []
    option = int(0)
    option2 = int(0)
    os.system('clear')
    y = bool(0)

    while y == 0:
        end_services = str('')
        # To select the services you can do it in two ways (graphical | text)
        print('You have selected to install the services in a personalized way.') 
        print('You have two ways of doing it: \n')
        print('1) Graphical (recommended)')
        print('2) Text\n')
        option = check_two_options()  # check if only is 1 or 2
        if option == 1:
            service = sel_services_graphical()  # Return a list with the services
        elif option == 2:
            service = sel_services_text()  # Return a list with the services

        # check if the services they're right
        print()
        print('You have select the next services:')
        if len(service) == 1:  # if only have selected 1 service
            end_services = service[0]
        else:
            for y in range(0,len(service)):
                end_services += service[y] +  ','  # concatenate the services with ","
            end_services = end_services[:-1]  # list of services - last ,
        print(end_services)  # print the selected services

        # check the if the option is "y" or "n"
        x = 0
        while x == 0:
            print('Are you sure? (y|n)')
            option2 = input('\n>')
            if option2 == 'y':  # if all is right go to next way
                x = 1
                y = 1
            elif option2 == 'n':  # if all not is right, go to before way
                x = 1
                y = 0
                os.system('clear')
            else:  # if option2 is different to "y" or "n"
                print('Please type "y" or "n"')
                x = 0
    print(service)
    # install the services
    if 'DHCP' in service:
        service_dhcp()
    if 'DNS' in service:
        service_dns()
    if 'FTP' in service:
        service_ftp()
    if 'MYSQL' in service:
        service_mysql()
    if 'Mail' in service:
        service_mail()
    if 'Apache' in service:
        service_apache()

def sel_services_graphical():
    '''Select services with graphics'''
    service = []
    # Open a graphic multiselect (services)
    os.system('zenity  --list  --text "Select all services you want" --checklist  --column "Select" --column "service" FALSE "DHCP" FALSE "DNS" FALSE "FTP" FALSE "Mail" FALSE "MYSQL" FALSE "Apache" --separator="\n" > .services.txt')
    
    # Add all lines in a list
    file = open(".services.txt")
    for line in file.readlines():
        service.append(line[:-1])

    return service

def sel_services_text():
    '''Select services with text'''
    option = int()
    service = ["","","","","",""]
    lista = []
    count = int(0)
    print('\nPlease select all services you want:')
    print('1) DHCP')
    print('2) DNS')
    print('3) FTP')
    print('4) MYSQL')
    print('5) Mail')
    print('6) Apache')
    print('Type the number of services without separation')
    print('Example: 123456\n')
    option = check_services()  # check if is correct

    # collet the services with numbers
    for i in range(0,len(option)):
        service[i] = service[i] + option[i]

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
        if service[x] == '6':
            lista.append('Apache')
    return lista

def end():
    '''text of end'''
    os.system('clear')
    print()
    print('Congratulations!')
    print('Now you have the environment pre configured.')
    print('To install the environment you need execute this script: first_time.sh')
    print('Example:' + "\033[1;33m"+" ./first_time.sh"+'\033[0;m')
    print()
    print("\033[1;31m"+"--> *You only need execute the before script the first time* <--"+'\033[0;m')
    print('')
    print('When the installation ends to up the all machines you need execute: start_laboratory.sh')
    print('Example:' + "\033[1;33m"+" ./start_laboratory.sh"+'\033[0;m')
    print()
    print('To shutdown the all machines you need execute: shutdown_laboratory.sh')
    print('Example:' + "\033[1;33m"+" ./shutdown_laboratory.sh"+'\033[0;m')
    print()
    print('To connect to the machine "tester" you need go to directori "tester" and execute: vagrant ssh')
    print('Example:' + "\033[1;33m"+" cd tester && vagrant ssh"+'\033[0;m')
    print('Inside this machine you find all tutorials and examples preparated for you.')
    print('Learn and enjoy! Good hacking')
    print()
    print("\033[1;31m"+"(You have all steps to install, configure and use this program into MANUAL.TXT)"+'\033[0;m')
    print()

# Services

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
    file.write('mysql -u root -pubuntu < /vagrant/world.sql' + os.linesep)
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

def service_apache():
    '''Install apache2'''
    
    try:
        file = open('server/script.sh', "a")
    except FileNotFoundError:
        print("File server/script.sh doesn't exist")

    file.write('\n#apache2 service' + os.linesep)
    file.write('apt install -y apache2' + os.linesep)
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
generate_conf_server(type_env)
end()
