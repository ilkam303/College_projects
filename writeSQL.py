#Creates SQL file for making SQL user accounts en mass

def writeSQL(file, fname, sname, password, uid):
    """Makes SQL file for creating users. Use writeSQL(file, first name, surname, password, user id)"""
    print(f'Creating SQL entry for user {fname} {sname}')
    file.write("#User "+fname+" "+sname+"\n")
    file.write("CREATE USER \'"+uid+"\'@\'localhost\' IDENTIFIED BY \'"+password+"\';\n")
    file.write("CREATE USER \'"+uid+"\'@\'%\' IDENTIFIED BY \'"+password+"\';\n")
    file.write("CREATE DATABASE IF NOT EXISTS \'"+uid+"\' ; \n")
    file.write("GRANT ALL PRIVILEGES ON \'"+uid+"\'.* TO \'"+uid+"\'@\'localhost\';\n")
    file.write("GRANT ALL PRIVILEGES ON \'"+uid+"\'.* TO \'"+uid+"\'@\'%\';\n\n")
