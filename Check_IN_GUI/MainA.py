import tkinter as tk
from PIL import ImageTk, Image
import ctypes
print("Start GUI")
# Getting monitor scale --
user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)
imagesFileDirectory = "../_Images"

# Create a window
window = tk.Tk()

# Load Background pic and resize it to fit with the monitor and place it
bImg = Image.open(f"{imagesFileDirectory}/backgroundIN.jpg")
resizedImage = bImg.resize((round(width), round(height)))
backImg = ImageTk.PhotoImage(resizedImage)
backLabel = tk.Label(window, image=backImg)
backLabel.place(height=height, width=width, x=0, y=0)

mainPic = tk.Label(window)
wPicRatio = 0.2895
hPicRatio = 0.45
picWidth = round(width * wPicRatio)
picHeight = round(height * hPicRatio)
mainPic.place(width=picWidth, height=picHeight, relx=0.0677, rely=0.17037)

tkImg = [None]
tkBImg = [None]
# This, or something like it, is necessary because if you do not keep a reference to PhotoImage instances,
# they get garbage collected.

delay = 1000  # in milliseconds


# The function of this function is to refresh the info inside the window
def loopCapture():
    with Image.open(f"{imagesFileDirectory}/ThePicIN.jpg") as mImg:
        mResizedImage = mImg.resize((picWidth, picHeight))
    with Image.open(f"{imagesFileDirectory}/backgroundIN.jpg") as bgImg:
        bgResizedImage = bgImg.resize((width, height))

    tkImg[0] = ImageTk.PhotoImage(mResizedImage)
    tkBImg[0] = ImageTk.PhotoImage(bgResizedImage)

    mainPic.config(image=tkImg[0])
    backLabel.config(image=tkBImg[0])

    window.update_idletasks()
    window.after(delay, loopCapture)


window.attributes("-fullscreen", True)

loopCapture()
window.mainloop()
