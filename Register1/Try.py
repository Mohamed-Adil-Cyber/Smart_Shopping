# modules
import datetime
from tkinter import *


def gui():
    # graphics for program
    # basic window config

    win = Tk()  # GUI window
    win.title("Regestration")  # window title
    fgColour = "#FFFFFF"  # font colour
    bgColour = "#212a7b"  # backgound colour
    text = ("Verdana", 13)
    win.geometry("946x440")  # window size

    # +#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

    # background image for regestration app
    bgImage = PhotoImage(file=r"n.png")
    Label(win, image=bgImage).place(relwidth=1, relheight=1)

    # main title and frame for the program
    titleFrame = Frame(win, bg=bgColour)
    titleFrame.place(relwidth=1, relheight=0.08)

    # main title label widget
    Label(titleFrame,
          text="Smart Shops Regestration",
          font=text,
          anchor=CENTER,
          fg=fgColour,
          bg=bgColour).place(relx=0, relheight=1)

    # +#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

    # date label widget
    date = Label(titleFrame,
                 text=str(datetime.datetime.now())[:10],
                 font=text,
                 anchor=E,
                 fg=fgColour,
                 bg=bgColour)

    date.place(relx=0.82,
               relwidth=0.18,
               relheight=1)

    # label widget for background information box
    bBox = Label(win,
                 fg=fgColour,
                 bg="#153e5f",
                 font=text)

    bBox.place(relx=0.01,
               rely=0.18,
               relwidth=0.635,
               relheight=0.435)

    # +#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

    # label widget for customer name
    cName = Label(win,
                  text="CUSTOMER NAME",
                  fg=fgColour,
                  bg="#1082ad",
                  font=("Bahnschrift", 13))

    cName.place(relx=0.1,
                rely=0.18,
                relwidth=0.25,
                relheight=0.1)

    # label widget for costumer name input
    E1 = Entry(win, bd=5)

    E1.place(relx=0.38,
             rely=0.18,
             relwidth=0.25,
             relheight=0.1)

    # icon for customer name
    brnImg = PhotoImage(file=r"name.png")

    # label of customer name icon
    cIcon = Label(win,
                  bg="#153e5f",
                  image=brnImg)

    cIcon.place(relx=0.02,
                rely=0.18,
                relwidth=0.07,
                relheight=0.1)

    # +#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

    # label widget for national id
    nID = Label(win,
                text="NATIONAL ID",
                fg=fgColour,
                bg="#1082ad",
                font=("Bahnschrift", 13))

    nID.place(relx=0.1,
              rely=0.29,
              relwidth=0.25,
              relheight=0.1)

    # label widget for national id input
    E2 = Entry(win, bd=5)

    E2.place(relx=0.38,
             rely=0.29,
             relwidth=0.25,
             relheight=0.1)

    # icon for national id
    bnnImg = PhotoImage(file=r"national.png")

    # label widget for national id icon
    nIcon = Label(win,
                  bg="#153e5f",
                  image=bnnImg)

    nIcon.place(relx=0.02,
                rely=0.29,
                relwidth=0.07,
                relheight=0.1)

    # +#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

    # label widget for bank account
    bAccount = Label(win,
                     text="BANK ACCOUNT",
                     fg=fgColour,
                     bg="#1082ad",
                     font=("Bahnschrift", 13))

    bAccount.place(relx=0.1,
                   rely=0.40,
                   relwidth=0.25,
                   relheight=0.1)

    # label widget for bank account input
    E3 = Entry(win, bd=5)

    E3.place(relx=0.38,
             rely=0.40,
             relwidth=0.25,
             relheight=0.1)

    # icon for bank card
    bcnImg = PhotoImage(file=r"card.png")

    # label widget for bank card icon
    bcIcon = Label(win,
                   bg="#153e5f",
                   image=bcnImg)

    bcIcon.place(relx=0.02,
                 rely=0.4,
                 relwidth=0.07,
                 relheight=0.1)

    # +#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

    # label widget for picture
    picture = Label(win,
                    text="PICTURE",
                    fg=fgColour,
                    bg="#1082ad",
                    font=("Bahnschrift", 13))

    picture.place(relx=0.1,
                  rely=0.511,
                  relwidth=0.25,
                  relheight=0.1)

    # button widget for choose picture
    cPicture = Button(win,
                      text="CHOOSE PICTURE",
                      fg=fgColour,
                      bg="#1082ad",
                      font=("Bahnschrift", 13))

    cPicture.place(relx=0.38,
                   rely=0.511,
                   relwidth=0.25,
                   relheight=0.1)

    # icon for picture and choose picture
    bpnImg = PhotoImage(file=r"pic.png")

    # label widget for picture and choose picture icon
    cpIcon = Label(win,
                   bg="#153e5f",
                   image=bpnImg)

    cpIcon.place(relx=0.02,
                 rely=0.51,
                 relwidth=0.07,
                 relheight=0.1)

    # +#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

    # background image for save button
    btnImg = PhotoImage(file=r"image.png")

    # button widget for save
    saveBtn = Button(win,
                     text="SAVE",
                     font=("Verdana", 10),
                     image=btnImg,
                     compound=CENTER)

    saveBtn.place(relx=0.30,
                  rely=0.7,
                  relwidth=0.09,
                  relheight=0.1)

    # +#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

    win.mainloop()


# call procedure
gui()
