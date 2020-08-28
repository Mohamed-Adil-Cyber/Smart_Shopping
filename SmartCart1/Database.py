from mysql.connector import connect

db = connect(
    host="johnny.heliohost.org",
    user="neom_entertainment",
    passwd="neomentertainment",

    database='neom_entertainment'
)

myCursor = db.cursor()


def sendItemToDatabase(cart_ID, item, count=1):
    myCursor.execute(f"""
        SELECT Costumer_ID, Item, count FROM InStore_Table WHERE Cart_ID = %s and Item = %s
    """, (cart_ID, item))  # Check if this customer have scanned similar item or not (check by item name)
    myResult = myCursor.fetchall()
    if myResult:  # If this customer have scanned similar item it will update the count
        olcCount = myResult[0][2]
        print(True)
        myCursor.execute(f"""
            UPDATE InStore_Table
            SET count = {olcCount + count}
            WHERE cart_ID = %s AND Item = %s
        """, (cart_ID, item))
        db.commit()
    else:  # If haven't scanned similar item it will create new row (customer_ID, Cart_ID, Item, Count, Date)
        customer_ID = getCostumerID(cart_ID)  # Will return a customer_ID according to cart number
        myCursor.execute(f"""
                INSERT INTO InStore_Table (Customer_ID, Cart_ID, Item, Count, Date) VALUES (%s, %s, %s, %s, DEFAULT)
                        """, (customer_ID, cart_ID, item, count))

        db.commit()


def getCostumerID(cart_ID):  # Will return a customer_ID according to cart number
    myCursor.execute(f"""
        SELECT Customer_ID FROM Cart_Table WHERE Cart_ID =%s 
                    """, (cart_ID,))
    costumer_ID = myCursor.fetchall()[0][0]
    return costumer_ID

# def printDatabase(table_Name):
#     myCursor.execute(f"""
#         SELECT * FROM {table_Name}
#     """)
#     x = myCursor.fetchall()
#     for i in x:
#         print(i)

# sendItemToDatabase(1, 'Som1eItem')
# printDatabase()

