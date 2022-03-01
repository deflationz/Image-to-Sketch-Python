try:
    import cv2
except ModuleNotFoundError:
    import os
    os.sys('pip install opencv-python')
    import cv2
print('''Enter your image path, ex: "C:\Users\Admin\Downloads\Image to Sketch Project\image1.jpg"''')
file = input()
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
