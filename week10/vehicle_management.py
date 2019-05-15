import sqlite3


def create_user_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS BaseUser
            (id Integer NOT NULL PRIMARY KEY AUTOINCREMENT, user_name Text NOT NULL UNIQUE, email Text NOT NULL UNIQUE, phone_number Integer NOT NULL, address Text)
        """)

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Client
            (base_id Integer, FOREIGN KEY(base_id) REFERENCES BaseUser(id))
        """)

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Mechanic
            (base_id Integer, title Text, FOREIGN KEY(base_id) REFERENCES BaseUser(id))
        """)

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Vehicle
            (id Integer NOT NULL PRIMARY KEY AUTOINCREMENT, category Text NOT NULL, make Text NOT NULL , model Text NOT NULL, register_number Text NOT NULL, gear_box Text, owner Integer, FOREIGN KEY(owner) REFERENCES Client(base_id))
        """)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Service
            (id Integer NOT NULL PRIMARY KEY AUTOINCREMENT, name Text)
        """)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Mechanic_services
            (id Integer NOT NULL PRIMARY KEY AUTOINCREMENT, mechanic_id Integer, service_id Integer, FOREIGN KEY(mechanic_id) REFERENCES Mechanic(base_id), FOREIGN KEY(service_id) REFERENCES Service(id))
        """)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Vehicle_repair
            (id Integer NOT NULL PRIMARY KEY AUTOINCREMENT, date Text, start_hour Text, vehicle Integer, bill Real, mechanic_service Integer, FOREIGN KEY(vehicle) REFERENCES Vehicle(id), FOREIGN KEY(mechanic_service) REFERENCES Mechanic_service(id))
        """)
    connection.commit()
    connection.close()

def add_user(user_name, email, phone_number, address):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO BaseUser (user_name, email, phone_number, address)
            VALUES ('{user_name}', '{email}', '{phone_number}', '{address}');
        """.format(user_name = user_name, email = email, phone_number = phone_number, address = address)
    )

    connection.commit()
    connection.close()

def add_client(id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO Client 
            VALUES ('{id}');
        """.format(id = id)
    )

    connection.commit()
    connection.close()

def add_mechanic(id, title):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO Mechanic 
            VALUES ('{id}', '{title}');
        """.format(id = id, title = title)
    )

    connection.commit()
    connection.close()

def add_vehicle(category, make, model, register_number, gear_box, owner):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO Vehicle (category, make, model, register_number, gear_box, owner)
            VALUES ('{category}', '{make}', '{model}', '{register_number}', '{gear_box}', '{owner}');
        """.format(category = category, make = make, model = model, register_number = register_number, gear_box = gear_box, owner = owner)
    )

    connection.commit()
    connection.close()

def add_vehicle_repair(date, start_hour, vehicle, bill, mechanic_service):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO Vehicle_repair (date, start_hour, vehicle, bill, mechanic_service)
            VALUES ({date}', '{start_hour}', '{vehicle}', '{bill}', '{mechanic_service}' );
        """.format(date = date, start_hour = start_hour, vehicle = vehicle, bill = bill, mechanic_service = mechanic_service)
    )

    connection.commit()
    connection.close()

def add_service(name):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO Service (name)
            VALUES ('{name}');
        """.format(name = name)
    )

    connection.commit()
    connection.close()

def add_mechanic_service( mechanic_id, service_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO Mechanic_services (mechanic_id, service_id)
            VALUES ('{mechanic_id}', '{service_id}');
        """.format(mechanic_id = mechanic_id, service_id = service_id)
    )

    connection.commit()
    connection.close()

def check_for_user_by_name(name):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM BaseUser WHERE user_name = ?;", (name, ))
    user = cursor.fetchall()
    return user

    connection.commit()
    connection.close()

def check_if_user_is_client(id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Client WHERE base_id = ?;", (id, ))
    user = cursor.fetchall()
    return user

    connection.commit()
    connection.close()

def list_all_free_hours():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("SELECT id, date, start_hour FROM Vehicle_repair WHERE vehicle = ?;", ('None',))
    users = cursor.fetchall()
    print("""
+----+-------------+-------+
| id | date | start_hour   |
+----+---------------------+
""")

    for elem in users:
        print('| {}  | {}  | {} |'.format(elem[0], elem[1], elem[2]))

    print('+----+-------------+-------+')
    connection.commit()
    connection.close()

def list_free_hours(date):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("SELECT id, date, start_hour FROM Vehicle_repair WHERE vehicle = ? and date = ?;", ('None',date, ))
    users = cursor.fetchall()
    print("""
+----+-------------+-------+
| id | date | start_hour   |
+----+---------------------+
""")
    for elem in users:
        print('| {}  | {}  | {} |'.format(elem[0], elem[1], elem[2]))

    print('+----+-------------+-------+')
    connection.commit()
    connection.close()

def get_client_vehicles(client_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("SELECT id, make, model, register_number FROM Vehicle WHERE owner = ?;", (client_id, ))
    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result

def print_client_vehicles(vehicles):
    print("""
+----+------------------------------------+
| id |               Vehicle              |
+----+------------------------------------+
""")
    for elem in vehicles:
        print('| {}  | {} {}  with RegNumber: {} |'.format(elem[0], elem[1], elem[2], elem[3]))

    print('+----+------------------------------------+')


def print_services():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("SELECT id, name FROM Service")
    users = cursor.fetchall()
    print("""
+----+------------------------------------+
| id |               Service              |
+----+------------------------------------+
""")

    for elem in users:
        print('| {}  | {}                         |'.format(elem[0], elem[1]))

    print('+----+------------------------------------+')
    connection.commit()
    connection.close()

def get_repair_hour(hour_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("SELECT date, start_hour, vehicle, bill, mechanic_service FROM Vehicle_repair WHERE id= ?;", (hour_id, ))
    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result

def save_repair_hour(hour_id, vehicle, mechanic_service):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE Vehicle_repair SET vehicle = ? ,mechanic_service = ? WHERE id= ?;", (vehicle, mechanic_service, hour_id, ))
    cursor.fetchall()

    connection.commit()
    connection.close()

def update_vehicle(hour_id, new_vehicle):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE Vehicle_repair SET vehicle = ? WHERE id= ?;", (new_vehicle, hour_id, ))
    cursor.fetchall()

    connection.commit()
    connection.close()

def update_mechanic_service(hour_id, new_mechanic_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE Vehicle_repair SET mechanic_service = ? WHERE id= ?;", (new_mechanic_id, hour_id, ))
    cursor.fetchall()

    connection.commit()
    connection.close()

def delete_repair_hour(hour_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE Vehicle_repair SET vehicle = ? , bill = ?, mechanic_service = ? WHERE id= ?;", ('None', 'None', 'None', hour_id, ))
    cursor.fetchall()

    connection.commit()
    connection.close()

def update_vehicle_register_number(vehicle_id, new_register_number):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE Vehicle SET register_number = ? WHERE id= ?;", (new_register_number, vehicle_id, ))
    cursor.fetchall()

    connection.commit()
    connection.close()

def update_vehicle_gear_box(vehicle_id, new_gear_box):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE Vehicle SET gear_box = ? WHERE id= ?;", (new_gear_box, vehicle_id, ))
    cursor.fetchall()

    connection.commit()
    connection.close()

def delete_vehicle(vehicle_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Vehicle WHERE id= ?;", (vehicle_id, ))
    cursor.fetchall()

    connection.commit()
    connection.close()

def list_all_busy_hours():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("SELECT id, date, start_hour FROM Vehicle_repair WHERE vehicle != ?;", ('None',))
    users = cursor.fetchall()
    print("""
+----+-------------+-------+
| id | date | start_hour   |
+----+---------------------+
""")

    for elem in users:
        print('| {}  | {}  | {} |'.format(elem[0], elem[1], elem[2]))

    print('+----+-------------+-------+')
    connection.commit()
    connection.close()

def list_busy_hours(date):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("SELECT id, date, start_hour FROM Vehicle_repair WHERE vehicle != ? and date = ?;", ('None',date, ))
    users = cursor.fetchall()
    print("""
+----+-------------+-------+
| id | date | start_hour   |
+----+---------------------+
""")
    for elem in users:
        print('| {}  | {}  | {} |'.format(elem[0], elem[1], elem[2]))

    print('+----+-------------+-------+')
    connection.commit()
    connection.close()

def update_repair_start_hour(hour_id, new_start_hour):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE Vehicle_repair SET start_hour = ? WHERE id= ?;", (new_start_hour, hour_id, ))
    cursor.fetchall()

    connection.commit()
    connection.close()

def update_repair_bill(hour_id, new_bill):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE Vehicle_repair SET bill = ? WHERE id= ?;", (new_bill, hour_id, ))
    cursor.fetchall()

    connection.commit()
    connection.close()

def get_vehicle_by_id(vehicle_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("SELECT category, make, model, register_number, gear_box, user_name FROM Vehicle LEFT JOIN BaseUser on owner = BaseUser.id WHERE Vehicle.id= ?;", (vehicle_id, ))
    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result

def get_mechanic_service_by_id(mechanic_service_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("SELECT title, base_id, name FROM Mechanic_services LEFT JOIN Mechanic on mechanic_id = base_id LEFT JOIN Service on service_id = Service.id WHERE Mechanic_services.id= ?;", (mechanic_service_id, ))
    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result

def print_mechanic_services():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.execute("SELECT Mechanic_services.id, title, name ,user_name FROM Mechanic_services LEFT JOIN Mechanic on mechanic_id = base_id LEFT JOIN Service on service_id = Service.id LEFT JOIN BaseUser on mechanic_id = BaseUser.id;")
    users = cursor.fetchall()
    print("""
+----+-------------+-------+
| id | service name |  mechanic name | mechanic title|
+----+---------------------+
""")
    for elem in users:
        print('| {}  | {}  | {} | {}|'.format(elem[0], elem[2], elem[3], elem[1]))

    print('+----+-------------+-------+')


    connection.commit()
    connection.close()



def main():
    delete_repair_hour(5)
    delete_repair_hour(3)

    print("""Hello!
Provide user name:""")
    user_name = input()
    user = check_for_user_by_name(user_name)
    if user == []:
        print("""Unknown user!
Would you like to create new user?""")
        answer = input()
        if answer == 'Yes' or answer == 'yes':
            print("Are you a client or Mechanic?")
            type_of_user = input()
            if type_of_user != 'Mechanic' or type_of_user == 'mechanic' or type_of_user == 'Client' or type_of_user == 'client':
                raise ValueError ('You have only two options: client or mechanic')

            print("Provide user_name:")
            user_name = input()
            print("Provide phone_number:")
            phone_number = input()
            print("Provide email:")
            email = input()
            print("Provide address:")
            address = input()
            add_user(user_name, email, phone_number, address)
            user = check_for_user_by_name(user_name)
            base_id = user[0][0]
            if type_of_user == 'Mechanic' or type_of_user == 'mechanic':
                print('Provide title:')
                title = input()
                add_mechanic(base_id, title)
            else:
                add_client(base_id)

            print("""Thank you, Roza!
Welcome to Vehicle Services!
Next time you try to login, provide your user_name!""")

    else:
        print('Hello, {}!'.format(user_name))
        user_id = user[0][0]

        if check_if_user_is_client(user[0][0]) != []:
            while  True:
                print("""You can choose from the following commands:
            list_all_free_hours
            list_free_hours <date>
            save_repair_hour <hour_id>
            update_repair_hour <hour_id>
            delete_repair_hour <hour_id>
            add_vehicle
            update_vehicle <vehicle_id>
            delete_vehicle <vehicle_id>
            exit""")

                option = input()
                options = option.split(' ')


                if len(options) == 2:
                    second = options[1]
                first = options[0]

                if first == 'list_all_free_hours':
                    list_all_free_hours()
                elif first == 'list_free_hours':
                    list_free_hours(second)
                elif first == 'save_repair_hour':
                    print("Choose Vehicle to repair:")
                    users = get_client_vehicles(user[0][0])
                    if users == []:
                        print('You have no vehicles!')

                    else:
                        print_client_vehicles(users)
                        vehicle_id = input()
                        print("Choose Service:")
                        print_services()
                        service_id = input()
                        save_repair_hour(second, vehicle_id, service_id)
                elif first == 'update_repair_hour':
                    repair_hour = get_repair_hour(second)
                    print(repair_hour)
                    vehicle_id = repair_hour[0][2]
                    info = get_vehicle_by_id(vehicle_id)
                    owner_name = info[0][5]
                    if user_name != owner_name:
                        print('this repair hour is not yours, so you could not change it')
                    else:
                        mechanic_service = get_mechanic_service_by_id(repair_hour[0][4])
                        print(repair_hour[0][4])
                        print(mechanic_service)
                        print("""On {} at {}:
Vehicle: {} {} 
Service: {}
Mechanic:{}
Title:{}
Choose one of the following:
1 - change vehicle
2 - change mechanic service
3 - return to main menu""".format(repair_hour[0][0], repair_hour[0][1], info[0][1], info[0][2], mechanic_service[0][0], mechanic_service[0][1], mechanic_service[0][2]))
                        option = input()
                        if option == '1':

                            print('Choose new vehicle:')
                            vehicles = get_client_vehicles(user_id)
                            print_client_vehicles(vehicles)
                            new_vehicle_id = input()
                            update_vehicle(second, new_vehicle_id)
                        elif option == '2':
                            print("You can choose from the following mechanic services:")
                            print_mechanic_services()
                            new_mechanic_service_id = input()
                            update_mechanic_service(second, new_mechanic_service_id)
                        else:
                            pass
                elif first == 'delete_repair_hour':
                    delete_repair_hour(second)
                elif first == 'add_vehicle':
                    print("Vehicle category:")
                    category = input()
                    print("Vehicle make:")
                    make = input()
                    print("Vehicle model:")
                    model = input()
                    print("Vehicle register number:")
                    register_number = input()
                    print('Vehicle gear box:')
                    gear_box = input()
                    add_vehicle(category, make, model, register_number, gear_box, user_id)
                    print('Thank you! You added new personal vehicle!')
                elif first == 'update_vehicle':
                    print("""Choose one of the following:
1 - change vehicle register number
2 - change vehicle gear box
3 - return to main menu""")
                    option = input()
                    if option == "1":
                        print("enter new register number")
                        new_register_number = input()
                        update_vehicle_register_number(second, new_register_number)
                    elif option == "2":
                        print("enter new gear box")
                        new_gear_box = input()
                        update_vehicle_gear_box(second, new_gear_box)
                elif first == "delete_vehicle":
                    delete_vehicle(second)
                else:
                    break
        else:
            while  True:
                print("""You can choose from the following commands:
list_all_free_hours
list_free_hours <date>
list_all_busy_hours
list_busy_hours <date>
add_new_repair_hour
add_new_service
update_repair_hour <hour_id>
exit""")

                option = input()
                options = option.split(' ')


                if len(options) == 2:
                    second = options[1]
                first = options[0]

                if first == 'list_all_free_hours':
                    list_all_free_hours()
                elif first == 'list_free_hours':
                    list_free_hours(second)
                elif option == 'list_all_busy_hours':
                    list_all_busy_hours()
                elif first == 'list_busy_hours':
                    list_busy_hours(second)
                elif first == "add_new_repair_hour":#TODO да оправя грешката в add_vehicle_repair_hour
                    print("Repair hour date:")
                    repair_hour = input()
                    print("Start Hour:")
                    start_hour = input()
                    add_vehicle_repair(repair_hour, start_hour, None, None, None)
                elif first == "add_new_service":
                    print("Enter service name:")
                    service_name = input()
                    add_service(service_name)
                elif first == "update_repair_hour":
                    repair_hour = get_repair_hour(second)
                    print(repair_hour)
                    vehicle_id = repair_hour[0][2]
                    info = get_vehicle_by_id(vehicle_id)
                    print(info)
                    owner_name = info[0][5]
                    print("""On 23-05-2018 at 10:30:
Client: {}
Vehicle: {} {} 
Current Bill: {}
Choose one of the following:
1 - change start hour
2 - change bill
3 - return to main menu""".format(owner_name, info[0][1], info[0][2], repair_hour[0][3]))

                elif option == 'exit':
                    break








if __name__ == '__main__':
    main()