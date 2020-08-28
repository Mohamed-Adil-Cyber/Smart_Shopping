from mysql.connector.errors import InterfaceError
from mysql.connector import connect
from datetime import datetime
from tkinter import messagebox

try:
    db = connect(
        host="remotemysql.com",
        user="VLwIyxlKeg",
        passwd="RPAo4fNBiy",

        database='VLwIyxlKeg'
    )
    myCursor = db.cursor()
except InterfaceError:
    messagebox.showwarning("No Internet", "There is no internet connection")


def getLastID():
    date = str(datetime.today())
    year = date[2:4]
    month = date[5:7]
    day = date[8:10]
    YMD = year + month + day

    myCursor.execute(f"""
            SELECT MAX(ID) FROM Main_Table
    """)
    maxID = myCursor.fetchall()
    if maxID:
        maxID = maxID[0][0]

    myCursor.execute(f"""
            SELECT Customer_ID FROM Main_Table WHERE ID = %s
    """, (maxID, ))
    maxCustomer_ID = myCursor.fetchall()
    if maxCustomer_ID:
        maxCustomer_ID = maxCustomer_ID[0][0]
    # maxCustomer_ID = '11111111111111'
    first6 = maxCustomer_ID[0:6]
    if first6 == YMD:
        newCustomer_ID = first6 + '0000' + str(int(maxCustomer_ID[7:]) + 1)
    else:
        newCustomer_ID = YMD + '00001'
    return newCustomer_ID
    # if myResult[7:] == '00001':


def createAnAccount(fullName, national_ID, bank_Info, pic, customer_ID):

    myCursor.execute(f"""
INSERT INTO Main_Table (ID ,Customer_ID, National_ID, Full_Name, Bank_Card, Pic) VALUES (DEFAULT ,%s, %s, %s, %s, %s)
    """, (customer_ID, national_ID, fullName, bank_Info, pic))

    db.commit()

    return customer_ID
