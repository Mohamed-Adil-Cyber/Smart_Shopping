from mysql.connector import connect

db = connect(
    host="remotemysql.com",
    user="VLwIyxlKeg",
    passwd="RPAo4fNBiy",
    database='VLwIyxlKeg'
)

myCursor = db.cursor()








def sendItemToDatabase(cart_ID, item, count=1):
    myCursor.execute(f"""
        SELECT Item, count FROM InStore_Table WHERE Cart_ID = %s and Item = %s
    """, (cart_ID, item))  # Check if this customer have scanned similar item or not (check by item name)
    myResult = myCursor.fetchall()
    if myResult:  # If this customer have scanned similar item it will update the count
        olcCount = myResult[0][1]
        print(True)
        price = str(getItemPrice(item) * (float(olcCount) + count))
        myCursor.execute(f"""
            UPDATE InStore_Table
            SET count = {olcCount + count}
            WHERE cart_ID = %s AND Item = %s;
        """, (cart_ID, item,))
        db.commit()
        myCursor.execute(f"""
            UPDATE InStore_Table
            SET Total_Price = {price}
            WHERE cart_ID = %s AND Item = %s
        """, (cart_ID, item))
        db.commit()
    else:  # If haven't scanned similar item it will create new row (customer_ID, Cart_ID, Item, Count, Date)
        customer_ID = getCostumerID(cart_ID)  # Will return a customer_ID according to cart number
        price = str(getItemPrice(item) * float(count))
        myCursor.execute(f"""
                INSERT INTO InStore_Table (Customer_ID, Cart_ID, Item, Count, Date, Total_Price) VALUES (%s, %s, %s, %s, DEFAULT, %s)
                        """, (customer_ID, cart_ID, item, count, price))

        db.commit()






def getCostumerID(cart_ID):  # Will return a customer_ID according to cart number
    myCursor.execute(f"""
        SELECT Customer_ID FROM Cart_Table WHERE Cart_ID =%s 
                    """, (cart_ID,))
    costumer_ID = myCursor.fetchall()[0][0]
    return costumer_ID






def getItemPrice(item, count=1):
    myCursor.execute(f"""
        SELECT Product_Price FROM Products_Table WHERE Product_Name =%s 
                    """, (item,))
    myResult = myCursor.fetchall()
    price = float(myResult[0][0])

    return price



def Recommend(item):

    myCursor.execute(f"""
                INSERT INTO Recommendation (Cart_ID, Recommend_Image, Recommend_Item, Origin_Item) VALUES (%s, %s, %s, %s)
                        """, ("1", "https://diegoinstudiocity.files.wordpress.com/2019/10/recom.jpg?w=400&h=282&crop=1", item, ""))

    db.commit()




