import sqlite3
import os
import sys


def main(args):
    inputfile = args[1]
    dbcon = sqlite3.connect('moncafe.db')
    with dbcon:
        cursor = dbcon.cursor()
        with open(inputfile) as inputfile:
            for line in inputfile:
                currentline = line.split(',')
                for i in range(len(currentline)):
                    currentline[i] = currentline[i].strip()

                if int(currentline[1]) > 0:
                    cursor.execute("INSERT INTO Activities VALUES(?,?,?,?)",
                                   (currentline[0], currentline[1], currentline[2], currentline[3]))
                    cursor.execute("SELECT * FROM Products WHERE id=(?)", (currentline[0],))
                    foundline = cursor.fetchone()
                    cursor.execute("UPDATE Products SET quantity=(?) WHERE id=(?)",
                                   (foundline[3]+int(currentline[1]), currentline[0],))

                elif int(currentline[1]) < 0:
                    cursor.execute("SELECT * FROM Products WHERE id=(?)", (currentline[0],))
                    foundline = cursor.fetchone()
                    if foundline[3] + int(currentline[1]) >= 0:
                        cursor.execute("INSERT INTO Activities VALUES(?,?,?,?)",
                                       (currentline[0], currentline[1], currentline[2], currentline[3]))
                        cursor.execute("UPDATE Products SET quantity=(?) WHERE id=(?)",
                                       (foundline[3] + int(currentline[1]), currentline[0],))

    os.system('python3 printdb.py')


if __name__ == '__main__':
    main(sys.argv)