import PrepareGUI
import M
import Database as db
from time import sleep
import tkinter as tk
from tkinter import messagebox

bank = 10_000
PrepareGUI.setDefault()
while True:
    customer_ID = M.getID()  # Return the costumer's ID
    print(customer_ID)
    name, pic = db.getCostumerInfo(customer_ID)  # Return the name of the customer and his pic

    PrepareGUI.setImages(name, pic)

    # total = db.getTotalPrice(ID)
    total = db.getTotalPriceSquare(customer_ID)
    if bank - total > 0:
        bank -= total
    else:
        tk.messagebox.showwarning("No enough money", "We can't find in")

    db.releaseACart(customer_ID)
    sleep(5)  # It should be replaced by a motion sensor that detect if customer pass the enter gate or not

    PrepareGUI.setDefault()
    print(bank)
