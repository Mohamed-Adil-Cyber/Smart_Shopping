import serial
import Database as db

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

