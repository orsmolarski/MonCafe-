import sqlite3
import os
import sys


def main(args):
    dbcon = sqlite3.connect('moncafe.db')
    with dbcon:
        cursor = dbcon.cursor()

        #activities needs to print in order of date while other table in order of primary key

        # printing activities tables
        print("Activities Table:")
        cursor.execute("SELECT * FROM Activities ORDER BY date")
        list_of_activities = cursor.fetchall()
        for Activity in list_of_activities:
            print(Activity)

        # printing coffee stand
        print("Coffee_stands Table:")
        cursor.execute("SELECT * FROM Coffee_stands")
        list_of_coffeestands = cursor.fetchall()
        for CoffeeStand in list_of_coffeestands:
            print(CoffeeStand)

        # printing Employees table
        print("Employees Table:")
        cursor.execute("SELECT * FROM Employees ORDER BY name")
        list_of_employees = cursor.fetchall()
        for Employee in list_of_employees:
            print(Employee)

        # printing products table
        print("Products Table:")
        cursor.execute("SELECT * FROM Products")
        list_of_products = cursor.fetchall()
        for product in list_of_products:
            print(product)

        # printing suppliers table
        print("Suppliers Table:")
        cursor.execute("SELECT * FROM Suppliers")
        list_of_suppliers = cursor.fetchall()
        for supplier in list_of_suppliers:
            print(supplier)

        print()
        print("Employees report")
        for Employee in list_of_employees:
            total = 0
            cursor.execute("SELECT * FROM Coffee_stands WHERE id=(?)", (Employee[3],))
            foundline1 = cursor.fetchone()
            building = foundline1[1]

            cursor.execute("SELECT * FROM Activities WHERE activator_id=(?)", (Employee[0],))
            foundline2 = cursor.fetchall()
            for line in foundline2:
                quan = line[1] * -1
                cursor.execute("SELECT * FROM Products WHERE id=(?)", (line[0],))
                foundline3 = cursor.fetchone()
                price = foundline3[2]
                total = total + quan * price

            output = str(Employee[1]) + " " + str(Employee[2]) + " " + str(building) + " " + str(total)
            print(output)

        print()
        print("Activity report")
        for Activity in list_of_activities:
            cursor.execute("SELECT * FROM Products WHERE id=(?)", (Activity[0],))
            foundline1 = cursor.fetchone()
            item = foundline1[1]

            cursor.execute("SELECT * FROM Employees INNER JOIN Activities WHERE id=(?)", (Activity[2],))
            foundline2 = cursor.fetchone()

            if(foundline2!=None):
                employeename = foundline2[1]
            else:
                employeename = 'None'

            cursor.execute("SELECT * FROM Suppliers INNER JOIN Activities WHERE id=(?)", (Activity[2],))
            foundline3 = cursor.fetchone()
            if (foundline3 != None):
                suppliername = foundline3[1]
                output1 ="(" + str(Activity[3]) + ", '" + str(item) + "', " + str(Activity[1]) + ", " + str(
                    employeename) + ", '" + str(suppliername) + "')"
            else:
                suppliername = 'None'
                output1 ="(" + str(Activity[3]) + ", '" + str(item) + "', " + str(Activity[1]) + ", '" + str(
                    employeename) + "', " + str(suppliername) + ")"
            print(output1)


if __name__ == '__main__':
    main(sys.argv)