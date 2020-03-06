import sqlite3
import os
import sys


def main(args):
    inputfile = args[1]
    databaseexisted = os.path.isfile('moncafe.db')
    dbcon = sqlite3.connect('moncafe.db')
    with dbcon:
        cursor = dbcon.cursor()

        if not databaseexisted:
            # initiating Employees table
            cursor.execute("CREATE TABLE Employees(id INTEGER PRIMARY KEY,"
                           " name TEXT NOT NULL,"
                           " salary REAL NOT NULL,"
                           "coffee_stand INTEGER REFERENCES Coffee_stand(id))")

            # initiating Suppliers table
            cursor.execute("CREATE TABLE Suppliers(id INTEGER PRIMARY KEY,"
                           "name TEXT NOT NULL,"
                           "contact_information TEXT)")

            # initiating Products table
            cursor.execute("CREATE TABLE Products(id INTEGER PRIMARY KEY,"
                           "description TEXT NOT NULL,"
                           "price REAL NOT NULL,"
                           "quantity INTEGER NOT NULL)")

            # initiating Coffee_stands table
            cursor.execute("CREATE TABLE Coffee_stands(id INTEGER PRIMARY KEY,"
                           "location TEXT NOT NULL,"
                           "number_of_employees INTEGER)")

            # initiating Activities table
            cursor.execute("CREATE TABLE Activities(product_id INTEGER INTEGER REFERENCES Product(id),"
                           "quantity INTEGER NOT NULL,"
                           "activator_id INTEGER NOT NULL,"
                           "date DATE NOT NULL)")

            with open(inputfile) as inputfile:
                for line in inputfile:
                    currentline = line.split(',')
                    for i in range(len(currentline)):
                        currentline[i] = currentline[i].strip()

                    if currentline[0] == 'E':
                        cursor.execute("INSERT INTO Employees VALUES(?,?,?,?)",
                                       (currentline[1], currentline[2], currentline[3], currentline[4]))
                    elif currentline[0] == 'S':
                        cursor.execute("INSERT INTO Suppliers VALUES(?,?,?)",
                                       (currentline[1], currentline[2], currentline[3]))
                    elif currentline[0] == 'C':
                        cursor.execute("INSERT INTO Coffee_stands VALUES(?,?,?)",
                                       (currentline[1], currentline[2], currentline[3]))
                    elif currentline[0] == 'P':
                        cursor.execute("INSERT INTO Products VALUES(?,?,?,?)",
                                       (currentline[1], currentline[2], currentline[3], 0))


if __name__ == '__main__':
    main(sys.argv)