from mysql.connector import connect

db = connect(
    host="remotemysql.com",
    user="VLwIyxlKeg",
    passwd="RPAo4fNBiy",

    database='VLwIyxlKeg'
    # host="johnny.heliohost.org",
    # user="neom_CheckOut",
    # passwd="CheckOut",
    # database='neom_entertainment'
)
myCursor = db.cursor()


def getCostumerInfo(customer_ID):
    print('customer_ID', customer_ID)
    myCursor.execute(f"""
        SELECT Full_Name, Pic FROM Main_Table WHERE Customer_ID = '{customer_ID}'
    """)

    myResult = myCursor.fetchall()
    if not myResult:
        return 'Not in the system', 'Not in the system'

    Name = myResult[0][0]
    pic = myResult[0][1]

    output = (Name, pic)
    return output


def getReservedCarts():
    myCursor.execute(f"""
        SELECT Cart_ID FROM Cart_Table
                    """)
    myResult = myCursor.fetchall()
    return myResult


def bookACart(customer_ID, Cart_ID):
    myCursor.execute(f"""
        INSERT INTO Cart_Table (Customer_ID, Cart_ID) VALUES (%s, %s)
                    """, (customer_ID, Cart_ID))
    print('customer_ID', customer_ID)
    db.commit()
