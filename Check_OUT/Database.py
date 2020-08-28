from mysql.connector import connect

db = connect(
    # host="remotemysql.com",
    # user="VLwIyxlKeg",
    # passwd="RPAo4fNBiy",
    #
    # database='VLwIyxlKeg'
    # host="remotemysql.com",
    # user="aE58i4dIXa",
    # passwd="dnoHY1aeit",
    # database='VLwIyxlKeg'
    host="remotemysql.com",
    user="aE58i4dIXa",
    passwd="dnoHY1aeit",
    database='aE58i4dIXa'
)
myCursor = db.cursor()


def getCostumerInfo(customer_ID):
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


def getTotalPrice(customer_ID):
    myCursor.execute(f"""
        SELECT Item, Count FROM InStore_Table WHERE ID = %s
                    """, (customer_ID,))

    result = myCursor.fetchall()
    price = 0
    for i in result:
        item, count = i
        myCursor.execute(f"""
            SELECT Product_Price FROM Products_Table WHERE Product_Name = %s
                        """, (item,))
        price += myCursor.fetchall()[0][0] * count
    return round(price, 3)


def getTotalPriceSquare(customer_ID):
    finalPrice = 0
    myCursor.execute(f"""
        SELECT Total_Price FROM InStore_Table WHERE Customer_ID = %s
                    """, (customer_ID,))
    result = myCursor.fetchall()

    for totalItemPrice in result:
        finalPrice += totalItemPrice[0]
    return finalPrice


def releaseACart(customer_ID):
    myCursor.execute(f"""
            INSERT INTO orders_archived SELECT * FROM InStore_Table WHERE Customer_ID = %s
                        """, (customer_ID,))
    db.commit()

    myCursor.execute(f"""
        DELETE FROM InStore_Table WHERE Customer_ID = %s
                    """, (customer_ID,))

    db.commit()
    myCursor.execute(f"""
        DELETE FROM Cart_Table WHERE Customer_ID = %s
                    """, (customer_ID,))

    db.commit()
