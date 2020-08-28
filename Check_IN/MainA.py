import PrepareGUI
import M
import Database as db
from time import sleep

while True:
    theCountOfCarts = 6
    try:
        ID = M.getID()  # Return the customer's ID by recognizing the customer via face recognition (Camera)
    except ValueError:
        print('can not in dataFile file')
        continue
    name, pic = db.getCostumerInfo(ID)  # Return the name of the customer and his pic

    if name == 'Not in the system':
        print("if name == 'Not in the system':")
        continue
    _reservedCarts = db.getReservedCarts()
    ReservedCarts = [int(i[0]) for i in _reservedCarts]
    print('ReservedCarts', ReservedCarts)
    AvailableCarts = [i for i in range(1, theCountOfCarts + 1) if i not in ReservedCarts]
    print('AvailableCarts', AvailableCarts)
    cartNumber = AvailableCarts.pop(0)
    db.bookACart(ID, cartNumber)
    PrepareGUI.setImages(name, pic, cartNumber)  # Will set the images to be used by GUI program
    print('sleep')
    sleep(5)  # It should be replaced by a motion sensor that detect if customer pass the enter gate or not
    print('sleep Done!')

    PrepareGUI.setDefault()  # Will set all images to the default status
