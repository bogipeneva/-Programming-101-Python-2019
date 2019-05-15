import sqlite3


def create_user_table():
    connection = sqlite3.connect('course.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS User
            (id Integer PRIMARY KEY AUTOINCREMENT, full_name Varchar NOT NULL UNIQUE, email Varchar NOT NULL UNIQUE, age Integer NOT NULL, phone Varchar NOT NULL, additional_info Text)
        """)
    connection.commit()
    connection.close()


def add(full_name, email, age, phone, additional_info):
    connection = sqlite3.connect('course.db')
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO User (full_name, email, age, phone, additional_info)
            VALUES ('{full_name}', '{email}', '{age}', '{phone}', '{additional_info}');
        """.format(full_name = full_name, email = email, age = age, phone = phone, additional_info = additional_info)
    )

    connection.commit()
    connection.close()



def list():
    connection = sqlite3.connect('course.db')
    cursor = connection.cursor()

    cursor.execute("SELECT id, full_name, email, age, phone, additional_info FROM User")
    users = cursor.fetchall()

    connection.commit()
    connection.close()

    for user in users:
        print('{}. ID: {}, Email: {}, Full name: {}'.format(user[0],user[0], user[2], user[1]))

def delete(id):
    connection = sqlite3.connect('course.db')
    cursor = connection.cursor()
    cursor.execute(
        """
        DELETE FROM User 
            WHERE id = ?;
        """, (id,))


    connection.commit()
    connection.close()

def get(id):
    connection = sqlite3.connect('course.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM User WHERE id = ?;", (id,))
    user = cursor.fetchall()
    print('ID: {}\nFull_name: {}\nEmail:{}\nAge:{}\nPhone:{}\nAdditional info: {}'.format(user[0][0],user[0][1], user[0][2], user[0][3], user[0][4], user[0][5]))

    connection.commit()
    connection.close()




def main():
    create_user_table()
    print('Hello! This is your business card catalog. What would you like? (enter "help" to list all available options)')
    
    while True:
        option = input('Enter command:')

        if option == 'help':
            print("""#############
###Options###
#############""")
            print("""
1. `add` - insert new business card
2. `list` - list all business cards
3. `delete` - delete a certain business card (`ID` is required)
4. `get` - display full information for a certain business card (`ID` is required)
5. `help` - list all available options """)

        elif option == 'add':
            user_name = input('Enter user name:')
            user_email = input('Enter email:')
            user_age = input('Enter age:')
            user_phone = input('Enter phone:')
            user_additional_info = input('Enter addional info (optional):')

            add(user_name, user_email, user_age, user_phone, user_additional_info)

        elif option == 'list':
            print("""
    #############
    ###Contacts###
    #############""")
            list()

        elif option == 'delete':
            contact_id = input('Enter id:')
            print("""Following contact is deleted successfully:

###############""")
            get(contact_id)
            print("###############")
            delete(contact_id)


        elif option == 'get':
            contact_id = input('Enter id:')
            print("""Contact info:

###############""")
            get(contact_id)
            print("###############")
        else:
            break





if __name__ == '__main__':
    main()
