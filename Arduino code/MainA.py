import serial
import Database as db
from mysql.connector import connect




host = input("Enter the host of the database: ")
user = input("Enter the username of the database: ")
passwd = input("Enter the password of the database: ")
database = input("Enter the name of the database: ")




db = connect(
    host,
    user,
    passwd,
    database
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
        price = str(getItemPrice(item) * (float(olcCount)+count))
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













# place the arduino in the correct usb port

Serial = input("Enter the number of the port that the arduino is connected to  [You can find the port number in the device manager]: ")

ser = serial.Serial('COM' + Serial, baudrate=9600, timeout=1)

while True:
    print('x')
    arduinoData = ser.readline().decode('ascii')  # Read all data that sent by Arduino
    # print(arduinoData)
    if arduinoData.strip():
        SArduinoData = arduinoData.split('_')  # split the string to (3) parts, (tag_ID, item, customer_ID)
        cart_ID = int(SArduinoData[2].strip())
        tag_ID = SArduinoData[1].strip()
        item = SArduinoData[0].strip()
        if item == 'IntroToJava':
            item = "Ginkgo"
        if item == 'book':
            item = "SonyHeadphones"
        if item == 'English':
            item = "ConceptsOfOs"

        db.Recommend(item)
        print(cart_ID)
        print(tag_ID)
        print(item)
        db.sendItemToDatabase(cart_ID, item)
        # This function ^ will save the item to database into InStore_Table

