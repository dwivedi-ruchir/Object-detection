# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:17:03 2020

@author: ruchirdwivedi
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0);

while True:
    #frame = cv2.imread('smarties.png')
    _, frame = cap.read()

    cv2.imshow("frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
