try:
    from tkinter import Tk
except ModuleNotFoundError:
    import os
    os.sys('pip install tkinter')
    from tkinter import Tk
try:
    from tkinter.filedialog import askopenfilename
except ModuleNotFoundError:
    import os
    os.sys('pip install tkinter')
    from tkinter.filedialog import askopenfilename
try:
    import cv2
except ModuleNotFoundError:
    import os
    os.sys('pip install opencv-python')
    import cv2
Tk().withdraw()
filename = askopenfilename()
file = filename
img = cv2.imread(file)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inv = cv2.bitwise_not(grey)
blur = cv2.GaussianBlur(inv, (19, 19), 28)
blur_inv = cv2.bitwise_not(blur)
ske = cv2.divide(grey, blur_inv, scale=240.0)
print('What would you like to save the sketched version as: ')
sfile = input()
cv2.imwrite(f"{sfile}.png", ske)
input()
