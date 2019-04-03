#Create Bash script for deleting user accounts

def writeBash(file, username) :
    print(f'creating delete script for {username} \n')
    file.write(f'echo deleting user {username}\n')
    file.write(f'userdel -f -r {username}\n')
    file.write(f'groupdel {username} \n\n')
