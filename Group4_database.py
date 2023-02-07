import sqlite3


check = 0

ifexist = False

while True:
    conn = sqlite3.connect('Customer.db')

    c = conn.cursor()
        
    option = input('\n 1 - Create\n 2 - Insert\n 3 - View\n 4 - View all\n 5 - Update\n 6 - DELETE\n>>> ')

    try: #For Value Error

        if option == '1':
            # Create
            if check == 0:
                c.execute("CREATE TABLE IF NOT EXISTS tblcustomer(id integer, name text, product text, quantity integer, contact integer)")
                print('table created ')
                conn.commit()
                check = 1
                continue
            else:
                print('Table already exist\n')
                continue

        elif option == '2':

            #2 Insert

            id = int(input('Enter your id: '))
            
            # to check if id arleady exist or not
            for rows in c.execute('SELECT id FROM tblcustomer ORDER BY id'):
                if id in rows:
                    ifexist = True
            
            if ifexist==True:

                print(f'{id} is already exist\n')  
                ifexist = False

            else:

                name = input('Enter your name: ').upper()
                product = input('Enter your product: ').upper()
                quantity = int(input('Enter your quantity: '))
                contact = int(input('Enter your contact number: '))

        
                sql = """INSERT INTO tblcustomer(id, name, product, quantity, contact) VALUES(?,?,?,?,?)"""
                c.execute(sql,(id, name,product,quantity, contact))

                conn.commit()
                conn.close()
            
            continue

        elif option == '3':
            #3 view

            id = int(input('Enter the id of the customer you want to find? '))
            
            for rows in c.execute('SELECT * FROM tblcustomer ORDER BY id'):
                if id in rows:
                    ifexist = True
            
            if ifexist==True:
                c.execute('SELECT * FROM tblcustomer WHERE id=?', (id,))
                print(c.fetchall())
                ifexist = False
            else:
                print(f'No id called "{id}" in data base\n')            
            continue


        elif option == '4':
            #4 View All
        
            for row in c.execute('SELECT * FROM tblcustomer ORDER BY id'):
                print(row)
            continue

        elif option == '5':
            # update 
            
            
            id = int(input('Enter the id you want to replace: '))

            # to check if input id is in the data base or not
            for rows in c.execute('SELECT * FROM tblcustomer ORDER BY id'):
                if id in rows:
                    ifexist = True
            
            if ifexist==True:
                name = input('Enter your new name: ').upper()
                product = input('Enter your new product: ').upper()
                quantity = int(input('Enter new quantity: ')) 
                contact = int(input('Enter your new contact number: '))
                

                sql = '''UPDATE tblcustomer SET id = ?, name = ?, product = ?, quantity = ?, contact = ? where id = ?'''
                c.execute(sql,(id, name,product,quantity, contact, id ))

                getAllData = c.execute("SELECT * FROM tblcustomer order by id")

                for row in getAllData:
                    print(row)
                    
                conn.commit()
                conn.close()

                ifexist = False


            # if input id is not in the data base
            else:
                print(f'No id "{id}" in data base\n')  

            continue
        
        elif option == '6':
            # To delete data from data base
            delete =input('What person do tou want to delete from the data base :').upper()

            # to check if input id is in the data base or not
            for rows in c.execute('SELECT * FROM tblcustomer ORDER BY id'):
                if delete in rows:
                    ifexist = True
            
            if ifexist==True:
                deleteQuery =f"DELETE FROM tblcustomer WHERE name = '{delete}'"
                c.execute(deleteQuery)

                conn.commit()
                conn.close()

                print('\nData deleted successfully\n')
                ifexist = False 

            else:
                print(f'\nNo Name called "{delete}"  in the data base.\n')
                continue
        else:
            print('ERROR')
            continue 
    except ValueError:
        print('\nInput Error. Please try again!\n')
        continue