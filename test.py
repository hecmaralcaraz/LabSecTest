import os
try:
    file = open('.services.txt', "a")
except FileNotFoundError:
    print("File server/script.sh doesn't exist")

file.write('\n#MYSQL service' + os.linesep)
file.write('apt install mysql-server' + os.linesep)
file.write('mysql -u root -pubuntu -e "create user \'hector\'@\'%\' identified by \'hector\';"' + os.linesep)
file.write('' + os.linesep)
file.close()