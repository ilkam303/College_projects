#Create Bash script for making user accounts en mass

def writeBash(file, username, password, fname, sname, uid) :
    """Makes bash file creating users from a file. Use writeBash(file, username, password, first name, surname, user id)"""
    print(f'Creating bash entry for user {fname} {sname}')
    file.write(f'echo Creating user {fname} {sname} \n')
    file.write(f"useradd -m -U {fname.lower()}.{sname.lower()} -c '{fname} {sname} {uid}' \n")
    file.write(f"echo {fname.lower()}.{sname.lower()}:{password} | chpasswd \n\n")
