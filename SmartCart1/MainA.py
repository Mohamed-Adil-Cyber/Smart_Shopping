import serial
import winsound
import Database as db

# place the arduino in the correct usb port
ser = serial.Serial('COM15', baudrate=9600, timeout=1)


while True:
    # print('x')
    arduinoData = ser.read_all().decode('ascii')  # Read all data that sent by Arduino

    if arduinoData:
        SArduinoData = arduinoData.split('%%%')  # split the string to (3) parts, (tag_ID, item, customer_ID)

        cart_ID = int(SArduinoData[0].strip())
        tag_ID = SArduinoData[1].strip()
        item = SArduinoData[2].strip()

        winsound.Beep(1500, 105)  # Extra. Can delete it
        db.sendItemToDatabase(cart_ID, item)
        # This function ^ will save the item to database into InStore_Table

# costumer = Database.
