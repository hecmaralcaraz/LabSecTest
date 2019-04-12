#!/usr/bin/python3.6
# Hèctor Martínez
# 05/04/2019
#
import os

# Variables

type_env = int(0)


# Funtions
def requirments():
    '''show/install the requirments to use this laboratory'''
    os.system("clear")
    print('\n')
    print('REQUIRMENTS:') 
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

def environment():
    '''Select the environment'''
    print("\n")
    print('You can select the environment (defualt or personalized).')
    print('If you select "Defualt" this program create a environment with the services and configurations by default.')
    print('If you select "Personalized" you can chose all server services you want.\n')
    y = bool(0)
    option = int(0)
    print("Choose the environment:")
    print("1. Default")
    print("2. Personalized")  
    while y == 0:
        option = input("select an option (1|2) \n>")
        if option == '1':
            return 1
            y = 1
        elif option == '2':
            return 2
            y = 1
        print('Please type 1 or 2')

def generate_MV(path,hostname,network):
    '''Generate/write Vagrantfile'''
    try:
        file = open(path + 'Vagrantfile', "w")
    except FileNotFoundError:
        print("File 'Vagrantfile' doesn't exist")

    file.write('Vagrant.configure("2") do |config|' + os.linesep)
    file.write('    config.vm.box = "debian/jessie64"' + os.linesep)  # system of the virtual machine
    file.write('    config.vm.hostname = "' + hostname + '"' + os.linesep)  # hostname of the virtual machine 
    
    # 1 = ip server, 2 = ip client
    if network == '1':  # IP static
        file.write('    config.vm.network "private_network", ip: "192.168.0.1",' + os.linesep)
        file.write('    virtualbox__intnet: true' + os.linesep)
    elif network == '2':  # IP with DHCP
        file.write('    config.vm.network "private_network", type: "dhcp"' + os.linesep)

    file.write('    config.vm.provider "virtualbox" do |vb|' + os.linesep)
    file.write('        vb.memory = "512"' + os.linesep)  # RAM of the virtual machine
    file.write('    end' + os.linesep)
    file.write('end')
    file.close()

def generate_environment():
    '''Generate the environment with Vagrant'''
    # Generate server
    path = 'server/'
    hostname = 'server.sectesting.com'
    network = '1'
    generate_MV(path,hostname,network)

    #Generate client
    path = 'client/'
    hostname = 'server.sectesting.com'
    network = '2'
    generate_MV(path,hostname,network)

    #Generate tester
    path = 'tester/'
    hostname = 'tester.sectesting.com'
    network = '2'
    generate_MV(path,hostname,network)

def services_by_default():
    '''Install all services and all configurations in server'''
    os.system('touch server/script.sh')
    os.system('echo "sudo apt update -y" > server/script.sh')
    
    bind_dns()

def bind_dns():
    '''Install and configurate dns server(bind)'''
    
    try:
        file = open('server/script.sh', "a")
    except FileNotFoundError:
        print("File server/script.sh doesn't exist")
    
    file.write('hola2' + os.linesep)
    file.close()

    

# Estructure

requirments()  # show/install the requirments to use this laboratory
welcome()  # Welcome to learning
type_env = environment()  # Select the environment
generate_environment()
if type_env == 1:
    services_by_default()
elif type_env == 2:
    print('Personalized')









