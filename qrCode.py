# Danish Muhammad Hafidz
# 16521436

import cv2
from pyzbar.pyzbar import decode
import webbrowser

img = cv2.imread("KSM.jpg")

for code in decode(img):
    print(code.type)
    print(code.data.decode("utf-8"))
    webbrowser.open(code.data.decode("utf-8"))
